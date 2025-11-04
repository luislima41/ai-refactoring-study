from domain.entities.user import User

class CreateUser:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, username, email):
        existing = getattr(self.repository, "find_by_email", None)
        if callable(existing) and self.repository.find_by_email(email):
            return {"success": False, "error": f"Email '{email}' already exists"}

        user = User(username, email)
        try:
            user.validate()
        except ValueError as e:
            return {"success": False, "error": str(e)}

        self.repository.save(user)
        return {"success": True, "user": user}
