SSH, or Secure Shell, is a network protocol that allows you to securely access and control a remote computer over an unsecured network by encrypting all communication. The connection is encrypted (scrambled, unreadable data), while authentication credentials are never sent over the network, as a public/private key pair is used instead. Once connected and authenticated, you can execute commands on the remote server, transfer files, and manage the system securely.
HTTP (Hypertext Transfer Protocol) is the application-layer protocol that forms the foundation of the World Wide Web. It works on a client-server, request-response model, where a client (like your web browser) sends a request to a server (hosting the content), and the server sends back a response with the requested data. While HTTP itself is a plain-text, stateless protocol, it can be secured using HTTPS, which encrypts the data for private and safe communication.
BERT (Bidirectional Encoder Representations from Transformers) is a language model developed by Google that excels at understanding the context of words in a sentence by analyzing them in relation to all other words in the sentence, bidirectionally. It is a key component in many natural language processing (NLP) tasks, such as search engine results, text classification, question answering, and text summarization. BERT's ability to consider context helps it differentiate the meaning of words like "bank" in "river bank" versus "bank account". A model used in the sentence-transformer Python package, along with its derivatives such as RoBERTa, or DistilBERT.
Intro into github:
🧱 The Big Picture
When you use Git + GitHub, you’re working with two repositories:
1.	Local repository → lives on your computer (what you see in CMD)
2.	Remote repository → lives on GitHub (the one you see on the website)
They are connected — but independent.
You can edit, save, and even create commits locally without internet or GitHub access.
Then you push your changes to GitHub to share or back them up.
________________________________________
🧩 The Basic Workflow
Here’s what happens in each stage:
1. git add
Think of this like “stage my changes.”
You edited files — now Git needs to know which ones you want to include in your next commit:
git add README.md
or to add everything:
git add .
Now those files are staged (ready to be saved permanently).
________________________________________
2. git commit -m "message"
This means: save the current snapshot of staged files inside your local repo.
The -m flag means “message” — it’s how you describe what this change is about:
git commit -m "Fix typo in README"
The commit lives only in your local repository so far.
________________________________________
3. git push
This means: send my local commits to GitHub.
git push origin main
•	origin = the nickname for your GitHub repository (remote)
•	main (or sometimes master) = the branch you’re pushing to
After this, your changes appear on GitHub.com.
________________________________________
🌍 Understanding origin
When you cloned your repo or linked it with:
git remote add origin https://github.com/yourname/yourrepo.git
You created a link — and named it origin.
It’s just a short alias for the GitHub URL.
You could technically have multiple remotes:
•	origin → GitHub
•	backup → maybe GitLab or another GitHub account
But in 99% of cases, you only need origin.
________________________________________
🌿 What are branches?
A branch is like a separate timeline of your project.
•	main (or master) → the default, stable line of development
•	You can create new branches to experiment or develop features without breaking main
For example:
git branch new-feature
git checkout new-feature
Now you’re working in a separate version of the project.
If you’re happy with your changes:
git merge new-feature
That merges your branch back into main.
GitHub encourages this because it allows collaboration:
•	Each developer works in their own branch
•	Then they open a Pull Request to merge back safely
________________________________________
🏷️ What does -M mean?
You’ll usually see this in:
git branch -M main
-M = move/rename the current branch, even if main already exists.
You might need this when:
•	You initialize a repo and rename the default branch from master → main.
________________________________________
⚙️ Summary (mental model)
Command	Meaning	Where it acts
git add	Stage files for the next commit	Local
git commit -m "msg"	Save a snapshot of changes	Local
git push origin main	Upload commits to GitHub	Remote
git pull	Download changes from GitHub	Local
git branch	List branches	Local
git checkout branch	Switch to a branch	Local
git merge branch	Combine branch into another	Local
________________________________________
GitHub publishes their official fingerprints here:
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints

Mistral's 7b response:
Retrieval-Augmented Generation (RAG) is a model architecture that combines the strengths of retrieval models and generation models to improve the performance of text-based AI systems.

Retrieval models are designed to search for relevant information from large datasets, such as pre-trained language models or knowledge bases, based on input queries. Generation models, on the other hand, 
generate new text based on learned patterns in the data.

The RAG approach combines these two components by first using a retrieval model to find the most relevant passages from a large dataset that can help answer a given query. Then, it uses a generation model to generate the final response by combining the information from the retrieved passages and the initial query.

RAG models have shown promising results in various applications, such as question answering, summarization, and chatbots, by providing more accurate and diverse responses compared to traditional generation-only models. They can also be used to offload computational costs from the generation model by retrieving information from a precomputed dataset instead of generating it from scratch.

vs gemma:2b:
**Retrieval-Augmented Generation (RAG)** is a machine learning technique that combines the strengths of both **retrieving** and **generating** data to improve the quality of generated content.

**Here's how it works:**

1. **Retrieval:** The model first searches a large database of existing data (e.g., images, text, code) based on the target content.
2. **Augmentation:** While the model is retrieving data, it also creates new variations of the retrieved content (e.g., different angles, colors, or text styles).
3. **Synthesis:** The combined output from retrieval and augmentation is used to generate new content 
that resembles the original but is different in some way.

**Benefits of RAG:**

* **High-quality generated content:** RAG can generate highly realistic and diverse images, text, and 
other data products.
* **Improved efficiency:** By combining retrieval and generation, RAG can be much faster than traditional text-based methods.
* **Enhanced diversity:** RAG can generate content that is more diverse and interesting than traditional methods.
* **Application to various domains:** RAG has potential applications in various fields, including content creation, marketing, and research.

**Some popular algorithms used for RAG include:**

* **Variational Autoencoders (VAEs)**
* **Generative Adversarial Networks (GANs)**
* **Cycle-Consistent Adversarial Networks (CycleGANs)**

**Key concepts in RAG:**

* **Retrieval:** The process of finding relevant data from a large database.
* **Generation:** The process of creating new content based on the retrieved data.
* **Synthesis:** The merging of different pieces of data to generate new content.

**Overall, RAG is a powerful approach that significantly enhances the quality and efficiency of content generation. It combines the strengths of retrieval and generation to produce high-quality and diverse content.**