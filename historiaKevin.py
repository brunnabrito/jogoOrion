from projetofinalmodulo1 import *


def fase1Kevin():
    global escolha
    global fase
    informaFaseePersonagem()
    # INTRODUÇAO DA FASE 1
    cabecalho("""Kevin é um jovem garoto que trabalha como assistente de manutenção em Orion.
Como a economia gira dentro do metaverso, apenas poucos trabalhos sobraram fora
da rede. Apesar de viver fora, ele gosta de se divertir lá dentro. Hoje é um dia
especial, é a virada do ano de 2999 para o ano 3000 e Kevin conseguiu uma folga.""")
    
    # LISTAS COM AS OPÇOES DA FASE 1
    fase1opcao1Kevin = ['1 - CONECTAR EM ORION E CURTIR AS FESTAS DE REVEILLON', 
    '2 - PASSAR O REVEILLON SOZINHO',
    '99 - SAIR']
    fase1opcao2Kevin = ['1 - COMEMORAR REVEILLON NA FESTA MAIS BADALADA', 
    '2 - COMEMORAR REVEILLON NUM RETIRO',
    '99 - SAIR']
    fase1opcao3Kevin = ['1 - PASSAR O REVEILLON NO METAVERSO METACORTEX',
    '2 - PASSAR O REVEILLON NO MUNDO REAL',
    '99 - SAIR']
    fase1opcao4Kevin = ['1 - IR PARA A FESTA X', 
    '2 - VOLTAR AO MUNDO REAL PARA CONHECER GENTE REAL',
    '99 - SAIR']
    
    # INICIO DAS ESCOLHAS DA FASE 1
    for opcao in fase1opcao1Kevin:
            print(opcao)
    escolha = escolhaUsuario()
    if escolha == 1:                                         # ESCOLHA 1 / 
        enrredo('ACESSANDO ORION')
        sleep(0.1)
        enrredo('DIGITE SEU LOGIN: KEVIN_BACON')
        sleep(0.1)
        enrredo('SENHA: ● ● ● ● ● ● ● ●')
        sleep(0.1)
        enrredo('DESEJA SALVAR SUAS CREDENCIAIS?')
        sleep(0.1)
        enrredo('SIM')
        sleep(0.1)
        enrredo('CREDENCIAIS SALVAS')
        enrredo('BEM VINDO A ORION')
        
        if escolha == 1:
            for opcao in fase1opcao2Kevin:
                    print(opcao)
        escolha = escolhaUsuario()
        if escolha == 1:                                     # ESCOLHA 1 * 1 /
            enrredo("""Falta pouco para a contagem regressiva e Kevin quer ir a um lugar um pouco mais
movimentado para quem sabe conhecer alguém""") 
            for opcao in fase1opcao4Kevin:
                    print(opcao)
            escolha = escolhaUsuario()
            if escolha == 1:                                   # ESCOLHA 1 * 1 * 1 /
                enrredo('Kevin foi a uma festa mais agitada, porém pouco segura')
                enrredo('Preparando para a contagem regressiva')
                enrredo('Que estranho, Gin, meu chefe está me ligando uma hora dessas')
                passouDeFase('VOCÊ PASSOU DE FASE')
                fase +=1
                informaFaseePersonagem()
                fase2Kevin()
            
            elif escolha == 2:                                 # ESCOLHA 1 * 1 * 2 /
                enrredo("""Kevin voltou ao mundo real, porém todos estava conectados a Orion""")
                titulos("""VONTANDO A ORION""")                

        elif escolha == 2:                                 # ESCOLHA 1 * 2 / 
                enrredo("""Kevin passou o reveillon meditando""")
                titulos("""OM""")                
                
        
    elif escolha == 2:                                       # ESCOLHA 2 /
        enrredo("""Ver opções de lugares""")
        for opcao in fase1opcao3Kevin:
                print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                    # ESCOLHA 2 * 1 / 
            enrredo("""Você saiu e Orion foi dominada por um malware""")
            titulos("""VOCÊ PERDEU""")       
            
        elif escolha == 2:                                    # ESCOLHA 2 * 2 / 
            enrredo("""Você salvou suas senhas para voltar depois
e suas credenciais foram roubadas""") 
            titulos("""VOCÊ PERDEU""")            
            
    
def fase2Kevin():
    global escolha
    global fase
    # INTRODUÇAO DA FASE 2
    cabecalho("""Kevin está curtindo seu reveillon e inesperadamente recebe uma ligação do seu
chefe às vésperas da contagem regressiva""")

 # LISTAS COM AS OPÇOES DA FASE 2
    fase2opcao1Kevin = ['1 - ATENDER AO TELEFONE', 
    '2 - REJEITAR LIGAÇÃO',
    '99 - SAIR']
    fase2opcao2Kevin = ['1 - VERIFICAR DISPOSITIVOS INTEGRADOS', 
    '2 - VERIFICAR AS REDES SOCIAIS',
    '99 - SAIR']
    fase2opcao3Kevin = ['1 - COLOCAR DISPOSITIVOS EM MODO AVIÃO PARA NÃO RECEBER MAIS LIGAÇÕES',
    '2 - ENVIAR UMA MENSAGEM DE TEXTO PERGUNTANDO DO QUE SE TRATA',
    '99 - SAIR']
    fase2opcao4Kevin = ['1 - PEDIR SOCORRO AO GIN', 
    '2 - JOGAR DISPOSITIVO FORA E COMPRAR OUTRO',
    '99 - SAIR']
    
    # INICIO DAS ESCOLHAS DA FASE 2
    for opcao in fase2opcao1Kevin:
            print(opcao)
    escolha = escolhaUsuario()
    if escolha == 1:                                         # ESCOLHA 1 / 
        enrredo("""Kevin: fala chefe? ligou adiantado! ainda falta um pouco para a virada...""")
        sleep(0.4)
        enrredo("""Gin: não me venha com conversa, me diga agora mesmo
por que está acessando os dados de Orion""")
        sleep(0.4)
        enrredo("""Kevin: quem, eu? neste momento eu não quero nem saber de Orion,
minha festa está muito boa!""")
        sleep(0.4)
        enrredo("""Gin: se não é você quem está conectando dos seus dispositivos?""")
        sleep(0.4)
        enrredo("""Kevin: que conexão, de que dispositivos?""")
        print('\033[34m' + '')
        for i in range(5, 0, -1):
            contagem = str(i)
            print(contagem.center(100)) 
            sleep(0.7)
        enrredo('FELIZ ANO NOVO!! ')
        if escolha == 1:
            for opcao in fase2opcao2Kevin:
                    print(opcao)
        escolha = escolhaUsuario()
        if escolha == 1:                                     # ESCOLHA 1 * 1 /
            enrredo("""Agora é tarde, os dados de Kevin já haviam sido encriptados
e ele perdeu acesso aos seus dispositivos.
""") 
            for opcao in fase2opcao4Kevin:
                    print(opcao)
            escolha = escolhaUsuario()
            
            if escolha == 1:                                   # ESCOLHA 1 * 1 * 1 /
                enrredo('Kevin: Gin eu fui rackeado, você precisa me ajudar!')
                sleep(0.4)
                enrredo('Gin: siga minhas instruções!')
                fase +=1
                informaFaseePersonagem()
                fase3Kevin()

            elif escolha == 2:                                 # ESCOLHA 1 * 1 * 2 /
                enrredo("""Mesmo com novos dispositivos você não tem
acesso pois as credenciais foram roubadas""")
                titulos("""VOCÊ PERDEU""")                
                

        elif escolha == 2:                                 # ESCOLHA 1 * 2 / 
                enrredo("""Seus dispositivos estão bloqueados""")
                titulos("""VOCÊ PERDEU""")                
                
        
    elif escolha == 2:                                       # ESCOLHA 2 /
        enrredo("""DELISGANDO O CELULAR""")
        for opcao in fase2opcao3Kevin:
                print(opcao)
        escolha = escolhaUsuario()

        if escolha == 1:                                    # ESCOLHA 2 * 1 / 
            enrredo("""Sem querer você parou o acesso de Dora ao seu usuário, mas foi sorte""")
            titulos("""SAINDO PARA CURTIR A FESTA""")            
            

        elif escolha == 2:                                    # ESCOLHA 2 * 2 / 
            enrredo("""Tarde de mais, enquanto você digitava seus dispositivos 
pararam de funcionar""") 
            titulos("""VOCÊ PERDEU""")            
            


def fase3Kevin():
    global escolha
    global fase
    # INTRODUÇAO DA FASE 3
    cabecalho("""Através dos acessos de Kevin, Dora conseguiu acessar Orion e
disparar mensagens de phishing para infectar todos os seus usuários,
porém Gin já havia rastreado os dados de dados através da conexão de
Kevin e interceptado os pacotes.
Gin irá dar importantes instruções à Kevin""")

 # LISTAS COM AS OPÇOES DA FASE 3
    fase3opcao1Kevin = ['1 - SEGUIR INSTRUÇÕES', 
    '2 - RESOLVER SOZINHO',
    '99 - SAIR']
    fase3opcao2Kevin = ['1 - SAIR DO LUGAR IMEDIATAMENTE E ABRIR MODO DE SEGURANÇA', 
    '2 - FALAR QUE SAIU MAS FICAR LÁ',
    '99 - SAIR']
    fase3opcao3Kevin = ['1 - RODAR SOLUÇÃO AUTOMÁTICA DO DISPOSITIVO',
    '2 - LIGAR PARA O RACKER ONE',
    '99 - SAIR']
    fase3opcao4Kevin = ['1 - REINICIAR CREDENCIAIS', 
    '2 - DESLIGAR TUDO ATÉ QUE SE RESOLVA SOZINHO',
    '99 - SAIR']
    
    # INICIO DAS ESCOLHAS DA FASE 3
    for opcao in fase3opcao1Kevin:
            print(opcao)
    escolha = escolhaUsuario()
    if escolha == 1:                                         # ESCOLHA 1 / 
        enrredo("""Gin: saia deste lugar imediatamente,
ele está causando um ataque DDKS no seu DMS""")
        sleep(0.4)
        enrredo("""Kevin: mas Gin, a entrada nessa festa me custou ¢187 metacoins""")
        sleep(0.4)
        enrredo("""GIN: SAIA IMEDIATAMENTE""")
        sleep(0.4)
        enrredo("""Kevin: tá, saindo.... e agora?""")
        sleep(0.4)
        enrredo("""Gin: você deverá reiniciar seus dispositivos em modo de segurança""")
        sleep(0.4)
        enrredo("""Kevin: como faço isso""")
        sleep(0.4)
        enrredo("""Gin: reinicie o dispositivo e com a tecla alpha apertada
solicite ao main terminal o safeboot""")

        if escolha == 1:
            for opcao in fase3opcao2Kevin:
                    print(opcao)
        escolha = escolhaUsuario()

        if escolha == 1:                                     # ESCOLHA 1 * 1 /
            enrredo("""Gin: agora eu vou resetar os seus dispositivos para
reiniciar as credenciais e impedir que o acesso continue""")
            enrredo('Kevin: mas assim vou perder as fotos do meu reveillon...')
            enrredo('Gin: ou as suas malditas fotos ou toda Orion estará destruída!!!')
            enrredo('Kevin: tá bem... ')

            for opcao in fase3opcao4Kevin:
                    print(opcao)
            escolha = escolhaUsuario()

            if escolha == 1:                                   # ESCOLHA 1 * 1 * 1 /
                enrredo("""Ao seguir as instruções, Kevin e Gin conseguiram impedir o ataque""") 
                passouDeFase("""ORION FOI SALVA DE MAIS UM ATAQUE DE DORA""")


            elif escolha == 2:                                 # ESCOLHA 1 * 1 * 2 /
                enrredo("""Você desligou e Gin perdeu a interceptação dos pacotes, Dora acessou Orion""")
                titulos("""VOCÊ PERDEU""")                
                

        elif escolha == 2:                                 # ESCOLHA 1 * 2 / 
                enrredo("""Os ataques ddks nos seu dms se intensificaram e foi impossível reverter o acesso""")
                titulos("""VOCÊ PERDEU""")                
                
        
    elif escolha == 2:                                       # ESCOLHA 2 /
        enrredo("""Vou resolver sozinho""")
        for opcao in fase3opcao3Kevin:
                print(opcao)
        escolha = escolhaUsuario()

        if escolha == 1:                                    # ESCOLHA 2 * 1 / 
            enrredo("""A solução automática demorou 18 minutos para fazer o diagnóstico,
neste tempo Dora já tinha rackeado todos de Orion""")
            titulos("""VOCÊ PERDEU""")            
            

        elif escolha == 2:                                    # ESCOLHA 2 * 2 / 
            enrredo("""Você não conseguiu contato com ONE""") 
            titulos("""VOCÊ PERDEU""")            
            

