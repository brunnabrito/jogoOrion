from projetofinalmodulo1 import *


def fase1Kevin():
    global escolha
    global fase
    # informaFaseePersonagem()
    # INTRODUÇAO DA FASE 1
    cabecalho("""KEVIN É UM JOVEM GAROTO QUE TRABALHA COMO ASSISTENTE DE MANUTENÇÃO EM ORION. 
COMO A ECONOMIA GIRA DENTRO DO METAVERSO, APENAS POUCOS TRABALHOS SOBRARAM FORA 
DA REDE. APESAR DE VIVER FORA, ELE GOSTA DE SE DIVERTIR LÁ DENTRO. HOJE É UM DIA 
ESPECIAL, É A VIRADA DO ANO DE 2999 PARA O ANO 3000 E KEVIN CONSEGUIU UMA FOLGA.""")
    
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
            enrredo("""FALTA POUCO PARA A CONTAGEM REGRESSIVA E KEVIN QUER IR A UM LUGAR UM POUCO MAIS 
MOVIMENTADO PARA QUEM SABE CONHECER ALGUEM""") 
            for opcao in fase1opcao4Kevin:
                    print(opcao)
            escolha = escolhaUsuario()
            if escolha == 1:                                   # ESCOLHA 1 * 1 * 1 /
                enrredo('KEVIN FOI A UMA FESTA MAIS AGITADA, PORÉM POUCO SEGURA')
                enrredo('PREPARANDO PARA A CONTAGEM REGRESSIVA')
                enrredo('QUE ESTRANHO, GIN, MEU CHEFE ESTÁ ME LIGANDO UMA HORA DESSAS')
                passouDeFase('VOCÊ PASSOU DE FASE')
                fase +=1
                # informaFaseePersonagem()
                fase2Kevin()
            
            elif escolha == 2:                                 # ESCOLHA 1 * 1 * 2 /
                enrredo("""KEVIN VOLTOU AO MUNDO REAL, PORÉM TODOS ESTAVA CONECTADOS A ORION""")
                titulos("""VONTANDO A ORION""")                

        elif escolha == 2:                                 # ESCOLHA 1 * 2 / 
                enrredo("""KEVIN PASSOU O REVEILLON MEDITANDO""")
                titulos("""OM""")                
                
        
    elif escolha == 2:                                       # ESCOLHA 2 /
        enrredo("""VER OPÇÕES DE LUGARES """)
        for opcao in fase1opcao3Kevin:
                print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                    # ESCOLHA 2 * 1 / 
            enrredo("""VOCÊ SAIU E ORION FOI DOMINADA POR UM MALWARE""")
            titulos("""VOCÊ PERDEU""")       
            
        elif escolha == 2:                                    # ESCOLHA 2 * 2 / 
            enrredo("""VOCÊ SALVOU SUAS SENHAS PARA VOLTAR DEPOIS 
E SUAS CREDENCIAIS FORAM ROUBADAS""") 
            titulos("""VOCÊ PERDEU""")            
            
    
def fase2Kevin():
    global escolha
    global fase
    # INTRODUÇAO DA FASE 2
    cabecalho("""KEVIN ESTÁ CURTINDO SEU REVEILLON E INESPERADAMENTE RECEBE UMA LIGAÇÃO DO SEU 
CHEFE ÀS VESPERAS DA CONTAGEM REGRESSIVA""")

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
        enrredo("""KEVIN: FALA CHEFE? LIGOU ADIANTADO! AINDA FALTA UM POUCO PARA A VIRADA...""")
        sleep(0.4)
        enrredo("""GIN: NÃO ME VENHA COM CONVERSA, ME DIGA AGORA MESMO 
POR QUE ESTÁ ACESSANDO OS DADOS DE ÓRION""")
        sleep(0.4)
        enrredo("""KEVIN: QUEM, EU? NESTE MOMENTO EU NÃO QUERO NEM SABER DE ORION, 
MINHA FESTA ESTÁ MUITO BOA!""")
        sleep(0.4)
        enrredo("""GIN: SE NÃO É VOCÊ QUEM ESTÁ CONECTANDO DOS SEUS DISPOSITIVOS?""") 
        sleep(0.4)
        enrredo("""KEVIN: QUE CONEXÃO, DE QUE DISPOSITIVOS?""")
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
            enrredo("""AGORA É TARDE, OS DADOS DE KEVIN JÁ HAVIAM SIDO ENCRIPTADOS 
E ELE PERDEU ACESSO AOS SEUS DISPOSITIVOS.""") 
            for opcao in fase2opcao4Kevin:
                    print(opcao)
            escolha = escolhaUsuario()
            
            if escolha == 1:                                   # ESCOLHA 1 * 1 * 1 /
                enrredo('KEVIN: GIN EU FUI RACKEADO, VOCÊ PRECISA ME AJUDAR!')
                sleep(0.4)
                enrredo('GIN: SIGA MINHAS INSTRUÇÕES!') 
                sleep(0.4)
                passouDeFase('VOCÊ PASSOU DE FASE')
                fase +=1
                # informaFaseePersonagem()
                fase3Kevin()

            elif escolha == 2:                                 # ESCOLHA 1 * 1 * 2 /
                enrredo("""MESMO COM NOVOS DISPOSITIVOS VOCÊ NÃO TEM 
ACESSO POIS AS CREDENCIAIS FORAM ROUBADAS""")
                titulos("""VOCÊ PERDEU""")                
                

        elif escolha == 2:                                 # ESCOLHA 1 * 2 / 
                enrredo("""SEUS DISPOSITIVOS ESTÃO BLOQUEADOS""")
                titulos("""VOCÊ PERDEU""")                
                
        
    elif escolha == 2:                                       # ESCOLHA 2 /
        enrredo("""DELISGANDO O CELULAR""")
        for opcao in fase2opcao3Kevin:
                print(opcao)
        escolha = escolhaUsuario()

        if escolha == 1:                                    # ESCOLHA 2 * 1 / 
            enrredo("""SEM QUERER VOCÊ PAROU O ACESSO DE DORA AO SEU USUÁRIO, MAS FOI SORTE""")
            titulos("""SAINDO PARA CURTIR A FESTA""")            
            

        elif escolha == 2:                                    # ESCOLHA 2 * 2 / 
            enrredo("""TARDE DE MAIS, ENQUANTO VOCÊ DIGITAVA SEUS DISPOSITIVOS PARARAM DE FUNCIONAR""") 
            titulos("""VOCÊ PERDEU""")            
            


def fase3Kevin():
    global escolha
    global fase
    # INTRODUÇAO DA FASE 3
    cabecalho("""ATRAVÉS DOS ACESSOS DE KEVIN, DORA CONSEGUIU ACESSAR ORION E 
DISPARAR MENSAGENS DE PHISHING PARA INFECTAR TODOS OS SEUS USUÁRIOS, 
PORÉM GIN JÁ HAVIA RASTERADO OS DADOS DE DADOS ATRAVÉS DA CONEXÃO DE 
KEVIN E INTERCEPTADO OS PACOTES.
GIN IRÁ DAR IMPORTANTES INSTRUÇÕES À KEVIN""")

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
        enrredo("""GIN: SAIA DESTE LUGAR IMEDIATAMENTE, 
ELE ESTÁ CAUSANDO UM ATAQUE DDKS NOS SEU DMS""")
        sleep(0.4)
        enrredo("""KEVIN: MAS GIN, A ENTRADA NESSA FESTA ME CUSTOU ¢187 METACOINS""")
        sleep(0.4)
        enrredo("""GIN: SAIA IMEDIATAMENTE""")
        sleep(0.4)
        enrredo("""KEVIN: TÁ, SAINDO.... E AGORA?""")
        sleep(0.4)
        enrredo("""GIN: VOCÊ DEVERÁ REINICIAR SEUS DISPOSITIVOS EM MODO DE SEGURANÇA""")
        sleep(0.4)
        enrredo("""KEVIN: COMO FAÇO ISSO?""")
        sleep(0.4)
        enrredo("""GIN: REINICIE O DISPOSITIVO E COM A TECLA ALPHA APERTADA
SOLICITE AO MAIN TERMINAL O SAFEBOOT""")

        if escolha == 1:
            for opcao in fase3opcao2Kevin:
                    print(opcao)
        escolha = escolhaUsuario()

        if escolha == 1:                                     # ESCOLHA 1 * 1 /
            enrredo("""GIN: AGORA EU VOU RESETAR OS SEUS DISPOSITIVOS PARA 
REINICIAR AS CREDENCIAIS E IMPEDIR QUE O ACESSO CONTINUE""")
            enrredo('KEVIN: MAS ASSIM VOU PERDER AS FOTOS DO MEU REVEILLON...')
            enrredo('GIN: OU AS SUAS MALDITAS FOTOS OU TODA ORION ESTARÁ DESTRUÍDA!!!')
            enrredo('KEVIN: TÁ BEM... ')

            for opcao in fase3opcao4Kevin:
                    print(opcao)
            escolha = escolhaUsuario()

            if escolha == 1:                                   # ESCOLHA 1 * 1 * 1 /
                enrredo("""AO SEGUIR AS INSTRUÇÕES, KEVIN E GIN CONSEGUIRAM IMPEDIR O ATAQUE""") 
                passouDeFase("""ORION FOI SALVA DE MAIS UM ATAQUE DE DORA""")


            elif escolha == 2:                                 # ESCOLHA 1 * 1 * 2 /
                enrredo("""VOCÊ DESLIGOU E GIN PERDEU A INTERCEPTAÇÃO DOS PACOTES, DORA ACESSOU ORION""")
                titulos("""VOCÊ PERDEU""")                
                

        elif escolha == 2:                                 # ESCOLHA 1 * 2 / 
                enrredo("""OS ATAQUES DDKS NOS SEU DMS SE INTENSIFICARAM E FOI IMPOSSÍVEL REVERTER O ACESSO""")
                titulos("""VOCÊ PERDEU""")                
                
        
    elif escolha == 2:                                       # ESCOLHA 2 /
        enrredo("""VOU RESOLVER SOZINHO""")
        for opcao in fase3opcao3Kevin:
                print(opcao)
        escolha = escolhaUsuario()

        if escolha == 1:                                    # ESCOLHA 2 * 1 / 
            enrredo("""A SOLUÇÃO AUTOMÁTICA DEMOROU 18 MINUTOS PARA FAZER O DIAGNÓSTICO,
NESTE TEMPO DORA JÁ TINHA RACKEADO TODOS DE ORION""")
            titulos("""VOCÊ PERDEU""")            
            

        elif escolha == 2:                                    # ESCOLHA 2 * 2 / 
            enrredo("""VOCÊ NÃO CONSEGUIU CONTATO COM ONE""") 
            titulos("""VOCÊ PERDEU""")            
            

