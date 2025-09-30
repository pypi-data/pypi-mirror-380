import io
import os
import gzip
import pypdf
import zipfile
import tarfile
import requests

from bs4 import BeautifulSoup


def _extract_text_from_pdf(file_path_or_buffer):
    """
    Extracts text from a PDF file given its path or a file-like object.

    Args:
        file_path_or_buffer: A path to a .pdf file or a file-like object.

    Returns:
        The extracted text as a single string.
    """
    text = ""
    try:
        pdf_reader = pypdf.PdfReader(file_path_or_buffer)
        for page in pdf_reader.pages:
            # Add a space to separate text from different pages
            text += (page.extract_text() or "") + " "
    except Exception as e:
        print(f"An error occurred while reading the PDF: {e}")
    return text.strip()


def _extract_text_from_html(html_content):
    """
    Extracts text from HTML content, removing tags and scripts.

    Args:
        html_content: A string containing HTML.

    Returns:
        The extracted plain text.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    # Remove script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()
    return soup.get_text(separator=' ', strip=True)


def _extract_text_from_archive(file_path):
    """
    Extracts text from various archive formats (zip, tar, tar.gz).
    It iterates through the files in the archive and extracts text
    from common text-based file types.

    Args:
        file_path: The path to the archive file.

    Returns:
        A concatenated string of text from all supported files in the archive.
    """
    full_text = ""
    text_extensions = {'.txt', '.md', '.html', '.htm', '.xml', '.csv', '.json'}

    try:
        if zipfile.is_zipfile(file_path):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                for file_info in zip_ref.infolist():
                    if not file_info.is_dir() and os.path.splitext(file_info.filename)[1].lower() in text_extensions:
                        with zip_ref.open(file_info) as file:
                            content = file.read().decode('utf-8', errors='ignore')
                            if file_info.filename.lower().endswith(('.html', '.htm')):
                                full_text += _extract_text_from_html(content) + "\n"
                            else:
                                full_text += content + "\n"
        elif tarfile.is_tarfile(file_path):
            with tarfile.open(file_path, 'r:*') as tar_ref:
                for member in tar_ref.getmembers():
                    if member.isfile() and os.path.splitext(member.name)[1].lower() in text_extensions:
                        file = tar_ref.extractfile(member)
                        if file:
                            content = file.read().decode('utf-8', errors='ignore')
                            if member.name.lower().endswith(('.html', '.htm')):
                                full_text += _extract_text_from_html(content) + "\n"
                            else:
                                full_text += content + "\n"
        elif file_path.endswith('.gz'):
             with gzip.open(file_path, 'rt', encoding='utf-8', errors='ignore') as f:
                full_text = f.read()

    except Exception as e:
        print(f"Failed to process archive {file_path}: {e}")

    return full_text.strip()


def extract_info(input_source, context_window_length):
    """
    Extracts text from a given source (URL, file path, or raw text) and
    splits it into chunks of a specified length.

    Args:
        input_source (str): The source of the text. This can be a URL,
                            a local file path, or a string of plain text.
        context_window_length (int): The maximum length of each text chunk.

    Returns:
        list[str]: A list of text chunks, or an empty list if no text
                   could be extracted.
    """
    if not isinstance(input_source, str) or not input_source:
        return ["Error: Input source must be a non-empty string."]
    if not isinstance(context_window_length, int) or context_window_length <= 0:
        return ["Error: Context window length must be a positive integer."]

    full_text = ""

    # Check if input is a URL
    if input_source.startswith(('http://', 'https://')):
        try:
            response = requests.get(input_source, timeout=15)
            response.raise_for_status()
            content_type = response.headers.get('content-type', '').lower()

            if 'pdf' in content_type:
                with io.BytesIO(response.content) as pdf_buffer:
                    full_text = _extract_text_from_pdf(pdf_buffer)
            elif 'html' in content_type:
                full_text = _extract_text_from_html(response.text)
            else: # Fallback for plain text or other text-based responses
                full_text = response.text
        except requests.exceptions.RequestException as e:
            return [f"Error fetching URL: {e}"]

    # Check if input is a file path
    elif os.path.exists(input_source):
        file_ext = os.path.splitext(input_source)[1].lower()
        if file_ext == '.pdf':
            full_text = _extract_text_from_pdf(input_source)
        elif file_ext in ['.zip', '.tar', '.gz', '.bz2', '.xz']:
            full_text = _extract_text_from_archive(input_source)
        else: # Assume it's a plain text file
            try:
                with open(input_source, 'r', encoding='utf-8', errors='ignore') as f:
                    full_text = f.read()
            except Exception as e:
                return [f"Error reading file: {e}"]

    # Otherwise, treat the input as raw text
    else:
        full_text = input_source

    if not full_text:
        return []

    # Chunk the extracted text
    chunks = [full_text[i:i + context_window_length] for i in range(0, len(full_text), context_window_length)]

    return chunks
