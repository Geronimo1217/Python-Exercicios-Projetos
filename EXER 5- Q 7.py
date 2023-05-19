while True:
    a=float(input(" Digite a primeira medida  do triângulo :"))
    b=float(input(" Digite a Segunda medida  do triângulo :"))
    c=float(input(" Digite a Terceira medida  do triângulo :"))

    if (a < b + c):
        True
        print("E um triangulo")

    elif (b < a + c):
        True
        print("E um triangulo")

    elif (c < a + b):

        True
        print("E um triangulo")


    else:
        break
        print("NÃO E um triangulo")
