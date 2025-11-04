def render_users(users):
    print("\n" + "="*60)
    print("LISTA DE USUÁRIOS")
    print("="*60)
    for i, u in enumerate(users, 1):
        status = "✓ Ativo" if u.active else "✗ Inativo"
        print(f"{i}. {u.username} ({u.email}) - {status}")
    print("="*60)

def render_user_detail(user):
    print("\n" + "="*60)
    print("DETALHES DO USUÁRIO")
    print("="*60)
    print(f"Nome: {user.username}")
    print(f"E-mail: {user.email}")
    print(f"Cadastrado em: {user.created_at.strftime('%d/%m/%Y às %H:%M:%S')}")
    print(f"Status: {'Ativo' if user.active else 'Inativo'}")
    print("="*60)

def render_error(message):
    print(f"❌ ERRO: {message}")

def render_success(message):
    print(f"✅ {message}")

def render_statistics(stats):
    print("\n" + "="*60)
    print("ESTATÍSTICAS DO SISTEMA")
    print("="*60)
    print(f"Total de usuários: {stats['total']}")
    print(f"Usuários ativos: {stats['active']}")
    print(f"Usuários inativos: {stats['inactive']}")
    print("="*60)