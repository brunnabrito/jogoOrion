
from projetofinalmodulo1 import *


# informaFaseePersonagem()

def fase1Dora():
    global escolha
    global fase
    # INTRODUÇAO DA FASE
    enrredo("""DORA É UMA PESSOA MUITO CURIOSA, E DESCOBRIU SOBRE UMA LENDA URBANA, A DO BUG DO 
MILENIO DE 1999. ISSO FEZ DORA PENSAR, SERÁ MESMO UMA LENDA URBANA? O QUE HÁ DE 
VERDADE SOBRE ISSO?""") 
    
    # LISTAS COM AS OPÇOES
    fase1opcao1Dora = ['1 - CURIOSO... PESQUISAR MAIS...', 
    '2 - É SÓ UMA LENDA URBANA, DEIXA PARA LÁ...',
    '99 - SAIR']
    fase1opcao2Dora = ['1 - INVESTIGAR FALHA DE SEGURANÇA', 
    '2 - INVESTIGAR SOBRE O SURGIMENTO DE GOLFINHOS ALADOS',
    '99 - SAIR']
    fase1opcao3Dora = ['1 - IR ATRÁS DA PESSOA QUE COLOCOU A PLACA',
    '2 - ESTOU COM FOME, VOU COMER',
    '99 - SAIR']
    fase2opcao4Dora = ['1 - USAR FALHA DE SEGURANÇA PARA CONSEGUIR ACESSAR ORION', 
    '2 - USAR FALHA DE SEGURANÇA PARA PESQUISAR SOBRE OS GOLFINHOS',
    '99 - SAIR']
    
    # INICIO DAS ESCOLHAS 
    for opcao in fase1opcao1Dora:
            print(opcao)
    escolha = escolhaUsuario()
    if escolha == 1:                                         # ESCOLHA 1 /
        enrredo('ACESSANDO AQUIVOS... O ERRO CONHECIDO COMO BUG DO MILÊNIO FOI CAUSADO PELA CONFIGURAÇÃO DE DATAS EM SISTEMAS DE COMPUTAÇÃO. COM A CHEGADA DO ANO 2000 OS COMPUTADORES INTERPRETARIAM O ANO 00 COMO 1900, GERANDO EFEITOS EM CASCATA NA LINHA TEMPORAL DOS PROGRAMAS QUE REGREDIRIAM 100 ANOS E UMA ENORME FALHA DE CYBERSEGURANÇA.') 
        if escolha == 1:
            for opcao in fase1opcao2Dora:
                    print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                     # ESCOLHA 1 * 1 /
            enrredo('PARA EVITAR A REGRESSÃO DE 100 ANOS NO ESPAÇO TEMPO É NECESSÁRIO RODAR UM PROGRAMA EXATAMENTE ÀS 23:59 DO DIA 31 DE DEZEMBRO DE 2999, PORÉM NESTE 1 MINUTO TODOS OS SISTEMAS FICAM VULNERÁVEIS') 
            for opcao in fase2opcao4Dora:
                    print(opcao)
            escolha = escolhaUsuario()
            
            if escolha == 1:                                   # ESCOLHA 1 * 1 * 1 /
                enrredo('CONSEGUI ACESSAR ORION!, PORÉM OS DISPOSITIVOS DE SEGURANÇA SÃO INTRASNPONÍVEIS, MAS POSSO MANIPULAR AS PESSOAS CONECTADAS A ME FAZER TRANSAÇÕES') 
                passouDeFase('VOCÊ PASSOU DE FASE')
                fase +=1
                # informaFaseePersonagem()
                fase2Dora()
            
            elif escolha == 2:                                     # ESCOLHA 1 * 1 * 2 / 
                enrredo('POBRES GOLFINHOS, VOU USAR ESSA FALHA PARA DESCOBRIR OS CULPADOS')
                perdeuPlayboy('Saindo para manifestação pró golfinhos...')                

        elif escolha == 2:                                 # ESCOLHA 1 * 2 /
                enrredo('OS GOLFINHOS ALADOS SURGIRAM ATRAVÉS DE UMA MUTAÇAO GENÉTICA CAUSADA PELO VAZAMENTO DE RADIAÇÃO DOS GERADORES DE ORION, O QUE FOI UM GRANDE ESCÂNDALO NA ÉPOCA')
                perdeuPlayboy('Tadinho dos golfilnhos, vou sair e me juntar a DolfinsPeace!')
    
     
    elif escolha == 2:                                       # ESCOLHA 2 / 
        enrredo("""DORA FOI SE DIVERTIR EM ORION, E EM UMA CYBERFESTA VÊ 
        UMA PESSOA COLANDO UMA PLACA COM OS DIZERES ---> O QUE ELES NÃO 
        QUEREM QUE VOCÊ SAIBA! O BUG É REAL <---""")
        for opcao in fase1opcao3Dora:
                print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                    # ESCOLHA 2 * 1 /
            enrredo('DORA CORRE ATRÁS DA PESSOA QUE COLOCOU A PLACA MAS A PERDE NA MULTIDÃO')
            perdeuPlayboy('VOCÊ PERDEU')            
            
        elif escolha == 2:                                    # ESCOLHA 2 * 2 / 
            enrredo('DORA NÃO QUER SABER DO BUG DO MILÊNIO E ABRE O IFOME PARA PEDIR UMA COMIDA') 
            perdeuPlayboy('Saindo para buscar a comida que chegou...')            
            
    
def fase2Dora():
    global escolha
    global fase
    # INTRODUÇAO DA FASE
    cabecalho("""DORA É UMA PESSOA MUITO AMBICIOSA, VENDO ESSA OPORTUNIDADE RESOLVEU
TIRAR PROVEITO DA SITUAÇÃO. 

DORA SABE TAMBÉM QUE OS MÉTODOS MODERNOS DE CRIPTOGRAFIA E CYBERSEGURANÇA NÃO
PERMITEM O RACKEAMENTO DE DADOS.

ENTÃO PRECISARIA AGIR RÁPIDO, SABENDO QUE O MECANISMO DOS SERVIDORES ERAM 
INTRANSPONÍVEIS DEVERIA ENTRAR DIRETAMENTE NOS SISTEMAS DAS PESSOAS, 
PRINCIPALMENTE DAQUELAS MAIS DESCUIDADAS.

AO ACESSAR O SISTEMA DAS PESSOAS NO METAVERSO ORION, DORA CONSEGUE MANIPULAR AS 
AÇOES DESSAS PESSOAS QUE PODEM FAZER O QUE DORA DESEJAR.""") 

    # LISTAS COM AS OPÇOES
    fase2opcao1Dora = ['1 - ENCRIPTAR OS DADOS DE KEVIN', 
    '2 - VER DADOS DE KEVIN DISPONÍVEIS E APROVEITAR PARA CHAMAR ELE PARA TOMAR CAFÉ',
    '99 - SAIR']
    fase2opcao2Dora = ['1 - TENTAR ACESSAR O LOGIN DE TRABALHO DE KEVIN EM ORION, ASSIM CONSEGUIR ROUBAR MAIS PESSOAS', 
    '2 - ENSINAR A KEVIN QUE ELE ESTÁ VULNERÁVEL EM ORION',
    '99 - SAIR']
    fase2opcao3Dora = ['1 - IR TOMAR CAFÉ COM KEVIN',
    '2 - PREFIRO TOMAR CAFÉ SÓ',
    '99 - SAIR']
    fase2opcao4Dora = ['1 - DOMINAR KEVIN E ACESSAR TODOS OS DADOS DE ORION', 
    '2 - ALGO INESPERADO ACONTECE, DE ONDE VEM ESSE IP QUE ESTÁ IMPEDINDO MINHA ENTRADA?',
    '99 - SAIR']
    
    # INICIO DAS ESCOLHAS
    for opcao in fase2opcao1Dora:
            print(opcao)
    escolha = escolhaUsuario()
    if escolha == 1:                                         # ESCOLHA 1 / 
        enrredo('KEVIN NÃO ATIVOU A SUA VERIFICAÇÃO DE DUAS ETAPAS E DEIXOU O SEU SISTEMA VULNERÁVEL, ELE AINDA DEIXOU SUAS CREDENCIAIS SALVAS E COSTUMA FREQUENTAR LOCAIS SUSPEITOS. FACILITANDO A ENTRADA DE DORA EM SEU LOGIN DO ORION. DORA ACESSOU OS ARQUIVOS DE KEVIN E VIU QUE ELE TRABALHA EM ORION') 
        if escolha == 1:
            for opcao in fase2opcao2Dora:
                    print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                     # ESCOLHA 1 * 1 /
            enrredo('KEVIN SALVOU SEUS DADOS EM UMA REDE PÚBLICA, O ACESSO A ORION E TODO SISTEMA DE MANUTENÇÃO DO SISTEMA DO QUAL É RESPONSÁVEL FICOU A MOSTRA. A ENTRADA DE DORA NÃO PODERIA MAIS SER EVITADA.') 
            for opcao in fase2opcao4Dora:
                    print(opcao)
            escolha = escolhaUsuario()
            
            if escolha == 1:                                   # ESCOLHA 1 * 1 * 1 /
                enrredo('ACESSANDO... ') 
                passouDeFase('VOCÊ PASSOU DE FASE')
                fase +=1
                # informaFaseePersonagem()
                fase3Dora()
            
            elif escolha == 2:                                 # ESCOLHA 1 * 1 * 2 /
                enrredo('MESMO APÓS DIVERSAS TENTATIVAS A ENTRADA EM ORION FOI BLOQUEADA')
                perdeuPlayboy('Saindo para interromper interceptação')                           

        elif escolha == 2:                                 # ESCOLHA 1 * 2 / 
                enrredo('UTILIZE SOLUÇÕES DE AUTENTICAÇÃO E PRINCIPALMENTE PARE DE ENTRAR EM SITES SUSPEITOS')
                perdeuPlayboy('xxx VOCÊ SABE DO QUE ESTOU FALANDO!!! xxx')                
  
    elif escolha == 2:                                       # ESCOLHA 2 /
        enrredo('CONVITE ACEITO!')
        for opcao in fase2opcao3Dora:
                print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                    # ESCOLHA 2 * 1 / 
            enrredo('DORA ENCONTRA COM KEVIN E APLICA UM GOLPE PESSOALMENTE. ANTES DE ENCONTRAR ALGUÉM QUE CONHECEU EM REDES SOCIAIS VERIFIQUE OS ANTECEDENTES DA PESSOA.')
            perdeuPlayboy('VOCÊ PERDEU')            
            
        elif escolha == 2:                                    # ESCOLHA 2 * 2 / 
            enrredo('DORA NÃO QUER SABER DO BUG DO MILÊNIO E ABRE O IFOME PARA PEDIR UMA COMIDA') 
            perdeuPlayboy('Saindo para buscar a comida que chegou...')            
            

def fase3Dora():
    global escolha
    global fase
    # INTRODUÇAO DA FASE
    cabecalho("""COM O DESCUIDO DE KEVIN, DORA CONSEGUIU ACESSAR OS DATA CENTER DE ORION, TENDO 
ACESSO AO METAVERSO MAIS FAMOSO DO MUNDO, E COM A CHANCE DE ACESSAR OS DADOS DE 
TODOS OS USUÁRIOS. PORÉM NÃO CONTAVA COM ALGO INESPERADO. O QUE SERÁ?""")

    # LISTAS COM AS OPÇOES
    fase3opcao1Dora = ['1 - DENTRO DE ORION DISPARAR MENSAGENS DE PHISHING PARA INFECTAR TODOS OS SEUS USUÁRIOS', 
    '2 - DENTRO DE ORION DISPARAR CORRENTES DE 7 ANOS DE AZAR',
    '99 - SAIR']
    fase3opcao2Dora = ['1 - INSTALAR MALWARE PARA DOMÍNIO DE MENTES NOS INFECTADOS', 
    '2 - INSTALAR MALWARE PARA QUE TODOS DANCEM MACARENA',
    '99 - SAIR']
    fase3opcao3Dora = ['1 - REPASSAR CORRENTE PARA 5 PESSOAS',
    '2 - IGNORAR CORRENTE',
    '99 - SAIR']
    fase3opcao4Dora = ['1 - DOMINAR AS MENTES E TOMAR PARA SI OS NFTS MAIS VALIOSOS', 
    '2 - VERIFICAR POR QUE AS INSTALAÇÕES NÃO ESTÃO FUNCIONANDO',
    '99 - SAIR']
    
    # INICIO DAS ESCOLHAS
    for opcao in fase3opcao1Dora:
            print(opcao)
    escolha = escolhaUsuario()
    if escolha == 1:                                         # ESCOLHA 1 / 
        enrredo('MALWARE INSTALADO, DISPARANDO PHISHING... ') 
        if escolha == 1:
            for opcao in fase3opcao2Dora:
                    print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                     # ESCOLHA 1 * 1 /
            enrredo('O DOMÍNIO DE MENTES É A UNICA FORMA DE CONTROLAR OS DADOS DOS USUÁRIOS, JÁ QUE TODOS MECANISMOS DE BLOCKCHAIN NÃO PODEM SER BURLADOS.') 
            for opcao in fase3opcao4Dora:
                    print(opcao)
            escolha = escolhaUsuario()
            
            if escolha == 1:                                   # ESCOLHA 1 * 1 * 1 /
                enrredo('A FORMA MAIS FÁCIL DE SOFRER GOLPES NA INTERNET É POR FALHA HUMANA, CUIDE DOS SEUS DADOS E NÃO CLIQUE EM QUALQUER COISA') 
                passouDeFase('Dora venceu')                
                
            elif escolha == 2:                                 # ESCOLHA 1 * 1 * 2 /
                enrredo('GIN CONSEGUIU IMPEDIR A INVASÃO')
                passouDeFase('QUER SABER COMO? JOGUE COM ESSA PERSONAGEM')                              

        elif escolha == 2:                                 # ESCOLHA 1 * 2 / 
                enrredo('Dale a tu cuerpo alegría Macarena \nQue tu cuerpo es pa darle alegría y cosa buena \nDale a tu cuerpo alegría, Macarena')
                titulos('Hey Macarena, ay')                              
       
    elif escolha == 2:                                       # ESCOLHA 2 /
        enrredo('Olá! Obrigado por ler esta mensagem. Tem um garoto faminto em Baklaliviatatlaglooshen que não tem braços, não tem pernas, não tem pais e não tem bodes. 😭😭😭 A vida deste menino pode ser salva, porque cada vez que você mandar essa mensagem, um dólar será doado para o Fundo Baklaliviatatlaglooshenense para Garotos Pernetas Manetas Órfãos e sem Bodes. Lembre-se: nós não temos nenhuma maneira de contar quantas cartas foram mandadas, e isso é tudo bobagem, então mande para 5 pessoas nos próximos 47 segundos. Ah, um lembrete: se você mandar acidentalmente para 4 ou 6 pessoas, você morrerá instantaneamente. ☠️😱 Obrigado!')
        for opcao in fase3opcao3Dora:
                print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                    # ESCOLHA 2 * 1 / 
            enrredo('Bem intencionado...')
            perdeuPlayboy('Mas perdeu seu tempo... saindo...')            

        elif escolha == 2:                                    # ESCOLHA 2 * 2 / 
            enrredo('Pensou mesmo que era mentira?') 
            perdeuPlayboy('VOCÊ PERDEU... A VIDA E NÃO PODE CONTINUAR JOGANDO')                        