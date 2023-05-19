from menuProf import menuProf
from controladorProfessor import *
def mainprof():
    while True:
        opcMenu=menuProf()
        if opcMenu==1:
            CadastroProf()
        elif opcMenu==2:
            ListarProfessor()
        elif opcMenu==3:
            removerProfessor()
        elif opcMenu==4:
            ListraPorDiciplina()
        elif opcMenu == 5:
            print('Aplicação finalizada!')
            break
        else:
            print("Opção invalida!!")


   # mainprof()