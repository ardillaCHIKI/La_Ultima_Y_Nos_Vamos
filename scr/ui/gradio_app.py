import gradio as gr
from controllers.ui_controller import UIController

class GradioApp:
    def __init__(self, ui_controller: UIController):
        self.ui_controller = ui_controller

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
