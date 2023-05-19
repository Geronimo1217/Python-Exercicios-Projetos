
baseAluno = {}
def CadastrarAlunoDic ():
    while True:
        aluno = {}
        matricula= (input('Digite sua Matrícula: '))
        nome=str(input('Digite seu nome: '))
        nota1=float(input('Digite nota 1: '))
        nota2 = float(input('Digite nota 2: '))
        media=(nota1+nota2)/2
        aluno={'matricula': matricula,'nome':nome,'media':media}
        baseAluno[matricula]=aluno
        print("Cadastro realizado com sucesso!!")
        input("Digite qualquer tecla para  contituar!!")
        resp=input('Quer cadastrar mais aluno: [S/N]').upper()
        if resp in 'S':
            pass
        elif resp=='N':
            break
        else:
            print('ERRO! Responda apenas S-sim ou N-não: ')


def ListarAlunoDic():
    print('-=' * 25)
    #print("{:-^80}".format(' '))
    print("{0:<3}{1:<10}{2:<20}{3:<5}".format("Id","Matricula","Nome","Média"))

    cont=1
    for aluno in baseAluno.values():
        print("{0:<3}{1:<10}{2:<20}{3:<5}".format(cont,aluno.get("matricula"),aluno.get("nome"), aluno.get("media")))
        cont+=1
    print('-=' * 25)
    print("Base aluno sem Formatar.:",baseAluno)
    print()


def imprimirBaseAluno():
    print(baseAluno)
    for aluno in baseAluno.values():
        print(aluno)

def verificarmatricula(matricula):
    return (matricula in baseAluno)


def editarAlunoDic():
    matPesquisa=input("Digite a matriculapara pesquisar: ")
    if (verificarmatricula(matPesquisa)):
        for aluno in baseAluno.values():
            if aluno.get("matricula")==matPesquisa:
                resp=int(input('Quer Editar o aluno: 1-[Sim] 2-[Não]'))
                if resp==1:
                    print()
                    nome = str(input('Digite seu nome: '))
                    nota1 = float(input('Digite nota 1: '))
                    nota2 = float(input('Digite nota 2: '))
                    # media=float(input('Digite a media: '))
                    media = (nota1 + nota2) / 2
                    novoAluno = {'matricula': matPesquisa, 'nome': nome, 'media': media}
                    baseAluno[matPesquisa]=novoAluno
                    print("Aluno editado com sucesso!!")
                    input("Digite qualquer tecla para  contituar!!")
                elif resp ==2:
                    break
                else:
                    print('ERRO! Responda apenas 1-sim ou 2-não: ')

    else:
        print("Aluno não cadastrado")
        input("Digite qualquer tecla para  contituar!!")


def removeralunodic():
    matPesquisa=input("Digite a matricula para remover: ")
    if (verificarmatricula(matPesquisa)):
        resp = input('Quer Remover o aluno: [S/N]').upper()
        if resp in 'Ss':
            del baseAluno[matPesquisa]
            print("Aluno Removido com sucesso!!")
    else:
        print("Aluno não cadastrado")
        input("Digite qualquer tecla para  contituar!!")




