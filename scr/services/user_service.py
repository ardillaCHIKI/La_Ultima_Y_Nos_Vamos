from models.user import User
from repositories.user_repository import UserRepository
import hashlib

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.users = {}

    def register_user(self, username: str, password: str):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        user = User(username, password_hash)
        self.users[username] = user
        self.user_repository.save_user(user)

    def verify_user(self, username: str, password: str) -> bool:
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        user = self.users.get(username)
        return user and user.password_hash == password_hash
