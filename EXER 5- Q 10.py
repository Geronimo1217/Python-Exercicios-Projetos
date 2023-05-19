nome = input("Digite seu nome :")
idade = int(input("Digite sua idade :"))
cont=0



while idade>cont:
    nome=input("Digite seu nome :")
    idade=int(input("Digite sua idade :"))
    cont+=1
    if idade <= 10 and idade >1:
        valor=30.00
        print(" Nome: {} o valor que deverá pagar:{}".format(nome, valor))
    elif idade >10 and idade<=29:
        valor= 60.00
        print(" Nome: {} o valor que deverá pagar:{}".format(nome, valor))
    elif (idade>29)and(idade<=45):
        valor=120.00
        print(" Nome: {} o valor que deverá pagar:{}".format(nome, valor))
    elif(idade>45) and (idade<= 59):
        valor=150.00
        print(" Nome: {} o valor que deverá pagar:{}".format(nome, valor))
    elif (idade>59) and (idade<=65):
        valor=250.00
        print(" Nome: {} o valor que deverá pagar:{}".format(nome, valor))
    elif (idade>65):
        valor=400.00
        print(" Nome: {} o valor que deverá pagar:{}".format(nome, valor))
    else:
        break


