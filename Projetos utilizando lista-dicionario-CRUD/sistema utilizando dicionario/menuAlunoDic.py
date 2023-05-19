


def menuAlunoDic():
    opcaoMenu=None
    while True:
        print("--"*3)
        print("Menu:")
        print("--"*3)
        print('''
        [1] - Cadastrar aluno
        [2] - Listar Aluno
        [3] - Remover Aluno
        [4] - Editar Aluno
        [5] - Imprimir Média de cada Aluno
        [6] - Sair ''')
        opcaoMenu = int(input("Digite a Opçao: "))
        return opcaoMenu