import re

def clean_text(text):
    """
    Clean the extracted resume text.
    """

    # Remove extra spaces, tabs, and newlines
    text = re.sub(r'\s+', ' ', text)

    # Remove leading and trailing spaces
    text = text.strip()

    return text