from langchain.text_splitter import RecursiveCharacterTextSplitter

class TranscriptSplitter:
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

    def split(self, transcript: str):
        return self.splitter.create_documents([transcript])
