from transformers import pipeline
from patterns.observer import Observer
class ChatbotService(Observer):
    def update(self, event: str, data: dict):
        if event == "poll_closed":
            print(f"ChatbotService: Se ha cerrado la encuesta {data['poll_id']}, actualizando respuestas.")

    def __init__(self, model_name="facebook/blenderbot-400M-distill"):
        self.chatbot = pipeline("text-generation", model=model_name)

    def respond_to_message(self, message: str):
        response = self.chatbot(message)
        return response[0]['generated_text']
