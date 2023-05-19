# Atividade utilizando LISTa
baseBolo=[]
def cadastrarBolo():
    while True:
        bolo=[]
        codigo=input('Digite o codigo: ')
        tipo=input('tipo de bolo ou sabor: ')
        qtdBolo=int(input("Quantidade de bolo: "))
        preco=float(input('Preço do bolo: '))
        bolo=[codigo,tipo,qtdBolo,preco]
        baseBolo.append(bolo)
        print('Cadastro realizado com sucesso!! ')
        resp=int(input('Quer cadastar mais? [1]-sim [2]-Não '))
        if resp==2:
            break

def listarBolo():
    print('-=' * 30)
    print(f'{"Ind":<4} {"Cod.":<4} {"Tipo":<10} {"Qtd":<10} {"Preço":<10}')
    for i,bolo in enumerate(baseBolo):
        print(f'{i:<4} {bolo[0]:<4} {bolo[1]:<10} {bolo[2]:<10} {bolo[3]:<10}')

def editarbolo():
    codpesq=input('Digite o codigo seu: ')
    for i, bolo in enumerate(baseBolo):
        if bolo[0]==codpesq:
            resp=int(input('Quer editar os dados de bolo? [1]-sim [2]-não : '))
            if resp==1:
                cod = input('Digite o codigo: ')
                bolo[0]=codpesq
                novotipo=input('Digite o sabor ou o tipo de bolo :')
                bolo[1]=novotipo
                qtdbolo=int(input('Quantidade de bolo : '))
                bolo[2]=qtdbolo
                novopreco=float(input('novo preço :'))
                bolo[3]=novopreco
                baseBolo[i]=bolo

def removerBolo():
    codPes = input('Digite matricula para excluir aluno: ')
    for i, bolo in enumerate(baseBolo):
        if bolo[0] == codPes:
            baseBolo.pop(i)
            print("Registro excluido com sucesso!!")
            input("Digite qualquer tecla para continuar!!")
            return
        else:
            print("Aluno não encontrado!!")
            input("Digite qualquer tecla para continuar!!")





cadastrarBolo()
print('Listar')
listarBolo()
print('editar')
editarbolo()
listarBolo()
print('Remover')
removerBolo()
listarBolo()
