def menuProf():
    opcMenu=None
    while True:
        print("[1] - Cadastrar Professor")
        print("[2] - Listar Professor")
        print("[3] - Remover Professor")
        print("[4] - Listar por diciplina")
        print("[5] - Sair")
        opcMenu = int(input("Digite a Opçao: "))
        return opcMenu
