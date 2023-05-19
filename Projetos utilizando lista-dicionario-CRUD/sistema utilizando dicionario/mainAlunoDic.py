from menuAlunoDic import menuAlunoDic
from controladorAlunoDic import *

def MainAlunoDic():
    while True:
        opcaoMenu=menuAlunoDic()
        if opcaoMenu==1:
            CadastrarAlunoDic()
        elif opcaoMenu==2:
            #Listar
            ListarAlunoDic()
        elif opcaoMenu==3:
            removeralunodic()
        elif opcaoMenu==4:
            editarAlunoDic()
        elif opcaoMenu==5:
           imprimirBaseAluno()
        elif opcaoMenu==6:
            #sair
            print(" Sair da aplicação ")
            break
        else:
            print("Opção invalida!!")


MainAlunoDic()

