#Eleição municipal da Nerdolandia do Sul candidatos
'''QUESTÃO-1 Construa um programa em Python para computar os votos de três candidatos da eleição
municipal da Nerdolandia do Sul. O primeiro candidato é do partido “Programar para
Vencer” e possui o número 99. O segundo candidato é do partido “A Ciência de Dados” e
possui o número 98. Já o terceiro candidato é do partido “Machine Learning” e possui o
número 97. A Nerdolandia do Sul possui cinco mil moradores. Assim, crie um programa
capaz de receber o voto de todos os moradores da cidade e produza as seguintes
informações:
a) O número de votos, em números absolutos, de cada candidato;
b) O percentual de votos de cada candidato;
c) Quem venceu a eleição;
d) A colocação em ordem de votação dos candidatos'''

cand_99=0
cand_98=0
cand_97=0
nullo=0
contador=1
numeroVotantes=5
while contador<=numeroVotantes:
    print(' \033[1;33;20m--Eleição para Prefeito---- \033[m' )

    print("\033[0;32;29mCandidato número 1 Programar para Vencer, número 99\033[m")
    print("\033[0;10;29mCandidato número 2 A Ciência de Dados número 98\033[m'")
    print("\033[0;15;459mCandidato número 3 Machine Learning 97\033[m'")
    print("\033[0;26;9mDigite zero(0) caso seja voto nullo ou em branco\033[m'")
    voto= int(input("\033[7;33;12mDigite o número seu candidato:\033[m"))
    if (voto==99):
        cand_99+=1
    elif (voto==98):
        cand_98+=1
    elif (voto==97):
        cand_97+=1
    elif (voto==0):
        nullo+=1

    contador+=1
val=[]
val.append(cand_99)
val.append(cand_98)
val.append(cand_97)
val.append(nullo)
val.sort(reverse=True)
print(f"Valores em ordem ",val)

print('-='*30)
percent99=(cand_99*100)/numeroVotantes
percent98=(cand_98*100)/numeroVotantes
percent97=(cand_97*100)/numeroVotantes
percentnullBranco = (nullo * 100) / numeroVotantes
print("Candidato 99:", cand_99)
print("Candidato 98:", cand_98)
print("Candidato 97:", cand_97)
print("Votos Nullos e Brancos:", nullo)
print()
print("Percent Candidato 99:", percent99)
print("Percent Candidato 98:", percent98)
print("Percent Candidato 97:", percent97)
print("Percentual dos votos Nullos e brancos:", percentnullBranco)
if (cand_99>cand_98) and (cand_99>cand_97):
    print("Venceu 99")
elif (cand_98>cand_99) and (cand_98>cand_97):
    print("Venceu 98")
else:
    print("Venceu 97")

''' 2. Escreva um programa em python para ler um número indeterminado de dados, contendo cada um
o peso de um indivíduo e o sexo/gênero. A entrada termina quando for inserido um peso
negativo. Calcular e imprimir:
* A média aritmética dos pesos das pessoas que possuem mais de 90 Kg;
* A média aritmética dos pesos das pessoas que possuem mais de 60 Kg e menos que 87 Kg;
* A média aritmética dos pesos das pessoas do sexo feminino;
* O maior peso.'''






''' 3. Crie um programa em Python que chama uma função que recebe três listas como
parâmetro. O primeiro parâmetro é uma lista de números inteiros, o segundo uma lista de
números reais e o terceiro uma lista caracteres. A função deve mostras as seguintes
informações: (2,5 Pontos)
* A soma dos valores inteiros entre 10 e 40;
* Quantas vogal “a” estão presente na lista; e
* A média dos valores reais;'''


#       Prova - Avaliação I

while True:# Questão 02 -Para fazer o fluxograma
    nome=input('Nome do funcionario: ')
    salario=float(input('Digite seu salario atual: '))
    if (salario<=1200):
        aumento=0.15*salario
        novoSal=salario+aumento
    elif (salario>1200) or (salario <=3000):
        aumento=0.10*salario
        novoSal = salario + aumento
    elif salario>3000:
        aumento=0.05*salario
        novoSal = salario + aumento

    resp=input('Quer Continuar? S/N')
    if resp in 'nN':
        break
print(f'Nome do Funcionario {nome} Aumento {aumento} salario Atual: {salario} Novo Salario:{novoSal}')






#    Questão 03

cont=1
totalSal=0
maior=0
while True:
    Salario=float(input('Digite o salario: '))
    totalSal+=Salario
    cont=cont+1
    if Salario > maior:
        Salario
    r=int(input('Quer continuar? 1-sim 2-Não: '))
    if r==2:
        break

media=(totalSal)/cont
print(f'A média Salarial dos funcionarios é  {media} e o Maior salario é {Salario}')




# Questão 04

def sumRange():
    soma=0
    for n in range(3,7):
        soma=n+soma
    print(f'A soma de todos os números inteiros entre (3 e 6) é: {soma}')

def Main():
    while True:
        print('Digite a opção desejada 1 - chamar a função Sumranger 2 - Sair')
        menu = int(input('Digite a opção:'))
        if menu==1:
            sumRange()
        else:
            break
Main()


#   Questão 05

def main1():
    while True:
        menu=int(input('Digite 1 - folha de pagamento ou 2 - sair'))
        if menu==1:
            folhaPag()
        else:
            print('Sair !!')
            break

def folhaPag():
    while True:
        nome=input('Digite o nome do funcionário: ')
        Salario = float(input('Digite o Salário do funcionário: '))
        if Salario < 0:
            break
        numFilho=int(input('Número de filhos: '))
        Reajuste(Salario, numFilho)
        opc=int(input('Quer cadastrar mais Funcionário? [1-sim 2-Não]: '))
        if opc==2:
            break


def Reajuste(Salario,numFilho):
    if Salario<=500:
        aum=0.30*Salario
    elif (Salario>500) or (Salario<=1000):
        aum = 0.20 * Salario
    elif Salario>1000:
        aum=0.10*Salario

    NovoSalario=Salario+aum+(numFilho*25.00)
    diferenca=NovoSalario-Salario
    print(f'O novo Salário é: {NovoSalario} e a diferença do antigo salário é de: {diferenca}')

folhaPag()

