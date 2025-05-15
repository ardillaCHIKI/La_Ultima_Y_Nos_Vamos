from transformers import pipeline
from src.services.poll_service import PollService

class ChatbotService:
    def __init__(self, poll_service: PollService):
        self.chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")
        self.poll_service = poll_service
        self.user_histories = {}  # Historial opcional de conversación por usuario

    def respond_to_message(self, username: str, message: str):
        # Verificar si la pregunta menciona términos relacionados con encuestas
        encuesta_keywords = ["quién va ganando", "cuánto falta", "resultado encuesta", "estado encuesta"]

        if any(keyword in message.lower() for keyword in encuesta_keywords):
            return self._handle_poll_question(message)

        # Si no hay coincidencias, delegar al modelo de IA
        response = self.chatbot(message)
        return response[0]['generated_text']

    def _handle_poll_question(self, message: str):
        # Determinar el tipo de consulta
        if "quién va ganando" in message.lower():
            return self.poll_service.get_live_results()

        elif "cuánto falta" in message.lower():
            return self.poll_service.get_poll_time_remaining()

        return "No encontré una encuesta relacionada, prueba con otra pregunta."
