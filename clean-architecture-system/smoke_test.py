from interface.user_interface import criar_usuario, listar_usuarios, listar_usuarios_ativos, detalhar_usuario, atualizar_usuario, remover_usuario

print("[Smoke] Creating users...")
criar_usuario("alice", "alice@example.com")
criar_usuario("bob", "bob@example.com")

print("\n[Smoke] Listing all users...")
listar_usuarios()

print("\n[Smoke] Listing active users...")
listar_usuarios_ativos()

print("\n[Smoke] Detailing 'alice'...")
detalhar_usuario("alice")

print("\n[Smoke] Updating 'alice' email...")
atualizar_usuario("alice", new_email="alice@newmail.com")
detalhar_usuario("alice")

print("\n[Smoke] Removing 'bob'...")
remover_usuario("bob")
listar_usuarios()
