import gradio as gr
from services.nft_service import NFTService
class GradioApp:
    def __init__(self, nft_service: NFTService):
        self.nft_service = nft_service

    def chatbot_response_function(self, username, message):
        return self.chatbot_service.respond_to_message(username, message)

    def launch(self):
        interface = gr.Interface(
            fn=self.ui_controller.get_active_polls,
            inputs=[],
            outputs="text",
            title="Encuestas Activas"
        )

        vote_interface = gr.Interface(
            fn=self.ui_controller.vote,
            inputs=["text", "text", "text"],
            outputs="text",
            title="Votar en Encuesta"
        )

        chatbot_interface = gr.Interface(
            fn=self.ui_controller.chat_response,
            inputs="text",
            outputs="text",
            title="Chatbot IA"
        )

        token_interface = gr.Interface(
            fn=self.ui_controller.get_tokens,
            inputs="text",
            outputs="text",
            title="Galería de Tokens NFT"
        )

        gr.TabbedInterface(
            [interface, vote_interface, chatbot_interface, token_interface],
            ["Encuestas", "Votar", "Chatbot", "Tokens"]
        ).launch()
        
    def show_tokens(self, username):
        tokens = self.nft_service.get_tokens_by_user(username)
        return tokens if tokens else "No tienes tokens."

    def launch(self):
        gr.Interface(
            fn=self.show_tokens,
            inputs="text",
            outputs="text",
            title="Galería de Tokens NFT"
        ).launch()