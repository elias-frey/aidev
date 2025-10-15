# Package imports

from PyPDF2 import PdfReader
import re

# Extracting text from a PDF file
pdf_path = "C:/Users/Manuscript/OneDrive/My laptop/Studies/Career/workshop/materials/datasets/2023 Stock market volatility.pdf"
def extract_text_pages(pdf_path):
    """Return a list with one string per PDF page (preserves page boundaries)."""
    reader = PdfReader(pdf_path)
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return pages
pages=extract_text_pages(pdf_path)  # list[str]
text = "\n".join(pages)        # full document as before
#print(pages[:2])  # Print the first 1 page of the extracted text
# Orginizing content according to headings

NUMBERED_HEADING = re.compile(r'^\d\.+(\d\.?)*\s+[A-Z][^.]*')     # , re.MULTILINE1. or 1.2 headings with uppercase from ChatGPT
ALLCAPS_STRICT = re.compile(r'^[A-Z\s]{3,}$')  
def find_heading_lines(text):
    """Return list of (line_index, line_text) for lines that look like headings."""
    data = []
    lines = text.splitlines()
    for idx, ln in enumerate(lines): # originaly for idx, ln in enumerate(lines):
        s = ln.strip()
        num_match=NUMBERED_HEADING.match(s)
        caps_match=ALLCAPS_STRICT.match(s)
        if not s:       #to skip empty lines 
            continue    #continues to the next iterate 
        # heuristics - you can reorder or combine them
        if num_match:
            data.append({"heading":num_match.group().strip(),"content":s[num_match.end():].strip()}) #saves the heading and the rest of the line in saperate keys in a dictionary
        elif caps_match:
            data.append({"heading":caps_match.group().strip(),"content":s[caps_match.end():].strip()}) 
        elif not data:
            data.append({"heading": "UNLABELED", "content": s})  #handles the case when the document starts with content before any heading
        else:    
            data[-1]["content"] += " " + s if data else s  #appends the content to the last heading found, if no heading found it saves the content with empty heading
    return data
data=find_heading_lines(text)
print(data)  # Print first 5 detected headings with their content to verify



# NUMBERED_HEADING = re.compile(r'^\d\.+(\d\.?)*\s+[A-Z][^.]*')    # , re.MULTILINE1. or 1.2 headings with uppercase from ChatGPT
# ALLCAPS_STRICT = re.compile(r'^[A-Z\s]{3,}$')                       # stricter uppercase

# def find_heading_lines(text):
#     """Return list of (line_index, line_text) for lines that look like headings."""
#     headings = []
#     lines = text.splitlines()
#     for idx, ln in enumerate(lines):
#         s = ln.strip()
#         if not s:
#             continue  
#         if NUMBERED_HEADING.match(s): # heuristics - you can reorder or combine them
#             headings.append( NUMBERED_HEADING.match(s).group().strip()) #idx, s)
#         elif ALLCAPS_STRICT.match(s):
#             headings.append(ALLCAPS_STRICT.match(s).group().strip()) #idx, s)
#     return headings
# headings=find_heading_lines(text)
# print(headings[:])  # Print first 10 detected headings to verify#