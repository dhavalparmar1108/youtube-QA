from langchain_community.vectorstores import FAISS

class VectorStore:
    def __init__(self, chunks, embeddings):
        self.vector_store = FAISS.from_documents(chunks, embeddings)

    def get_store(self):
        return self.vector_store
