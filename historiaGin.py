from projetofinalmodulo1 import *



def fase1Gin():
    global escolha
    global fase
    # informaFaseePersonagem()

    # INTRODUÇAO DA FASE 1
    cabecalho("""Gin é o responsável de manutenção de Orion, apesar dele odiar Orion esta é a 
unica alternativa de emprego para ele, já que a economia intermundial gira em 
torno desse metaverso.
    
Ele não gosta muito de festas e foi escalado para o plantão de Reveillon do ano 
de 2999, e durante a contagem regressiva viu uma anomalia, um pico de dados no 
sistema...""")
    
    # LISTAS COM AS OPÇOES DA FASE 1
    fase1opcao1Gin = ['1 - VERIFICAR ORIGEM DO PICO DE DADOS', 
    '2 - LEVANTAR E BUSCAR UM CAFÉ',
    '99 - SAIR']
    fase1opcao2Gin = ['1 - A ORIGEM DO PICO VEM DE UM LUGAR CONHECIDO', 
    '2 - A ORIGEM DO PICO DE DADOS VEM DE UM LUGAR DESCONHECIDO',
    '99 - SAIR']
    fase1opcao3Gin = ['1 - IGNORAR ACESSOS',
    '2 - TENTAR REVERTER A SITUAÇAO',
    '99 - SAIR']
    fase1opcao4Gin = ['1 - VERIFICAR POR QUE KEVIN ESTÁ ACESSANDO DADOS DE ORION', 
    '2 - VERIFICAR POR QUE O AR CONDICIONADO PAROU DE FUNCIONAR',
    '99 - SAIR']
    
    # INICIO DAS ESCOLHAS DA FASE 1
    for opcao in fase1opcao1Gin:
            print(opcao)
    escolha = escolhaUsuario()
    if escolha == 1:                                         # ESCOLHA 1 / 
        enrredo('RASTREANDO PICO DE DADOS...') 
        if escolha == 1:
            for opcao in fase1opcao2Gin:
                    print(opcao)
        escolha = escolhaUsuario()
       
        if escolha == 1:                                     # ESCOLHA 1 * 1 /
            enrredo('O PICO VEM DOS DISPOSITIVOS DO ...')
            sleep(1)
            enrredo('KEVIN') 
            sleep(0.5)
            enrredo('KEVIN É O ASSISTENTE DE GIN, QUE ESTÁ DE FOLGA, CURTINDO O REVEILLON')
            for opcao in fase1opcao4Gin:
                    print(opcao)
            escolha = escolhaUsuario()
            
            if escolha == 1:                                   # ESCOLHA 1 * 1 * 1 /
                enrredo('Vou fazer uma chamada para esse menino imediatamente!') 
                passouDeFase('VOCÊ PASSOU DE FASE')
                fase +=1
                # informaFaseePersonagem()
                fase2Gin()
           
            elif escolha == 2:                                 # ESCOLHA 1 * 1 * 2 /
                enrredo('A temperatura ficou agradável, mas o clima esquentou com a invasão de Orion')
                perdeuPlayboy('VOCÊ PERDEU')                

        elif escolha == 2:                                 # ESCOLHA 1 * 2 / 
                enrredo('GIN NÃO INSISTIU E PERMITIU UMA GRANDE FALHA DE SEGURANÇA EM ORION')
                perdeuPlayboy('Persista')                
        
    elif escolha == 2:                                       # ESCOLHA 2 /
        enrredo('VOCÊ LEVANTOU E ORION FOI INVADIDA')
        for opcao in fase1opcao3Gin:
                print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                    # ESCOLHA 2 * 1 / 
            enrredo('Gin foi demitido por justa causa')
            perdeuPlayboy('Pequenos descuidos causam grandes impactos')  

        elif escolha == 2:                                    # ESCOLHA 2 * 2 / 
            enrredo('PARA ALGUMAS COISAS EXISTEM SOMENTE UMA OPORTUNIDADE') 
            perdeuPlayboy('AGARRE-A ANTES QUE SEJA TARDE')            

   
def fase2Gin():
    global escolha
    global fase

    # INTRODUÇAO DA FASE 2
    cabecalho("""Gin enfurecido faz uma chamada holográfica para Kevin e descobre que ele está 
em uma festa num lugar muito suspeito, e para a sua surpresa ele descobre que 
não é Kevin que está acessando os dados""")

 # LISTAS COM AS OPÇOES DA FASE 2
    fase2opcao1Gin = ['1 - RASTREAR ORIGEM DOS DADOS', 
    '2 - RASTREAR O COELHO BRANCO',
    '99 - SAIR']
    fase2opcao2Gin = ['1 - BUSCAR NOVAMENTE', 
    '2 - PROCRASTINAR E FAZER ISSO AMANHÃ',
    '99 - SAIR']
    fase2opcao3Gin = ['1 - TOMAR A PILULA AZUL',
    '2 - TOMAR A PILULA VERMELHA',
    '99 - SAIR']
    fase2opcao4Gin = ['1 - INTERCEPTAR PACOTES', 
    '2 - INTERCEPTAR ENCOMENDAS',
    '99 - SAIR']
    
    # INICIO DAS ESCOLHAS DA FASE 2
    for opcao in fase2opcao1Gin:
            print(opcao)
    escolha = escolhaUsuario()
    if escolha == 1:                                         # ESCOLHA 1 / 
        enrredo('RASTREANDO DADOS...')
        sleep(0.3)
        enrredo('RASTREANDO DADOS...')
        sleep(0.3)
        enrredo('RASTREANDO DADOS...')
        sleep(0.3)
        enrredo('ORIGEM NÃO ENCONTRADA')

        if escolha == 1:
            for opcao in fase2opcao2Gin:
                    print(opcao)
        escolha = escolhaUsuario()
        if escolha == 1:                                     # ESCOLHA 1 * 1 /
            enrredo('Nem sempre você acerta de primeira, insista!') 
            enrredo('Os dados estão vindo de uma VPN, mas ainda não é possível identificar quem está acessando.')
            for opcao in fase2opcao4Gin:
                    print(opcao)
            escolha = escolhaUsuario()
            
            if escolha == 1:                                   # ESCOLHA 1 * 1 * 1 /
                enrredo('DEU CERTO! Ao comparar as informações de outros trafegos, achei uma coincidência.') 
                passouDeFase('VOCÊ PASSOU DE FASE!')
                fase +=1
                fase3Gin()
            
            elif escolha == 2:                                 # ESCOLHA 1 * 1 * 2 /
                enrredo('ISSO É CRIME')
                perdeuPlayboy('DA CADEIA VOCÊ NÃO PODE CONTINUAR')              
                
        elif escolha == 2:                                 # ESCOLHA 1 * 2 / 
                enrredo('PROCRASTINAÇÃO PODE LEVAR A DEPRESSÃO, ANSIEDADE, INSATISFAÇÃO E ESTRESSE CRÔNICO')
                perdeuPlayboy('PROCURE AJUDA PSICOLÓGICA')                     
        
    elif escolha == 2:                                       # ESCOLHA 2 /
        enrredo('enreddo9')
        for opcao in fase2opcao3Gin:
                print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                    # ESCOLHA 2 * 1 / 
            enrredo('VOLTANDO PARA A MATRIX')
            perdeuPlayboy('ACORDANDO EM SEU APARTAMENTO ATRASADO PARA O TRABALHO QUE VOCÊ DETESTA...')          
        
        elif escolha == 2:                                    # ESCOLHA 2 * 2 / 
            enrredo('SAINDO DA MATRIX') 
            perdeuPlayboy('BEM VINDO AO MUNDO REAL')            


def fase3Gin():
    global escolha
    global fase
    # informaFaseePersonagem()

    # INTRODUÇAO DA FASE 3
    cabecalho('Gin conseguiu chegar até a pessoa que está usando os dados de Kevin.')

 # LISTAS COM AS OPÇOES DA FASE 3
    fase3opcao1Gin = ['1 - REVELAR IDENTIDADE', 
    '2 - REVELAR SEGREDO',
    '99 - SAIR']
    fase3opcao2Gin = ['1 - INVADIR REDE DE DORA', 
    '2 - DESLIGAR A ENERGIA DE ORION PARA IMPEDIR O ACESSO',
    '99 - SAIR']
    fase3opcao3Gin = ['1 - ABRIR CARTA',
    '2 - QUEIMAR CARTA E GUARDAR O SEGREDO PARA SEMPRE',
    '99 - SAIR']
    fase3opcao4Gin = ['1 - INTERROMPER O ACESSO DE DORA', 
    '2 - ESQUECER A SENHA MASTER',
    '99 - SAIR']
    
    # INICIO DAS ESCOLHAS DA FASE 3
    for opcao in fase3opcao1Gin:
            print(opcao)
    escolha = escolhaUsuario()
    if escolha == 1:                                         # ESCOLHA 1 / 
        enrredo('A pessoa que está acessando os dados de Kevin é Dora, já conhecida por aplicar golpes virtuais em Orion.') 
        if escolha == 1:
            for opcao in fase3opcao2Gin:
                    print(opcao)
        escolha = escolhaUsuario()
        if escolha == 1:                                     # ESCOLHA 1 * 1 /
            enrredo('Gin com as sua habilidade conseguiu acessar a rede de Dora') 
            for opcao in fase3opcao4Gin:
                    print(opcao)
            escolha = escolhaUsuario()
            
            if escolha == 1:                                   # ESCOLHA 1 * 1 * 1 /
                enrredo('Gin salvou Kevin e todo metaverso dos golpes de Dora') 
                passouDeFase('FIM DE JOGO')                
            
            elif escolha == 2:                                 # ESCOLHA 1 * 1 * 2 /
                enrredo('DORA CONSEGUIU ACESSAR ORION E ROUBOU OS NFTS MAIS VALIOSOS DO MUNDO')
                perdeuPlayboy('DORA VENCEU')                

        elif escolha == 2:                                 # ESCOLHA 1 * 2 / 
                enrredo('DESLIGAR A ENERGIA DE ORION CAUSOU GRANDE DESCONTENTAMENTO DOS USUÁRIOS LEVANDO A DEMISSÃO DE GIN')
                perdeuPlayboy('VOCÊ PERDEU')                
        
    elif escolha == 2:                                       # ESCOLHA 2 /
        enrredo('O SEGREDO ESTÁ REVELADO NUMA CARTA')
        for opcao in fase3opcao3Gin:
                print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                    # ESCOLHA 2 * 1 / 
            enrredo('O QUE DISSE QUE DISSESTE QUE DIZIA A CARTA?')
            perdeuPlayboy('ÓH, É ALGO TERRÍVEL...')            
        
        elif escolha == 2:                                    # ESCOLHA 2 * 2 / 
            enrredo('O SEGREDO ERA ALGO TERRÍVEL PARA SER REVELADO') 
            perdeuPlayboy('VOCÊ PERDEU')
            