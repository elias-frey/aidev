# Importing the requeired data
import os
from dotenv import load_dotenv
import requests
# Load environment variables from .env
load_dotenv()
# Get your OpenAI API key from environment
openai_api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
pdf_path = os.getenv("DATA_PATH")  # Path to your PDF file from .env file

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
        text += page.extract_text() + "\n" #alt: text.append(page.extract_text() or "")
    return text
#text=extract_text_from_pdf(pdf_path)  # list[str]
#print(text[:500])  # Print the first 1 page of the extracted text

# Orginizing content according to headings

NUMBERED_HEADING = re.compile(r'^\d\.+(\d\.?)*\s+[A-Z][^.]*')     # , re.MULTILINE1. or 1.2 headings with uppercase from ChatGPT
ALLCAPS_STRICT = re.compile(r'^[A-Z\s]{3,}$')  
def find_heading_lines(text):
    """Return list of (line_index, line_text) for lines that look like headings."""
    data = []
    lines = text.splitlines()
    for idx, ln in enumerate(lines):
        s = ln.strip()     #removes leading and trailing whitespace characters from the line
        num_match=NUMBERED_HEADING.match(s) #
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
#data=find_heading_lines(text)
#print(data[3].values())  # Prints headings and contant as values from a list of dictionaries

#Breaking content into smaller chunks for faster/better processing

def chunk_by_headings(data, max_chunk_size=500):
    chunks = []
    for section in data:
        heading = section["heading"]
        content = section["content"].split()
        for i in range(0, len(content), max_chunk_size):
            chunk = " ".join(content[i:i + max_chunk_size])
            chunks.append(f"{heading}\n{chunk}")
    return chunks
#chunks = chunk_by_headings(data)
#print(chunks[:1]) # Print first 2 chunks to verify

#Transforming text into numerical vectors aka embeddings (enabels semantic search, clustering, etc)
from sentence_transformers import SentenceTransformer

def generate_embeddings(chunks):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(chunks, normalize_embeddings=True)
    return embeddings

#embeddings = generate_embeddings(chunks)
#print(embeddings.shape)  # Verify the shape of the embeddings array (num_chunks, embedding_dim)
#print(embeddings)

#Storing data efficiently using FAISS (Facebook AI Similarity Search), an advanced indexing tool

import faiss
import numpy as np
def store_in_faiss(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)  # Inner product similarity
    index.add(np.array(embeddings))
    return index

#index = store_in_faiss(embeddings)
#print(index)  # This Python object is a SWIG wrapper around a C++ FAISS index, returns:
#faiss.swigfaiss_avx2.IndexFlatIP; proxy of <Swig Object of type 'faiss::IndexFlatIP *' at 0x000001E30C6E4930>
#print("Index type:", type(index))
#print("Dimension:", index.d)       # embedding dimension (e.g. 384)
#print("Number of vectors:", index.ntotal)
# example of how to search the index to get similar items
# query = embeddings[0:1]  # shape (1, 384)
# scores, indices = index.search(query, k=3)  # find top-3 similar
# print("Indices:", indices)
# print("Scores:", scores)

# Function to embedd and index query and retrieve relevant chunks
# performs similar tasks to the quere as were previously done to the context (aka knowledgesource/pdf)
def query_faiss(index, query, chunks): 
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    query_embedding = model.encode([query], normalize_embeddings=True)
    distances, indices = index.search(np.array(query_embedding), 5)  # Find top 5 matches
    return [chunks[i] for i in indices[0]]

# Using GROQ cloud model for generating response
from groq import Groq
#user_query = "What factors contribute to stock market volatility?"
def get_answer_fromcloud (context, query):
    client = Groq(api_key=groq_api_key)
    messages = [
        {"role": "system", "content": "You are a helpful assistant that answers questions based on provided context only."},
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}\nAnswer:"}
    ]
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        #max_tokens=300,
        #temperature=0.7
    )
    return response.choices[0].message.content.strip() #returns the generated answer while stripping leading/trailing whitespace

# Using local Ollama model for generating response
# import requests
# def get_answer_with_local_model(context, query, model="mistral"):
#     """
#     Generate an answer from a local Ollama model (e.g., mistral, phi3, gemma)
#     based only on the provided context and query.
#     """
#     prompt = (
#         "You are a helpful assistant that answers questions based strictly on the provided context.\n\n"
#         f"Context:\n{context}\n\n"
#         f"Question: {query}\n\nAnswer:"
#     )
#     response = requests.post("http://localhost:11434/api/generate", json={
#         "model": model,
#         "prompt": prompt,
#         "stream": False,            # disable streaming for simple usage
#         "options": {
#             "num_predict": 300,     # similar to max_tokens
#             "temperature": 0.7
#         }
#     })
#     data = response.json()
#     return data["response"].strip()

# Putting it all together
def main():

    text = extract_text_from_pdf(pdf_path)
    data=find_heading_lines(text)
    chunks = chunk_by_headings(data)
    embeddings = generate_embeddings(chunks)
    index = store_in_faiss(embeddings)
    
    user_query = input("Enter your question: ")
    relevant_chunks = query_faiss(index, user_query, chunks)
    context = "\n".join(relevant_chunks)
    
    #answer = get_answer_with_local_model(context, user_query) #local machine
    answer = get_answer_fromcloud(context, user_query) #, openai_api_key
    print(f"\n Answer: {answer}")

main()