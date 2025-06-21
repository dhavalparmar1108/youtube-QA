from langchain.prompts import PromptTemplate

class PromptBuilder:
    def __init__(self, template: str = None):
        # Default template if not provided
        self.template = template or """
            You are a helpful assistant.
            Use the provided context of video transcript to answer.
            If the context is insufficient, just say you don't know.

            {context}
            Question: {question}
        """

        self.prompt = PromptTemplate(
            template=self.template,
            input_variables=["context", "question"]
        )

    def get_prompt(self):
        return self.prompt
