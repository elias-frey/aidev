#Package imports
from PyPDF2 import PdfReader

#Data preparation

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

pdf_path = "C:/Users/Manuscript/OneDrive/My laptop/Studies/Career/workshop/materials/datasets/2023 Stock market volatility.pdf" 
text = extract_text_from_pdf(pdf_path)
print(text[:500])  # Print the first 500 characters of the extracted text