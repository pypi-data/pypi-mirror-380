def build_output_format_from_pydantic_model(schema_dict: dict, indent_level: int = 0) -> str:
    """
    Recursively builds a text-based description of a Pydantic model’s structure.
    """
    INDENT = "\t"
    indent = INDENT * indent_level
    prompt = ""
    
    properties = schema_dict.get("properties", {})
    required_fields = schema_dict.get("required", [])
    definitions = schema_dict.get("$defs", {})

    for prop, info in properties.items():
        # Field metadata
        type_ = info.get("type", "object")
        description = info.get("description", "")
        optional = "optional" if prop not in required_fields else "required"
        enum = info.get("enum")

        # Add base field line
        prompt += f"\n{indent}- {prop} ({type_}, {optional}):\n"
        prompt += f"{indent}{INDENT}- Description: {description or 'No description'}\n"

        # Handle enum
        if enum:
            prompt += f"{indent}{INDENT}- Allowed values: {enum}\n"

        # Handle arrays
        if type_ == "array":
            items = info.get("items", {})
            item_type = items.get("type")

            if "$ref" in items:
                ref_name = items["$ref"].split("/")[-1]
                ref_model = definitions.get(ref_name)
                if ref_model:
                    prompt += f"{indent}{INDENT}- Item type: object defined as:\n"
                    prompt += build_output_format_from_pydantic_model(ref_model, indent_level + 2)
            elif item_type:
                prompt += f"{indent}{INDENT}- Item type: {item_type}\n"

    return prompt