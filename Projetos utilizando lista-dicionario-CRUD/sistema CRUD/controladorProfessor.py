lstProfessor=[]


def ChecarMatricula(matriculaPesquisa):
    for i,professor in enumerate(lstProfessor):
        if professor[0] == matriculaPesquisa:
            print(professor)
            print(lstProfessor[i])
            input('Digite qualquer tecla para continuar!!  ')
            return True
    return False

def CadastroProf():
    while True:
        professor=[]
        matricula=input("Digite a matricula do Professor: ")
        if ChecarMatricula(matricula):
            print("Professor já cadastrado!!")
            input('Digite qualquer tecla para continuar!!  ')
            break
        nome=input("Digite o nome do Professor: ")
        diciplina=input("digite a diciplina: ")
        professor=[matricula,nome,diciplina]
        lstProfessor.append(professor)
        print('Professor Cadastrado!!')
        resp=input('Quer cadastrar outro Professor? [S/N]')
        if resp in 'Nn':
            break


def ListarProfessor():
    print('-='*38)
    for i,professor in enumerate(lstProfessor):
        print(f'indice {i} Matricula:{professor[0]} nome:{professor[1]}  diciplina: {professor[2]}')
        print('-=' * 40)

def removerProfessor():
    matriculaPesquisa=input("Digite a matricula para Pesquisar:")

    for i,professor in enumerate(lstProfessor):
        if professor[0]==matriculaPesquisa:
            lstProfessor.pop(i)
            print('Registro excluido!!')
            input('Digite qualquer tecla para sair: ')
            return
        else:
            print("Aluno não encontrado!!")
            input("Digite qualquer tecla para continuar!!")


def ListraPorDiciplina():
    print('-='*38)
    for i, prof in enumerate (lstProfessor):
        print(prof[2])
        print('-=' *10)


