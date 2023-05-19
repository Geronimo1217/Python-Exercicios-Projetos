
idade=int(input("Qual é sua idade? :"))
reside=int(input("Você reside a quanto tempo nos estados unidos? :"))
print("Você é cidadão dos Estados Unidos :")
cidadao=input(" Se sim você é nato ou naturalizado? :")
apto=True

if idade < 35 and  reside <14:
            apto= False
elif('nato' == cidadao or 'naturalizado' == cidadao) and (apto):
    apto=True
    print("Você está apto para concorrera Precidência dos Estados Unidos da América!!!!/n")
else:
    print("Infelismente Você NÃO está apto para concorrera Precidência dos Estados Unidos da América/n")