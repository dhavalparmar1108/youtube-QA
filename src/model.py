import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from langchain_community.llms import HuggingFaceEndpoint
# from langchain_community.chat_models import ChatHuggingFace
import yaml

class HuggingFaceLLM:
    def __init__(self):
        load_dotenv()  # Load API key from .env

        self.api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        if not self.api_token:
            raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in environment.")

        config_path = os.path.join("src","params.yaml")
        
        print(config_path)

        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
            self.model_name = config['chat_model']['model_name']
            self.task = config['chat_model']['task']
            self.temperature = config['chat_model']['temperature']

        self.llm = HuggingFaceEndpoint(
            task=self.task,
            model=self.model_name,
            temperature=self.temperature,
        )

        self.chat_model = ChatHuggingFace(llm=self.llm)

    def get_model(self):
        return self.chat_model
