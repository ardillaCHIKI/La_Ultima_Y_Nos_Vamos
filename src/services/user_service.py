import hashlib
import uuid
from src.models.user import User
from src.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.active_sessions = {}

    def register(self, username: str, password: str):
        # Validar si el usuario ya existe
        if self.user_repository.get_user(username):
            raise ValueError("El nombre de usuario ya existe.")

        # Hash de la contraseña usando PBKDF2
        password_hash = hashlib.pbkdf2_hmac(
            'sha256', password.encode(), b'salt', 100000
        ).hex()

        user = User(username, password_hash)
        self.user_repository.save_user(user)
        return "Registro exitoso."

    def login(self, username: str, password: str):
        user = self.user_repository.get_user(username)
        if not user:
            return "Usuario no encontrado."

        # Validación del hash de contraseña
        password_hash = hashlib.pbkdf2_hmac(
            'sha256', password.encode(), b'salt', 100000
        ).hex()

        if user.password_hash != password_hash:
            return "Credenciales incorrectas."

        # Generación de token de sesión UUID
        session_token = str(uuid.uuid4())
        self.active_sessions[username] = session_token
        return f"Login exitoso. Token de sesión: {session_token}"

    def logout(self, username: str):
        if username in self.active_sessions:
            del self.active_sessions[username]
            return "Sesión cerrada correctamente."
        return "Usuario no está logueado."

