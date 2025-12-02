# Visualizing Text Embeddings with PCA and t-SNE
# This script demonstrates how to use text embeddings to visualize relationships that model encoded from data

from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# 1️⃣ Prepare some sample text chunks
chunks = [
    "The cat sits on the mat.",
    "A dog is barking loudly.",
    "Paris is the capital of France.",
    "Berlin is the capital of Germany.",
    "I love playing the guitar.",
    "Music makes me happy."
]

# 2️⃣ Generate embeddings
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(chunks, normalize_embeddings=True)

print("Embeddings shape:", embeddings.shape)  # (6, 384)

# 3️⃣ Reduce dimensionality to 2D
# Option A: PCA (fast, linear)
pca = PCA(n_components=2)
reduced_pca = pca.fit_transform(embeddings)

# Option B: t-SNE (slower, better for visual separation)
tsne = TSNE(n_components=2, random_state=42, perplexity=5)
reduced_tsne = tsne.fit_transform(embeddings)

# 4️⃣ Plot both PCA and t-SNE results
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# PCA plot
axes[0].scatter(reduced_pca[:, 0], reduced_pca[:, 1])
for i, text in enumerate(chunks):
    axes[0].annotate(text, (reduced_pca[i, 0]+0.01, reduced_pca[i, 1]+0.01))
axes[0].set_title("PCA projection")

# t-SNE plot
axes[1].scatter(reduced_tsne[:, 0], reduced_tsne[:, 1])
for i, text in enumerate(chunks):
    axes[1].annotate(text, (reduced_tsne[i, 0]+0.5, reduced_tsne[i, 1]+0.5))
axes[1].set_title("t-SNE projection")

plt.tight_layout()
plt.show()


    
query = embeddings[0:1]  # shape (1, 384)
scores, indices = index.search(query, k=3)  # find top-3 similar
print("Indices:", indices)
print("Scores:", scores)

# Ollama AI Agent Base - Sandbox for Testing Code Snippets

import requests

#This codes generates error due to Ollama's response format: it returns multiple json objects (chunks) instead of a single json object
#This could be adjusted by specifying parameter "stream": False (default is true, which gradually returns tokens/chunks/json objects)
response = requests.post("http://localhost:11434/api/generate", json={
    "model": "gemma:2b", #or "mistral:7b-v0.1"
    "prompt": "What is Retrieval-Augmented Generation",
    "stream": False
})

print(response.json()["response"])

