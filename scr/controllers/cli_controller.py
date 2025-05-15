import argparse
from services.poll_service import PollService

class CLIController:
    def __init__(self, poll_service: PollService):
        self.poll_service = poll_service
        self.parser = argparse.ArgumentParser(description="Gestión de encuestas por terminal")
        self._setup_commands()

    def _setup_commands(self):
        self.parser.add_argument("crear_encuesta", nargs=4, help="Crear encuesta: <poll_id> <pregunta> <opciones separado por comas> <duración en segundos>")
        self.parser.add_argument("listar_encuestas", action="store_true", help="Listar encuestas activas.")
        self.parser.add_argument("cerrar_encuesta", nargs=1, help="Cerrar una encuesta: <poll_id>")
        self.parser.add_argument("ver_resultados", nargs=1, help="Ver resultados de una encuesta: <poll_id>")

    def ejecutar(self, args):
        parsed_args = self.parser.parse_args(args)
        
        if parsed_args.crear_encuesta:
            poll_id, pregunta, opciones, duracion = parsed_args.crear_encuesta
            self.poll_service.create_poll(poll_id, pregunta, opciones.split(","), int(duracion))

        elif parsed_args.listar_encuestas:
            print(self.poll_service.list_active_polls())

        elif parsed_args.cerrar_encuesta:
            poll_id = parsed_args.cerrar_encuesta[0]
            self.poll_service.close_poll(poll_id)

        elif parsed_args.ver_resultados:
            poll_id = parsed_args.ver_resultados[0]
            print(self.poll_service.get_results(poll_id))

