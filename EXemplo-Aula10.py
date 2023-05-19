def cabecalho():
    print("Curso Sistema de Informaação")
    print("Introdução a Programação ")

def cabecalho2(exercicio,listaExercicio):
    print("Exercicio ",exercicio,"-",listaExercicio)

def exer03():
    #msg= "Exercício 03 - Lista Estrutura de Controle"
    #print("Cadastrar Funcionário")
    #print("Exercicio 3 ")
    cabecalho2(" 03 ", "Lista Estrutura de Controle ")
    diaVencimento=10
    valorDesconto=0.0
    diapagamento=int(input("Digite o Dia de pagamento:"))
    valorPrestacao=float(input("Digite o valor da prestação:"))
    diasAtraso=diapagamento-diaVencimento
    if(diasAtraso<=0):
        valorDesconto=valorPrestacao*0.10
    elif (diasAtraso<=5):
         valorDesconto=0.0
    else:
        valorMulta=(valorPrestacao*0.02)*diasAtraso
    valorTotal=(valorPrestacao+valorMulta)-valorDesconto

    print("O valor  Total a pagar: %.2f" % (valorTotal))

def exer08():
    msg = "Exercício 08 - Lista Estrutura de Controle"
    # print("Cadastrar Funcionário")
    # print("Exercicio 08")
    cabecalho2(" 08 ","Lista Estrutura de Controle ")
    nota=float(input("Por favor, insira sua porcentagem de pontos:"))
    if (nota>=93.33):
        print("Você ganhou um A na classe")
    elif (nota>=90.00):
        print("Você ganhou um A- na classe")
    elif (nota >= 86.67):
        print("Você ganhou um B+ na classe")
    elif (nota >=83.33):
        print("Você ganhou um B na classe")
    elif (nota >= 80.00):
        print("Você ganhou um B- na classe")
    elif (nota >= 76.67):
        print("Você ganhou um C+ na classe")
    elif (nota >=73.33):
        print("Você ganhou um C na classe")
    elif (nota >= 70.00):
        print("Você ganhou um C- na classe")
    elif (nota >= 66.67):
        print("Você ganhou um D+ na classe")
    elif (nota >= 63.33):
        print("Você ganhou um D na classe")
    elif (nota >= 60.00):
        print("Você ganhou um D- na classe")
    else:
        print("Você ganhou um F na classe")

def exer05():

    cabecalho2(" 05 ", "Lista Repetição ")
    # print("Exercicio 5 ")
    cont=0
    qtM=0
    qtF=0
    somaIdadeF=0
    somaIdadeH=0
    while (cont<=4):
        cont+=1
        sexo=input("Digite seu sexo: M- Masculino ou F- Feminino")
        idade=int(input("Digite sua idade: "))
        if (sexo=='M' or sexo=='m'):
            qtM= qtM +1
            somaIdadeH=somaIdadeH+idade

        else:
            qtF= qtF +1
            somaIdadeF = somaIdadeF + idade

        if somaIdadeF>=1 and qtF>=1:
             media(somaIdadeF, qtF)
        elif somaIdadeH>=1 and qtM>=1:
            media(somaIdadeH,qtM)
        else:
            print(" Valores Invalidos para calculara Media" )

    print("Idade Media Feminina é :", media(somaIdadeF, qtF))
    print("Idade Media Masculino é :",media(somaIdadeH,qtM))

def exer08l2():
    nota1=float(input("Digite nota 1: "))
 
def media( somatotal,quantidade):
        return somatotal/quantidade


def menu():
    cabecalho()
    print("[1] - Exercicio 03")
    print("[2] - Exercicio 08")
    print("[3] - Exercicio 05 Lista Repetição2")
    print("[4] - Exercicio 08 Lista Repetição2")
    print("[5] - Sair ")
    opcao=int(input("Digite a opção: "))
    return opcao

def main():
    while True:
        opcaoMenu = menu()

        if opcaoMenu==1:
            exer03()
        elif opcaoMenu==2:
            exer08()
        elif opcaoMenu == 3:
            exer05()
        elif opcaoMenu == 4:
            exer08l2()

        elif opcaoMenu==5:
            print("Sair  do programa")
            break
        else:
            print("Opcao Invalida!!!")


main()

