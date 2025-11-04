from typing import List, Optional

class UserRepository:
    def __init__(self):
        self._users: List[object] = []

    def save(self, user: object) -> None:
        self._users.append(user)

    def update(self, username: str, new_email: Optional[str] = None, active: Optional[bool] = None) -> bool:
        user = self.find_by_username(username)
        if not user:
            return False
        if new_email is not None:
            user.email = new_email
        if active is not None:
            user.active = active
        return True

    def delete(self, username: str) -> bool:
        user = self.find_by_username(username)
        if not user:
            return False
        self._users.remove(user)
        return True

    def list_all(self) -> List[object]:
        return list(self._users)

    def list_active(self) -> List[object]:
        return [u for u in self._users if getattr(u, "active", False)]

    def find_by_email(self, email: str) -> Optional[object]:
        return next((u for u in self._users if getattr(u, "email", None) == email), None)

    def find_by_username(self, username: str) -> Optional[object]:
        return next((u for u in self._users if getattr(u, "username", None) == username), None)