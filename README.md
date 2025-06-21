# 🎥 YouTubeRAG: LLM-powered Video Question Answering System

**YouTubeRAG** is a Streamlit-based web application that enables users to ask questions about any YouTube video by simply providing a link. Under the hood, it leverages a Retrieval-Augmented Generation (RAG) pipeline using Hugging Face models, LangChain, and FAISS to deliver accurate, context-aware responses based on the video's transcript.

---

## 🚀 Features

- 🔗 Accepts YouTube video URLs as input
- 🧠 Uses Hugging Face Sentence Transformers to embed video transcripts
- 🔍 FAISS-powered semantic search for transcript chunk retrieval
- 💬 LLM-powered responses using a RAG architecture
- 🌐 User-friendly Streamlit interface for real-time interaction

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Web UI
- **LangChain** – RAG pipeline
- **FAISS** – Vector search for transcript chunks
- **Hugging Face Transformers** – Embeddings and LLM (e.g., `all-MiniLM-L6-v2`)
- **YouTubeTranscriptApi** – Transcript extraction

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/dhavalparmar1108/youtube-QA.git
cd YouTubeRAG
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate 
```
### 3. Install the dependencies
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### Create a .env file in the project root:
    
    HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key

## ▶️ Usage
```bash
streamlit run main.py
```
