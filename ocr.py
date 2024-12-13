import easyocr
from summarize import summarizer


def extract_text(image):
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(image)
    sorted_text_snippets = sorted(result, key=lambda x: x[0][0][1])
    paragraph = ' '.join([text for _, text, _ in sorted_text_snippets])
    return paragraph
 