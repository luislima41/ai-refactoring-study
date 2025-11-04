from typing import Optional

class UpdateUser:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, username: str, new_email: Optional[str] = None, active: Optional[bool] = None):
        user = self.repository.find_by_username(username)
        if not user:
            return {"success": False, "error": f"User '{username}' not found"}

        if new_email:
            existing = self.repository.find_by_email(new_email)
            if existing and existing.username != username:
                return {"success": False, "error": "Email already in use"}

        updated = self.repository.update(username, new_email=new_email, active=active)
        if not updated:
            return {"success": False, "error": "Update failed"}

        return {"success": True, "user": self.repository.find_by_username(username)}
