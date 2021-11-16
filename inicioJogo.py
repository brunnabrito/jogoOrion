from projetofinalmodulo1 import *
from historiaDora import *
from historiaGin import *
from historiaKevin import *

# FUNÇÃO PARA INICO DE JOGO
def inicioJogo():
    if personagemEscolhido == 'DORA':
        fase1Dora()

    elif personagemEscolhido == 'GIN':
        fase1Gin()

    elif personagemEscolhido == 'KEVIN':
        fase1Kevin()

    else:
        titulos('Digite uma opçao válida!')
        inicioJogo()
        

# FUNÇAO PARA REINICIAR JOGO
def reinicioJogo():
    global personagemEscolhido
    global seguirJogo
    seguirJogo = int(input('FIM DE JOGO, DESEJA REINICIAR? \n[1] SIM \n[2] NÃO \n\nINFORME A OPÇÃO DESEJADA: '))
    linha()
    
    if seguirJogo == 1:
        while True:
            input('DIGITE ENTER PARA CONTINUAR: ')
            os.system('clear' or 'cls')
            menuInicial()
            personagemEscolhido = definePersonagem()
            inicioJogo()
            seguirJogo = 0
        
    elif seguirJogo ==2:
        exit

    else:
        titulos('Digite uma opção válida')
        reinicioJogo()

inicioJogo()
reinicioJogo()