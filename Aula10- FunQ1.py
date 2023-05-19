

def cabelho():
    print(" Lista de Estrutura de repetição 06 ")
    print("Soma dos número de 1 até 100 ")

def main():
    '''
    Programa que Calcula o somatório dos números de 1 a 100 e imprima o resultado.
    1 + 2 + 3 + ... + 100.

'''
    soma = 0
    num = int(input("Digite um número :"))

    while num<=100:
        cabelho()
        # calcule a soma
        if num <= 0:
            print("Número invalido!!!!")
            break
        soma = soma+num

       num = int(input("Digite um número :"))

    # imprima a soma
    print("A soma dos números de 1 até 100  é", soma)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()
