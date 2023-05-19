def menuAluno():
    opcaoMenu=None
    while True:
        print("[1] - Cadastrar Aluno")
        print("[2] - Calcular Média Geral ")
        print("[3] - Listar Aluno")
        print("[4] - Remover Aluno")
        print("[5] - Imprimir Média de cada Aluno")
        print("[6] - Editar Aluno")
        print("[7] - Sair")
        opcaoMenu=int(input("Digite a Opçao: "))
        return opcaoMenu
