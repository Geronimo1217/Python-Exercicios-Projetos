

a=range(10)
somador=0
for i in a:
    somador=somador+1
    nota1 = float(input("Digite nota 1 :"))
    nota2 = float(input("Digite nota 2 :"))
    media = (nota1 + nota2) / 2
    if media>=7:
        print("Aprovado!!",media)
    else:
        print("Reprovado com Media :",media)



