import argparse
from src.controllers.cli_controller import CLIController
from src.ui.gradio_app import GradioApp
from src.controllers.ui_controller import UIController
from src.services.poll_service import PollService
from src.services.chatbot_service import ChatbotService
from src.services.nft_service import NFTService
from src.repositories.poll_repository import PollRepository
from src.repositories.user_repository import UserRepository
from src.repositories.nft_repository import NFTRepository
from src.patterns.strategy import AlphabeticalTieBreaker

def main():
    # Configuración de servicios y repositorios
    poll_repository = PollRepository(storage_type='json')
    user_repository = UserRepository(storage_type='json')
    nft_repository = NFTRepository(storage_type='json')

    tiebreaker_strategy = AlphabeticalTieBreaker()
    poll_service = PollService(poll_repository, tiebreaker_strategy)
    chatbot_service = ChatbotService()
    nft_service = NFTService(nft_repository)

    # Controladores
    cli_controller = CLIController(poll_service)
    ui_controller = UIController(poll_service, chatbot_service, nft_service)
    
    # Configuración de argumento para elegir CLI o UI
    parser = argparse.ArgumentParser(description="Sistema de encuestas interactivas para streamers")
    parser.add_argument("--ui", action="store_true", help="Ejecutar con interfaz gráfica Gradio")
    args = parser.parse_args()

    if args.ui:
        print("Iniciando interfaz gráfica con Gradio...")
        app_ui = GradioApp(ui_controller)
        app_ui.launch()
    else:
        print("Iniciando controlador CLI...")
        cli_controller.ejecutar([])  # Puede recibir argumentos desde sys.argv
    
if __name__ == "__main__":
    main()
