# from langchain.embeddings import HuggingFaceEmbeddings
import yaml
from langchain.embeddings import HuggingFaceEmbeddings
import os

class Embedder:
    def __init__(self):

        config_path = os.path.join("src","params.yaml")

        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        self.model_name = config['embedding_model']['model_name']
        self.embeddings = HuggingFaceEmbeddings(model_name=self.model_name)

    def get_embedder(self):
        return self.embeddings

