from application.use_cases.create_user import CreateUser
from application.use_cases.list_users import ListUsers
from application.use_cases.list_active_users import ListActiveUsers
from application.use_cases.get_user import GetUser
from application.use_cases.update_user import UpdateUser
from application.use_cases.delete_user import DeleteUser
from infrastructure.repositories.user_repository import UserRepository

repo = UserRepository()

create_user_uc = CreateUser(repo)
list_users_uc = ListUsers(repo)
list_active_uc = ListActiveUsers(repo)
get_user_uc = GetUser(repo)
update_user_uc = UpdateUser(repo)
delete_user_uc = DeleteUser(repo)


def criar_usuario(username: str, email: str) -> None:
    result = create_user_uc.execute(username, email)
    if result.get("success"):
        user = result["user"]
        print(f"✅ Usuário '{user.username}' criado com sucesso.")
    else:
        print(f"❌ Erro ao criar usuário: {result.get('error')}")


def listar_usuarios() -> None:
    users = list_users_uc.execute()
    if not users:
        print("Nenhum usuário cadastrado ainda.")
        return
    print("\nUsuários cadastrados:")
    for u in users:
        status = "Ativo" if getattr(u, "active", False) else "Inativo"
        print(f"- {u.username} ({u.email}) - {status}")


def listar_usuarios_ativos() -> None:
    users = list_active_uc.execute()
    if not users:
        print("Nenhum usuário ativo.")
        return
    print("\nUsuários ativos:")
    for u in users:
        print(f"- {u.username} ({u.email})")


def detalhar_usuario(username: str) -> None:
    result = get_user_uc.execute(username)
    if not result.get("success"):
        print(f"❌ {result.get('error')}")
        return
    u = result["user"]
    print("\nDetalhes do usuário:")
    print(f"- Nome: {u.username}")
    print(f"- Email: {u.email}")
    print(f"- Ativo: {'Sim' if getattr(u, 'active', False) else 'Não'}")
    created_at = getattr(u, "created_at", None)
    if created_at:
        print(f"- Criado em: {created_at}")


def atualizar_usuario(username: str, new_email: str | None = None, active: bool | None = None) -> None:
    result = update_user_uc.execute(username, new_email=new_email, active=active)
    if result.get("success"):
        print("✅ Usuário atualizado com sucesso.")
    else:
        print(f"❌ {result.get('error')}")


def remover_usuario(username: str) -> None:
    result = delete_user_uc.execute(username)
    if result.get("success"):
        print("🗑️  Usuário removido com sucesso.")
    else:
        print(f"❌ {result.get('error')}")
