lista_compras = []

while True:
    print("\nLista de Compras:")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Listar itens")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        lista_compras.append(item)
        print("Item adicionado com sucesso!")
    elif opcao == "2":
        item = input("Digite o item que deseja remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print("Item removido com sucesso!")
        else:
            print("Item não encontrado na lista.")
    elif opcao == "3":
        print("Itens na lista de compras:")
        for item in lista_compras:
            print("- " + item)
    elif opcao == "4":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
