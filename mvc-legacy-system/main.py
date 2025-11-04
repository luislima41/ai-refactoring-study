from controllers.user_controller import (
    create_user, list_users, list_active_users, 
    show_user_details, update_user_controller,
    delete_user_controller, show_statistics
)

def main():
    while True:
        print("\n" + "="*60)
        print("SISTEMA MVC - GERENCIAMENTO DE USUÁRIOS")
        print("="*60)
        print("1. Cadastrar novo usuário")
        print("2. Listar todos os usuários")
        print("3. Listar usuários ativos")
        print("4. Buscar usuário por nome")
        print("5. Atualizar usuário")
        print("6. Remover usuário")
        print("7. Ver estatísticas")
        print("0. Sair")
        print("="*60)

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- CADASTRO DE USUÁRIO ---")
            username = input("Nome de usuário: ").strip()
            email = input("E-mail: ").strip()
            password = input("Senha (opcional): ").strip()
            create_user(username, email, password if password else None)

        elif opcao == "2":
            list_users()

        elif opcao == "3":
            list_active_users()

        elif opcao == "4":
            username = input("\nDigite o nome de usuário: ").strip()
            show_user_details(username)

        elif opcao == "5":
            print("\n--- ATUALIZAR USUÁRIO ---")
            username = input("Nome de usuário: ").strip()
            new_email = input("Novo e-mail (deixe vazio para não alterar): ").strip()
            new_password = input("Nova senha (deixe vazio para não alterar): ").strip()
            update_user_controller(
                username, 
                new_email if new_email else None,
                new_password if new_password else None
            )

        elif opcao == "6":
            username = input("\nDigite o nome de usuário para remover: ").strip()
            confirmacao = input(f"Confirma remoção de '{username}'? (s/n): ").strip().lower()
            if confirmacao == 's':
                delete_user_controller(username)

        elif opcao == "7":
            show_statistics()

        elif opcao == "0":
            print("\n👋 Encerrando o sistema...")
            break

        else:
            print("\n❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    print("🚀 Iniciando Sistema MVC de Gerenciamento de Usuários")
    main()
