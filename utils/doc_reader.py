from docx import Document

def extract_docx_text(file):
    """
    Extract text from a DOCX file.
    """

    doc = Document(file)

    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text