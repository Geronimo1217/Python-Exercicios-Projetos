idade=int(input("Digite sua idade :"))
print("Você tem licenca?")
licenca1=int(input("Digite 1-sim ou 2-não:"))
print("Seu pai tem licença?")
licenca2=int(input("Digite 1-sim ou 2-não"))


if idade <=15 and licenca2==1:
        print("Você pode pescar")
elif idade <= 15 and licenca2 == 2:
            print("Você NÃO pode pescar")
elif 16>=idade and licenca1==1:
        print("Você pode pescar")

else:
    print("você não pode pescar!!")



