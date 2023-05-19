from menuAluno import menuAluno
from controladorAluno2 import *

def mainaluno():
    while True:
        opcaoMenu=menuAluno()
        if opcaoMenu==1:
            cadastroAluno()
        elif opcaoMenu==2:
            calcularMediaGeral()

        elif opcaoMenu==3:
            listarAluno()
        elif opcaoMenu==4:
            removerAluno()
        elif opcaoMenu == 5:
            # listar M edia de cada Aluno
            imprimirMediaCadaAluno()
            #listar Aluno aprovado
            listarAlunoAprovado()
        elif opcaoMenu == 6:
            editarAluno()
        elif opcaoMenu==7:
            print('Aplicação finalizada!')
            break
        else:
            print("Opção invalida!!")


#mainaluno()