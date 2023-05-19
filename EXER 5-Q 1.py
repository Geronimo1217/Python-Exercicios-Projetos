
while True:
    num = float(input("Digite um número que representa o índice de poluição :"))
    if num<35:
        print("índice de poluição Agradável ")
    elif (num>=35)  or (num<=60):
        print("índice de poluição Desagradável ")
    elif num >60:

        print("índice de poluição Perigoso")
    else:
        print("índice de poluição Inesistente")
    break


