#Package imports

#Data preparation
from PyPDF2 import PdfReader
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
#print(pages[:500])  # Print the first 500 characters of the extracted text

# Save the extracted text to a .txt file
# with open("extracted_text.txt", "w", encoding="utf-8") as text_file:
#     text_file.write(pages)  # Save the full text to a .txt file

# Orginizing content according to headings

import re

# Example heading patterns (tweak to your document):
NUMBERED_HEADING = re.compile(r'^\d\.+(\d\.?)*\s+[A-Z][^.]*')     # , re.MULTILINE1. or 1.2 headings with uppercase from ChatGPT
ALLCAPS_STRICT = re.compile(r'^[A-Z\s]{3,}$')                       # stricter uppercase
#CENTERED_HEADING = re.compile(r'^\s{10,}([A-Z].+)$')     # not that relevant for plaintext format, shold work with format sensitive pdf extractors PyMuPDF (fitz)

def find_heading_lines(text):
    """Return list of (line_index, line_text) for lines that look like headings."""
    data = []
    lines = text.splitlines()
    for ln in enumerate(lines): # originaly for idx, ln in enumerate(lines):
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
        else:
            data[-1]["content"] += " " + s if data else s  #appends the content to the last heading found, if no heading found it saves the content with empty heading
    return data
data=find_heading_lines(text)
print(data)  # Print first 5 detected headings with their content to verify
#headings=find_heading_lines(text)
#print(headings[:])  # Print first 10 detected headings to verify

def extract_text_with_headings(pdf_path):
    reader = PdfReader(pdf_path)
    data = []
    for page in reader.pages:
        text = page.extract_text()
        lines = text.split("\n")
        for line in lines:
            if re.match(r"^[A-Z][A-Z\s]+$", line.strip()):  # Detect uppercase headings
                data.append({"heading": line.strip(), "content": ""})
            elif data:
                data[-1]["content"] += line.strip() + " "
    return data

def split_text_by_headings(text):
    """Return list of (heading, body_text). If preface text exists before first heading, heading may be None."""
    lines = text.splitlines()
    headings = find_heading_lines(text)
    sections = []
    if not headings:
        return [ (None, text.strip()) ]

    # build sections using line indices
    # build sections using line indices
    for i, (hline_idx, htext) in enumerate(headings):
        # collect body lines from end of this heading line to start of next heading line
        start = hline_idx + 1
        end = headings[i+1][0] if i+1 < len(headings) else len(lines)
        body = "\n".join(lines[start:end]).strip()
        sections.append((htext, body))
    # handle preface if exists
    first_idx = headings[0][0]
    if first_idx > 0:
        pre = "\n".join(lines[:first_idx]).strip()
        if pre:
            sections.insert(0, (None, pre))
    return sections

# Usage with your in-memory text:
sections = split_text_by_headings(text)
for i, (h, b) in enumerate(sections[:5]):
    print("SECTION", i, "HEADING:", h)
    print("BODY (first 120 chars):", b[:120])
    print("-----")


pattern = re.compile(r'^\s*\*\*(.+?)\*\*\s*$', re.MULTILINE)  # lines that are exactly **Heading**
# Find headings with their start positions
headings = [(m.start(), m.end(), m.group(1).strip()) for m in pattern.finditer(text)]

# Split into sections
sections = []
last_index = 0
for i, (start, end, title) in enumerate(headings):
    # content from previous heading end to this heading start
    if i == 0 and start > 0:
        pre = text[:start].strip()
        if pre:
            sections.append(('__pre__', pre))
    # find next heading start or EOF
    next_start = headings[i+1][0] if i+1 < len(headings) else len(text)
    section_body = text[end:next_start].strip()
    sections.append((title, section_body))
# sections is list of (heading, content)
print(sections[:3])  # Print first 3 sections to verify