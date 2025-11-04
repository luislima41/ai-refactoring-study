class GetUser:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, username: str):
        user = self.repository.find_by_username(username)
        if not user:
            return {"success": False, "error": f"User '{username}' not found"}
        return {"success": True, "user": user}
