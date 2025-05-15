# controllers/ui_controller.py
from src.services.poll_service import PollService
from src.services.chatbot_service import ChatbotService
from src.services.nft_service import NFTService

class UIController:
    def __init__(self, poll_service: PollService, chatbot_service: ChatbotService, nft_service: NFTService):
        self.poll_service = poll_service
        self.chatbot_service = chatbot_service
        self.nft_service = nft_service

    def get_active_polls(self):
        return self.poll_service.list_active_polls()

    def vote(self, poll_id, option, user_id):
        try:
            self.poll_service.vote(user_id, poll_id, option)
            return "Voto registrado correctamente."
        except Exception as e:
            return str(e)

    def chat_response(self, message):
        return self.chatbot_service.respond_to_message(message)

    def get_tokens(self, user_id):
        return self.nft_service.get_tokens_by_user(user_id)
