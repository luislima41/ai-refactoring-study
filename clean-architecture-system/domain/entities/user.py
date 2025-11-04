from datetime import datetime
import re

class User:
    def __init__(self, username: str, email: str, active: bool = True, created_at: datetime | None = None):
        self.username = username
        self.email = email
        self.active = active
        self.created_at = created_at or datetime.now()

    def validate(self) -> None:
        if not self.username or len(self.username.strip()) < 3:
            raise ValueError("Username must have at least 3 characters")

        if not self._is_valid_email(self.email):
            raise ValueError("Invalid email format")

    def deactivate(self) -> None:
        self.active = False

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        return re.match(pattern, email) is not None