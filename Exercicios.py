
       #  Area do terreno
def area(a, b):
    rest = a * b
    print(f'A largura do terreno de {a} m² × {b} m² é de {rest} m²')

def l():
    print('=' * 20)


l()
print('Gerador de terrenos')
l()
ma = float(input('Alrura do terreno em M² :'))
ml = float(input('Alrura do terreno em M² :'))
l()
area(ma, ml)

        TABUADA que o Usuario digitar
num=int(input("Digite um número ver a tabuada :"))
for c in range(1,11):
    print('{} x {:2}= {} '.format(num,c,num*c))

valores=[]
valores.append(5)
valores.append(9)
valores.append(4)

for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')


li = list()
e = 0
c = 0
while True:
    li.append(int(input('Digite um valor: ')))
    e += 1
    if 5 in li:
        c = 1
    while True:
        sn = str(input('Quer continurar? [S/N]'))
        if sn.upper() == "S" or sn.upper() == "N":
            break
        else:
            print('Você digitou algo errado! Tente Novamente!!')
    if sn.upper() == "N":
        break
print(f'\nVocê digitou {e} Elementos.\nOs valores em ordem decrescente são: {sorted(li, reverse=True)}')
if c == 1:
    print('O numero 5 esta na lista')
else:
    print('O numero 5 não esta na lista')

                # PALINDROMO
frase = str(input('Digite uma frase :')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
#inverso= ''
inverso=junto[::-1]
for letra in range(len(junto) -1, -1, -1):
    inverso+=junto[letra]
print('O inverso de {} é {} '.format(junto,inverso))
if inverso==junto:
    print('Temos um palíndromo!!')
else:
    print('A frase digitada não é um palíndromo!')

ficha=list()
while True:
    nome = str(input('Nome: '))
    nota1=float(input("nota1 :"))
    nota2=float(input("nota2 :"))
    media=(nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resp=str(input('Quercontinuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4} {"Nome":<10} {"Média":>8}')
print('-'*26)
for i,a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')
while True:
    print('-=' * 35)
    opc= int(input('Mostrar notas de qual aluno? (999 interrompe) :'))
    if opc==999:
        print('FINALIZANDO...')
        break
    if opc<=list(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
        print('<<<VoLTESEMPRE>>>')


