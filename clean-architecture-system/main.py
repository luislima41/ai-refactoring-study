from interface.user_interface import (
    criar_usuario,
    listar_usuarios,
    listar_usuarios_ativos,
    detalhar_usuario,
    atualizar_usuario,
    remover_usuario,
)

def main():
    while True:
        print("\n=== Sistema Clean Architecture - Usuários ===")
        print("1. Criar novo usuário")
        print("2. Listar todos os usuários")
        print("3. Listar usuários ativos")
        print("4. Detalhar usuário por nome")
        print("5. Atualizar usuário")
        print("6. Remover usuário")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            username = input("Digite o nome de usuário: ")
            email = input("Digite o e-mail: ")
            criar_usuario(username, email)

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "3":
            listar_usuarios_ativos()

        elif opcao == "4":
            username = input("Digite o nome de usuário: ")
            detalhar_usuario(username)

        elif opcao == "5":
            username = input("Nome de usuário: ")
            new_email = input("Novo e-mail (vazio para manter): ").strip()
            active_str = input("Ativar? (s/n vazio para manter): ").strip().lower()
            active = True if active_str == 's' else False if active_str == 'n' else None
            atualizar_usuario(username, new_email if new_email else None, active)

        elif opcao == "6":
            username = input("Nome de usuário para remover: ")
            remover_usuario(username)

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
