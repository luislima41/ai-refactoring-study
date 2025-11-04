from models.user_model import (
    User, add_user, get_all_users, get_user_by_email, 
    get_user_by_username, update_user, delete_user,
    get_active_users, count_users
)
from views.user_view import (
    render_users, render_user_detail, render_error, 
    render_success, render_statistics
)

def create_user(username, email, password=None):
    if get_user_by_email(email):
        render_error("E-mail já cadastrado")
        return False
    
    if get_user_by_username(username):
        render_error("Nome de usuário já existe")
        return False
    
    user = User(username, email, password)
    
    errors = user.validate()
    if errors:
        for error in errors:
            render_error(error)
        return False
    
    add_user(user)
    render_success(f"Usuário '{username}' criado com sucesso!")
    return True

def list_users():
    users = get_all_users()
    if not users:
        print("Nenhum usuário cadastrado.")
        return
    render_users(users)

def list_active_users():
    users = get_active_users()
    if not users:
        print("Nenhum usuário ativo.")
        return
    render_users(users)

def show_user_details(username):
    user = get_user_by_username(username)
    if user:
        render_user_detail(user)
    else:
        render_error(f"Usuário '{username}' não encontrado")

def update_user_controller(username, new_email=None, new_password=None):
    new_data = {}
    if new_email:
        new_data['email'] = new_email
    if new_password:
        new_data['password'] = new_password
    
    if update_user(username, new_data):
        render_success(f"Usuário '{username}' atualizado!")
        return True
    else:
        render_error(f"Usuário '{username}' não encontrado")
        return False

def delete_user_controller(username):
    if delete_user(username):
        render_success(f"Usuário '{username}' removido!")
        return True
    else:
        render_error(f"Usuário '{username}' não encontrado")
        return False

def show_statistics():
    total = count_users()
    active = len(get_active_users())
    inactive = total - active
    
    stats = {
        'total': total,
        'active': active,
        'inactive': inactive
    }
    render_statistics(stats)
