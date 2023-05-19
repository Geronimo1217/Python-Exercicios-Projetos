while True:
    pol= 2.54 #centimetro
    print('\t ----Conversão de medida---- ')
    cm = float(input('Informe o valor em cemtimetros Para ser convertido: '))
    polegada = cm/ pol
    pes=polegada/12
    jarda = pes/3

    print('O valor em pes é :', int(pes))
    print('O valor em Jarda é :', int(jarda))
    print('O valor em polegadas é :', polegada)

    if jarda==1:
        print(" Apenas Uma Jarda ")
    elif jarda > 1:
        print("Varias Jardas ", jarda)
    else:
        break
        print(" ")

    if pes==1:
        print("Apenas um pe ")
    elif pes>1:
        print("Varios PéS",pes)
    else:
        break
        print(" ")

