from pypdf import pdf, PdfReader, PdfWriter
from typing import List, Optional
from io import BytesIO

def extract_text_from_pdf(file:BytesIO) -> List[str]:
    """ read pdf files

    Args:
        file (BytesIO): file path

    Returns:
        List[str]: pdf content
    """
    reader = PdfReader(file)
    text = ' '
    for page in reader.pages:
        text = text + page.extract_text() or ''
    return text