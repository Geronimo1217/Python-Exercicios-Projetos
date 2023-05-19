# Lista para cadastro dos alunos -variável global
lstAluno=[]
#maior=menor=0
def cadastroAluno():
            while True:
                aluno=[]
                matricula=input("Digite a matricula do aluno(a): ")
                if ChecarMatricula(matricula):
                    print('Aluno já cadastrado!!')
                    input('Digite qualquer tecla para continuar!!  ')
                    break
                nome = input("Digite o nome  do aluno(a): ")
                nota1=float(input("Digite a nota 1: "))
                nota2 = float(input("Digite a nota 2: "))
                media=(nota1+nota2)/2
                aluno=[matricula,nome, [nota1,nota2] ,media]
                lstAluno.append(aluno)
                print('Aluno Cadastrado do Aluno Realizado!!')
                resp = str(input('Quer continuar? [S/N] '))
                if resp in 'Nn':
                    break

def ChecarMatricula( matriculaPesquisa ):
    for i,aluno in enumerate(lstAluno):
        if aluno[0]==matriculaPesquisa:
            print(aluno)
            print(lstAluno[i])
            input('Digite qualquer tecla para continuar!!  ')
            return True
    return False


def listarAlunoAprovado():
    listarAlunoAprovado=[]
    for aluno in lstAluno:
        if aluno[3]>=7.0:
            print('-='*38)
            print(f'Matricula: {aluno[0]} seu nome é {aluno[1]} coma a média {aluno[3]}')
            #listarAlunoAprovado.append(aluno)
        #else:
            #listarAlunoReprovado.append(al)

def editarAluno():
    matPesquisa=input('Digite a maticula para pesquizar')
    aluno=[]
    for i,aluno in enumerate(lstAluno):
        if aluno[0]==matPesquisa:
            print('-=' * 38)
            print(f'Matricula: {aluno[0]} seu nome é {aluno[1]} coma a média {aluno[3]}')
            print(aluno)
        resp = str(input('Deseja Editar a Matricula do aluno ? [S/N] '))
        if resp in 'Ss':
            novaMatricula=input("Digite a Nova matricula do aluno(a) para ser Editada: ")
            aluno[0]=novaMatricula
        resp=str(input('Deseja Editar o nome do aluno ? [S/N]'))
        if resp in 'Ss':
            nome=input('Digite o novo nome: ')
            aluno[1]=nome
        resp = str(input('Deseja Editar a nota 1 do  aluno ? [S/N]'))
        if resp in 'Ss':
            novanota1=float(input('Digite a nova nota 1 do aluno: '))
            aluno[2][0]=novanota1
        resp = str(input('Deseja Editar a nota2 do aluno ? [S/N]'))
        if resp in 'Ss':
            novanota2=float(input("digite a nova nota2 do aluno"))
            aluno[2][1]=novanota2
        lstAluno[i]=aluno
        print(aluno)
        print("Aluno Editado com sucesso!!")
        input("Digitequaquer tecla para sair: ")
        return
    print("Aluno não encontrado!")
    input("Digitequaquer tecla para sair: ")




def calcularMediaGeral():
    somaMedia=0.0
    quantidadeAluno=len(lstAluno)

    for aluno in lstAluno:
        somaMedia=somaMedia+aluno[3]
    mediaGeralTurma=somaMedia/quantidadeAluno
    imprimeMediaGeral(mediaGeralTurma)

def imprimeMediaGeral(mediaGeral):
    print("Média geral da turma:", mediaGeral)

def imprimirMediaCadaAluno():
    d=len(lstAluno)
    for  a in lstAluno:
        if a[3] >= 7:
            print(f"[{a[1]}] Aprovado!!{d}", end='')
            print(f'Com Média de {a[3]}')
        else:
            print(f'[ {a[1]} ] Reprovado{d}', end='')
            print(f'Com Média de {a[3]}')
    print()


def listarAluno():
    print('-=' * 30)
    print(f'{"IndiceL":<4} {"Mat.":<4} {"Nome":<10} {"Nota1":<10} {"Nota2":<10} {"Média":>8}')
    print('-' * 49)
    for i,aluno in enumerate(lstAluno):
        print(f'{i:<5} {aluno[0]:<10} {aluno[1]:<10}  {aluno[2][0]:<10} {aluno[2][1]:<10} {aluno[3]:>8.1f}')


def removerAluno():
    matriculaPesquisa=input('Digite matricula para excluir aluno: ')

    for i,aluno in enumerate(lstAluno):
        if aluno[0]==matriculaPesquisa:
            lstAluno.pop(i)
            print("Registro excluido com sucesso!!")
            input("Digite qualquer tecla para continuar!!")
            return
        else:
            print("Aluno não encontrado!!")
            input("Digite qualquer tecla para continuar!!")

