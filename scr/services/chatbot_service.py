from transformers import pipeline

class ChatbotService:
    def __init__(self, model_name="facebook/blenderbot-400M-distill"):
        self.chatbot = pipeline("text-generation", model=model_name)

    def respond_to_message(self, message: str):
        response = self.chatbot(message)
        return response[0]['generated_text']
