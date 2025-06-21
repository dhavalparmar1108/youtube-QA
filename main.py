import streamlit as st
from src.transcript_loader import TranscriptLoader
from src.text_splitter import TranscriptSplitter
from src.embeddings import Embedder
from src.vectorstore import VectorStore
from src.context_retriever import ContextRetriever
from src.prompt_templates import PromptBuilder
from src.model import HuggingFaceLLM
from src.logger import setup_logger

st.set_page_config(page_title="YouTube Q&A", layout="wide")

st.title("📺 YouTube Video Q&A")

# Step 1: Input YouTube URL
youtube_url = st.text_input("Enter a YouTube video URL:")

logger = setup_logger(__name__)

if youtube_url:

    # Step 2: Load transcript
    logger.info("Load Transcript")
    loader = TranscriptLoader(youtube_url)
    transcript = loader.load_transcript()

    # Step 3: Split transcript
    logger.info("Split Transcript")
    splitter = TranscriptSplitter()
    chunks = splitter.split(transcript)

    # Step 4: Create embeddings
    logger.info("Embedd")
    embedder = Embedder()
    embeddings = embedder.get_embedder()

    # Step 5: Vector Store
    logger.info("vector store")
    vector_store = VectorStore(chunks, embeddings)
    retriever = vector_store.get_store().as_retriever()

    # Step 6: Prompt template + LLM
    logger.info("Prompt Build")
    prompt = PromptBuilder().get_prompt()

    logger.info("Model Build")
    llm = HuggingFaceLLM().get_model()

    logger.info("Get context")
    context_retriever = ContextRetriever(retriever)

    # Step 7: Question from user
    question = st.text_input("Ask a question based on the video:")
    if question:
        context_text = context_retriever.retrieve_context(question)
        final_prompt = prompt.invoke({"context": context_text, "question": question})
        answer = llm.invoke(final_prompt)
        st.markdown("### 🧠 Answer:")
        st.success(answer.content)



