class ContextRetriever:
    def __init__(self, retriever):
        """
        retriever: Any LangChain-compatible retriever (e.g., FAISS.as_retriever())
        """
        self.retriever = retriever

    def retrieve_context(self, question: str) -> str:
        """
        Retrieves relevant documents and joins their contents into one context string.
        """
        retrieved_docs = self.retriever.invoke(question)
        context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
        return context_text
