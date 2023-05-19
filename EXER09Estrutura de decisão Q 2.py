codigo = int(input("Digite o codigo do Mês:"))

match (codigo):
    case 1:
        print("Descrição: Janeiro")
    case 2:
        print("Descrição: Fevereiro")
    case 3:
        print("Descrição: Março")
    case 4:
        print("Descrição: Abril")
    case 5:
        print("Descrição: Maio")
    case 6:
        print("Descrição: Junho")
    case 7:
        print("Descrição: Julho")
    case 8:
        print("Descrição: Agosto")
    case 9:
        print("Descrição: Setembro")
    case 10:
        print("Descrição: Outubro")
    case 11:
        print("Descrição: Novembro")
    case 12:
        print("Descrição: Dezembro")
    case _:
        print(" Codigo do mês invalido!!")