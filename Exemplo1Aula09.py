
numero1=float(input("Digite o numero 1 :"))
numero2=float(input("Digite o numero 2 :"))
resultado=None
print("[1]- Soma")
print("[2]- Subtração")
print("[3]- Multiplicação")
print("[4]- Divisão")
print()

opcao=int(input("Digite opção: "))

if opcao==1:
    resultado=numero1+numero2
elif opcao==2:
    resultado=numero1 - numero2
elif opcao==3:
    resultado=numero1* numero2
elif opcao==4:
    resultado=numero1/numero2
else:
    print("Opção Invalida!!!")

print("Resultado :", resultado)

