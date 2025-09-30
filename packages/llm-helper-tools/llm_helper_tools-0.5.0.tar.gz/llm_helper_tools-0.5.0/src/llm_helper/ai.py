import os
import json
import time
import logging

from typing import List
from pydantic import BaseModel, ValidationError
from parse_llm_code import extract_first_code
from langchain_core.tools import StructuredTool
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.llms.huggingface_hub import HuggingFaceHub
from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI
from langchain_ollama import ChatOllama
from google.api_core.exceptions import ResourceExhausted


def setup_langchain_llm(
        name: str,
        api_key: str = "",
        args: object = {}
):
    if "openai" in name:
        assert api_key, "Selecting an openai model requires api_key."
        model = ChatOpenAI(
            openai_api_key=api_key,
            model_name=name.split("/")[-1],
            **args
        )
    elif "google" in name:
        assert api_key, "Selecting a google model requires an api_key."
        os.environ["GOOGLE_API_KEY"] = api_key
        model = ChatGoogleGenerativeAI(model=name.split("/")[-1])
    elif "anthropic" in name:
        assert api_key, "Selecting an anthropic model requires an api_key."
        os.environ["ANTHROPIC_API_KEY"] = api_key
        model = ChatAnthropic(
            model=name.split("/")[-1]
        )
    elif "mistral" in name:
        assert api_key, "Selecting a mistral model requires an api_key."
        os.environ["MISTRAL_API_KEY"] = api_key
        model = ChatMistralAI(
            model=name.split("/")[-1]
        )
    elif "ollama" in name:
        model = ChatOllama(
            model=name.split("/")[-1]
        )
    else:
        llm = HuggingFaceHub(
            repo_id=name,
            task="text-generation",
            model_kwargs=args
        )

        model = ChatHuggingFace(llm)

    return model    


"""
    mirostat 	Enable Mirostat sampling for controlling perplexity. (default: 0, 0 = disabled, 1 = Mirostat, 2 = Mirostat 2.0) 	int 	mirostat 0
    mirostat_eta 	Influences how quickly the algorithm responds to feedback from the generated text. A lower learning rate will result in slower adjustments, while a higher learning rate will make the algorithm more responsive. (Default: 0.1) 	float 	mirostat_eta 0.1
    mirostat_tau 	Controls the balance between coherence and diversity of the output. A lower value will result in more focused and coherent text. (Default: 5.0) 	float 	mirostat_tau 5.0
    num_ctx 	Sets the size of the context window used to generate the next token. (Default: 2048) 	int 	num_ctx 4096
    repeat_last_n 	Sets how far back for the model to look back to prevent repetition. (Default: 64, 0 = disabled, -1 = num_ctx) 	int 	repeat_last_n 64
    repeat_penalty 	Sets how strongly to penalize repetitions. A higher value (e.g., 1.5) will penalize repetitions more strongly, while a lower value (e.g., 0.9) will be more lenient. (Default: 1.1) 	float 	repeat_penalty 1.1
    temperature 	The temperature of the model. Increasing the temperature will make the model answer more creatively. (Default: 0.8) 	float 	temperature 0.7
    seed 	Sets the random number seed to use for generation. Setting this to a specific number will make the model generate the same text for the same prompt. (Default: 0) 	int 	seed 42
    stop 	Sets the stop sequences to use. When this pattern is encountered the LLM will stop generating text and return. Multiple stop patterns may be set by specifying multiple separate stop parameters in a modelfile. 	string 	stop "AI assistant:"
    num_predict 	Maximum number of tokens to predict when generating text. (Default: -1, infinite generation) 	int 	num_predict 42
    top_k 	Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative. (Default: 40) 	int 	top_k 40
    top_p 	Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text. (Default: 0.9) 	float 	top_p 0.9
    min_p 	Alternative to the top_p, and aims to ensure a balance of quality and variety. The parameter p represents the minimum probability for a token to be considered, relative to the probability of the most likely token. For example, with p=0.05 and the most likely token having a probability of 0.9, logits with a value less than 0.045 are filtered out. (Default: 0.0) 	float 	min_p 0.05
"""
def query_model(
        models: List[tuple], # Tuple (Model, Timeout in seconds)
        prompt: str, 
        parse_code: bool = False,
        parse_json: bool = False,
        schema: BaseModel = None,
        tools: List = [],
        options: dict = {},
        max_retries: int = 5
    ):
    index = 0

    available_functions = { tool.__name__: tool for tool in tools }
    assert not (len(tools) > 0) or not (parse_json or parse_code),  "Tools can only be used in non-parsing mode" 

    result = None
    for _ in range(0, max_retries):
        try:
            model = models[index][0]

            if tools:
                tools = [StructuredTool.from_function(tool, parse_docstring=True) for tool in tools]
                model = model.bind_tools(tools)

            if schema:
                model.with_structured_output(schema)
            
            start = time.time()
            response = model.invoke([{"role": "user", "content": prompt}])
            time.sleep(max(models[index][1] - (time.time() - start), 0))  # Respect the timeout for the current model

            if parse_json:
                parser = JsonOutputParser()
                if schema:
                    result = schema.model_validate(parser.parse(response.content))
                    return response.content, result.model_dump()
                else:
                    return response.content, parser.parse(response.content)
            elif parse_code:
                code = extract_first_code(response.content)
                return response, code
            elif tools:
                tool_outputs = []
                for tool in response.tool_calls:
                    function_to_call = available_functions.get(tool["name"])
                    if function_to_call:
                        tool_outputs.append(function_to_call(**tool["args"]))
                
                return response, tool_outputs
            else:
                return response, response.content
        except ResourceExhausted:
            logging.warning(f"Resource exhausted for model {models[index]}, switching to next model.")
            index += 1
            if index == len(models):
                exit()
        except json.JSONDecodeError:
            logging.exception("JSON decode error. Retrying with adjusted prompt.")
            prompt += "\n\nPlease ensure the returned structure is valid JSON, escape or remove critical characters."
        except ValidationError:
            logging.exception("Validation error. Retrying with adjusted prompt.")
            prompt += "\n\nPlease ensure the returned structure matches the expected schema."
        except Exception:
            logging.exception("An unexpected error occurred. Retrying with different model if possible.")
            if index < len(models) - 1:
                index += 1

    raise RuntimeError("Maximum retries exceeded. Unable to get a valid response from the models.")
