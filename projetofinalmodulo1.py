from sys import exit 
from time import sleep
import os


#LISTA DE VARIÁVEIS DE USO GERAL
titulo = ("""
 .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     ____     | || |  _______     | || |     _____    | || |     ____     | || | ____  _____  | |
| |   .'    `.   | || | |_   __ \    | || |    |_   _|   | || |   .'    `.   | || ||_   \|_   _| | |
| |  /  .--.  \  | || |   | |__) |   | || |      | |     | || |  /  .--.  \  | || |  |   \ | |   | |
| |  | |    | |  | || |   |  __ /    | || |      | |     | || |  | |    | |  | || |  | |\ \| |   | |
| |  \  `--'  /  | || |  _| |  \ \_  | || |     _| |_    | || |  \  `--'  /  | || | _| |_\   |_  | |
| |   `.____.'   | || | |____| |___| | || |    |_____|   | || |   `.____.'   | || ||_____|\____| | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
""")
personagens = ("Gin", "Kevin", "Dora", "Voltar")
opcoesMenuInicial = ('Iniciar', 'Créditos', 'Sair')
acoes = ("Ver perfil de cada personagem", "Escolher Personagem", "Voltar")
textoKevin = 'Kevin é um jovem de boa índole porém um pouco atrapalhado. \nÉ o assitente do Gin, eles trabalham na manutenção de Orion.'
textoGin = 'Ranzinza e rabugento, um senhor que sem opção de emprego, faz \nna manutenção de Orion, no metaverso que dominou o mundo \nem 2999.'
textoDora = 'Ambição e traumas fazem parte de sua personalidade, \nprocura o tempo todo meios fáceis de conseguir dinheiro no \nmetaverso.'
personagemEscolhido = ' '
seguirJogo = 0
escolha = 0
fase = 0


#FUNÇÃO PARA INSERIR LINHA
def linha():
    print('=' * 100)


#FUNÇÕES PARA FORMATAÇÕES 
## PREFIXO C PARA COR E PREFIXO B PARA BACK
cRed = '\033[31m'
cEnd = '\033[0m'
cBlu = '\033[34m'
cGre = '\033[32m'
cBol = '\033[;1m'
cInv = '\033[;7m'
bWhi = '\033[1;107m'
cBla = '\033[1;30m'
bCya = '\033[1;46m'

def cabecalho(msg):
    linha()
    linhas = msg.splitlines()
    for l in linhas:
        print(l.center(100))
        sleep(0.4)
    linha()

def titulos(msg):
    print()
    print(bWhi + cBla + msg.center(100) + cEnd)
    print()

def passouDeFase(msg):
    print(cGre + ('=' * 100) + cEnd)
    print(cGre + msg.center(100)+ cEnd)
    print(cGre + ('=' * 100) + cEnd)


def perdeuPlayboy(msg):
    print(cRed + ('=' * 100) + cEnd)
    print(cRed + msg.center(100) + cEnd)
    print(cRed + ('=' * 100) + cEnd)


def subcabecalho(msg):
    linhas = msg.splitlines()
    for l in linhas:
        print(l.center(100))
        sleep(0.4)
    linha()


def enrredo(msg):
    print()
    linhas = msg.splitlines()
    for l in linhas:
        print(cBlu + l.center(100) + cEnd)
        sleep(0.4)
    print()

# FUNÇAO PARA EXIBIR OS CRÉDITOS
def creditos():
    titulos('CRÉDITOS')
    subcabecalho("""Este jogo é um trabalho de conclusão do primeiro módulo da turma 12 do curso de 
Data Analytics da Resilia.""")
    subcabecalho("""Agradeço a Marisa e a Taís pela dedicação, profissionalismo e paciência e ao meu 
grupo Gabriel e Juliano pela parceria e companheirismo, sem vocês seria muito mais 
difícil.""")
    titulos('O JOGO')
    subcabecalho("""ORION é o metaverso que dominou o mundo no final do terceiro milênio, porém devido 
ao BUG DO MILENIO Dora encontrou uma falha que a faz controlar as pessoas e o jovem 
Kevin caiu em uma de suas armadilhas vituais. Agora Gin terá que salvar seu 
assistente e salvar o mundo de ser dominado por Dora.""")
    menuInicial()
    

# FUNÇÃO COM PERFIL DOS PERSONAGENS
def verPerfil():
    titulos(' ')
    titulos('KEVIN')
    print(textoKevin)
    titulos('GIN')
    print(textoGin)
    titulos('DORA')
    print(textoDora)
    titulos(' ')
    titulos('MENU')
    subMenu()


#FUNÇAO DO MENU INICIAL
def menuInicial():
    titulos(titulo)
    for i, opcao in enumerate(opcoesMenuInicial):
        print(i+1, '- ', opcao)
    linha()
    escolha = int(input('INFORME A OPÇÃO DESEJADA: '))
    linha()
    if escolha == 1:
        subMenu()
    elif escolha == 2:
        creditos()
    elif escolha == 3:
        exit()
    else:
        print(cabecalho('Digite uma opção válida'))
        menuInicial()


#FUNÇAO SUBMENU
def subMenu():
    global personagemEscolhido
    for i, nome in enumerate(acoes):
        print(i + 1, " - ", nome)
    linha()
    escolhaPersonagens = int(input('INFORME A OPÇÃO DESEJADA: '))
    linha()
    if escolhaPersonagens == 1:
        verPerfil()
    elif escolhaPersonagens == 2:
        if personagemEscolhido == ' ':      # ESSE IF DEVE-SE MANTER POIS AO REINICIAR NÃO REPETE DEFINICAO DE PERSONAGEM
            definePersonagem()
    elif escolhaPersonagens == 3:
        menuInicial()
    else:
        titulos('Digite uma opção válida')
        subMenu()


#FUNÇAO PARA DEFINIR O PERSONAGEM ESCOLHIDO
def definePersonagem():
    titulos('ESCOLHA DO PERSONAGEM')
    global personagemEscolhido
    for i, nome in enumerate(personagens):
        print(i + 1, " - ", nome)

    linha()
    personagemEscolhido = int(input('INFORME A OPÇÃO DESEJADA: '))
    linha()
    if personagemEscolhido == 1:
        personagemEscolhido = 'GIN'
        
    elif personagemEscolhido == 2:
        personagemEscolhido = 'KEVIN'
        
    elif personagemEscolhido == 3:
        personagemEscolhido = 'DORA'

    elif personagemEscolhido == 4:
        subMenu()
       
    else:
        titulos('Digite uma opçao válida!')
        definePersonagem()

    titulos(f'Você escolheu o personagem {personagemEscolhido}')
    return personagemEscolhido

 
# FUNCÃO PARA DEFINIR ESCOLHA DO USUÁRIO
def escolhaUsuario():
    global escolha
    linha()
    escolha = int(input('INFORME A OPÇÃO DESEJADA: '))
    linha()

    while escolha < 99:
        if escolha == 1:
            titulos(f'DECISÃO {escolha}')
            return escolha
        elif escolha == 2:
            titulos(f'DECISÃO {escolha}')
            return escolha
        else:
            titulos('Digite uma opçao válida!')
            escolhaUsuario()
        return escolha


# FUNCÃO PARA INFORMAR A FASE - AINDA A SER IMPLEMENTADA - ESTÁ DANDO ERRO AO REINICIAR JOGO
# def informaFaseePersonagem():
#     global fase
#     if personagemEscolhido != ' ':
#         fase += 1
#     titulos(f'VOCÊ ESTÁ NA FASE {fase} DA PERSONAGEM {personagemEscolhido}')
#     return fase
        

menuInicial()