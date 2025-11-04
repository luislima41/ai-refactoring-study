import re
from datetime import datetime

class User:
    def __init__(self, username, email, password=None):
        self.username = username
        self.email = email
        self.password = password
        self.created_at = datetime.now()
        self.active = True
    
    def validate(self):
        errors = []
        
        if not self.username or len(self.username) < 3:
            errors.append("Nome de usuário deve ter pelo menos 3 caracteres")
        
        if not self._validate_email(self.email):
            errors.append("E-mail inválido")
        
        if self.password and len(self.password) < 6:
            errors.append("Senha deve ter pelo menos 6 caracteres")
        
        return errors
    
    def _validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def deactivate(self):
        self.active = False
    
    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'active': self.active
        }

users_db = []

def add_user(user):
    users_db.append(user)
    return True

def get_all_users():
    return users_db

def get_user_by_email(email):
    for user in users_db:
        if user.email == email:
            return user
    return None

def get_user_by_username(username):
    for user in users_db:
        if user.username == username:
            return user
    return None

def update_user(username, new_data):
    user = get_user_by_username(username)
    if user:
        if 'email' in new_data:
            user.email = new_data['email']
        if 'password' in new_data:
            user.password = new_data['password']
        return True
    return False

def delete_user(username):
    user = get_user_by_username(username)
    if user:
        users_db.remove(user)
        return True
    return False

def get_active_users():
    return [u for u in users_db if u.active]

def count_users():
    return len(users_db)