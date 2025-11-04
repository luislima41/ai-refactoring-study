class DeleteUser:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, username: str):
        deleted = self.repository.delete(username)
        if not deleted:
            return {"success": False, "error": f"User '{username}' not found"}
        return {"success": True}
