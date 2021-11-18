
from projetofinalmodulo1 import *

def fase1Dora():
    global escolha
    global fase
    informaFaseePersonagem()
    # INTRODUÇAO DA FASE
    enrredo("""Dora é uma pessoa muito curiosa, e descobriu sobre uma lenda urbana, a do bug do 
milenio de 1999. isso fez Dora pensar, será mesmo uma lenda urbana? o que há de 
verdade sobre isso?""") 
    
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
        enrredo("""Acessando aquivos... O erro conhecido como bug do milênio foi causado pela configuração de datas 
em sistemas de computação. Com a chegada do ano 2000 os computadores interpretariam o ano 00 como 
1900, gerando efeitos em cascata na linha temporal dos programas que regrediriam 100 anos e uma 
enorme falha de cybersegurança.""")
        if escolha == 1:
            for opcao in fase1opcao2Dora:
                    print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                     # ESCOLHA 1 * 1 /
            enrredo("""Para evitar a regressão de 100 anos no espaço tempo é necessário rodar um programa exatamente 
às 23:59 do dia 31 de dezembro de 2999, porém neste 1 minuto todos os sistemas ficam vulneráveis""") 
            for opcao in fase2opcao4Dora:
                    print(opcao)
            escolha = escolhaUsuario()
            
            if escolha == 1:                                   # ESCOLHA 1 * 1 * 1 /
                enrredo("""Consegui acessar Orion! Porém os dispositivos de segurança são intrasnponíveis, mas posso 
manipular as pessoas conectadas a me fazer transações""") 
                passouDeFase('VOCÊ PASSOU DE FASE')
                fase +=1
                informaFaseePersonagem()
                fase2Dora()
            
            elif escolha == 2:                                     # ESCOLHA 1 * 1 * 2 / 
                enrredo("""Pobres golfinhos, vou usar essa falha para descobrir os culpados""")
                perdeuPlayboy('Saindo para manifestação pró golfinhos...')                

        elif escolha == 2:                                 # ESCOLHA 1 * 2 /
                enrredo("""Os golfinhos alados surgiram através de uma mutaçao genética causada pelo vazamento de 
radiação dos geradores de Orion, o que foi um grande escândalo na época""")
                perdeuPlayboy('Tadinho dos golfilnhos, vou sair e me juntar a DolfinsPeace!')
    
     
    elif escolha == 2:                                       # ESCOLHA 2 / 
        enrredo("""Dora foi se divertir em Orion, e em uma cyberfesta vê 
uma pessoa colando uma placa com os dizeres ---> O que eles não 
querem que você saiba! O bug é real <---""")
        for opcao in fase1opcao3Dora:
                print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                    # ESCOLHA 2 * 1 /
            enrredo("""Dora corre atrás da pessoa que colocou a placa mas a perde na multidão""")
            perdeuPlayboy('VOCÊ PERDEU')            
            
        elif escolha == 2:                                    # ESCOLHA 2 * 2 / 
            enrredo("""Dora não quer saber do bug do milênio e abre o ifome para pedir uma comida""") 
            perdeuPlayboy('Saindo para buscar a comida que chegou...')            
            
    
def fase2Dora():
    global escolha
    global fase
    # INTRODUÇAO DA FASE
    cabecalho("""Dora é uma pessoa muito ambiciosa, vendo essa oportunidade resolveu
tirar proveito da situação. 

Sabe também que os métodos modernos de criptografia e cybersegurança não
permitem o rackeamento de dados.

Então precisaria agir rápido, sabendo que o mecanismo dos servidores eram 
intransponíveis deveria entrar diretamente nos sistemas das pessoas, 
principalmente daquelas mais descuidadas.

Ao acessar o sistema das pessoas no metaverso Orion, Dora consegue manipular as 
ações dessas pessoas que podem fazer o que Dora desejar.""") 

    # LISTAS COM AS OPÇOES
    fase2opcao1Dora = ['1 - ENCRIPTAR OS DADOS DE KEVIN', 
    '2 - VER DADOS DE KEVIN DISPONÍVEIS E APROVEITAR PARA CHAMAR ELE PARA TOMAR CAFÉ',
    '99 - SAIR']
    fase2opcao2Dora = ["""1 - TENTAR ACESSAR O LOGIN DE TRABALHO DE KEVIN EM ORION, 
    ASSIM CONSEGUIR ROUBAR MAIS PESSOAS""", 
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
        enrredo("""Kevin não ativou a sua verificação de duas etapas e deixou o seu sistema vulnerável, ele ainda 
deixou suas credenciais salvas e costuma frequentar locais suspeitos.""") 
        if escolha == 1:
            for opcao in fase2opcao2Dora:
                    print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                     # ESCOLHA 1 * 1 /
            enrredo("""Kevin salvou seus dados em uma rede pública, o acesso a Orion e todo sistema de manutenção 
do sistema do qual é responsável ficou a mostra. a entrada de Dora não poderia mais ser evitada.""") 
            for opcao in fase2opcao4Dora:
                    print(opcao)
            escolha = escolhaUsuario()
            
            if escolha == 1:                                   # ESCOLHA 1 * 1 * 1 /
                enrredo('Acessando... ') 
                passouDeFase('VOCÊ PASSOU DE FASE')
                fase +=1
                informaFaseePersonagem()
                fase3Dora()
            
            elif escolha == 2:                                 # ESCOLHA 1 * 1 * 2 /
                enrredo('Mesmo após diversas tentativas a entrada em Orion foi bloqueada')
                perdeuPlayboy('Saindo para interromper interceptação')                           

        elif escolha == 2:                                 # ESCOLHA 1 * 2 / 
                enrredo('Utilize soluções de autenticação e principalmente pare de entrar em sites suspeitos')
                perdeuPlayboy('xxx Você sabe do que estou falando!!! xxx')                
  
    elif escolha == 2:                                       # ESCOLHA 2 /
        enrredo('Convite aceito!')
        for opcao in fase2opcao3Dora:
                print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                    # ESCOLHA 2 * 1 / 
            enrredo("""Dora encontra com kevin e aplica um golpe pessoalmente. Antes de encontrar alguém que 
conheceu em redes sociais verifique os antecedentes da pessoa.""")
            perdeuPlayboy('VOCÊ PERDEU')            
            
        elif escolha == 2:                                    # ESCOLHA 2 * 2 / 
            enrredo('Dora não quer saber do bug do milênio e abre o ifome para pedir uma comida') 
            perdeuPlayboy('Saindo para buscar a comida que chegou...')            
            

def fase3Dora():
    global escolha
    global fase
    # INTRODUÇAO DA FASE
    cabecalho("""Com o descuido de kevin, Dora conseguiu acessar os data center de Orion, tendo 
acesso ao metaverso mais famoso do mundo, e com a chance de acessar os dados de 
todos os usuários. porém não contava com algo inesperado. o que será?""")

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
        enrredo('Malware instalado, disparando phishing...') 
        if escolha == 1:
            for opcao in fase3opcao2Dora:
                    print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                     # ESCOLHA 1 * 1 /
            enrredo("""O domínio de mentes é a única forma de controlar os dados dos usuários, já que todos 
mecanismos de blockchain não podem ser burlados.""") 
            for opcao in fase3opcao4Dora:
                    print(opcao)
            escolha = escolhaUsuario()
            
            if escolha == 1:                                   # ESCOLHA 1 * 1 * 1 /
                enrredo("""A forma mais fácil de sofrer golpes na internet é por falha humana, cuide dos seus 
dados e não clique em qualquer coisa""") 
                passouDeFase('Dora venceu')                
                
            elif escolha == 2:                                 # ESCOLHA 1 * 1 * 2 /
                enrredo('Gin conseguiu impedir a invasão')
                passouDeFase('Quer saber como? jogue com essa personagem')                              

        elif escolha == 2:                                 # ESCOLHA 1 * 2 / 
                enrredo('Dale a tu cuerpo alegría Macarena \nQue tu cuerpo es pa darle alegría y cosa buena \nDale a tu cuerpo alegría, Macarena')
                titulos('Hey Macarena, ay')                              
       
    elif escolha == 2:                                       # ESCOLHA 2 /
        enrredo("""Olá! Obrigado por ler esta mensagem. Tem um garoto faminto em Baklaliviatatlaglooshen que não 
tem braços, não tem pernas, não tem pais e não tem bodes. 😭😭😭 A vida deste menino pode ser 
salva, porque cada vez que você mandar essa mensagem, um dólar será doado para o Fundo 
Baklaliviatatlaglooshenense para Garotos Pernetas Manetas Órfãos e sem Bodes. Lembre-se: nós não 
temos nenhuma maneira de contar quantas cartas foram mandadas, e isso é tudo bobagem, então mande 
para 5 pessoas nos próximos 47 segundos. 
Ah, um lembrete: se você mandar acidentalmente para 4 ou 6 pessoas, 
você morrerá instantaneamente. ☠️😱 Obrigado!""")
        for opcao in fase3opcao3Dora:
                print(opcao)
        escolha = escolhaUsuario()
        
        if escolha == 1:                                    # ESCOLHA 2 * 1 / 
            enrredo('Bem intencionado...')
            perdeuPlayboy('Mas perdeu seu tempo... saindo...')            

        elif escolha == 2:                                    # ESCOLHA 2 * 2 / 
            enrredo('Pensou mesmo que era mentira?') 
            perdeuPlayboy('VOCÊ PERDEU... A VIDA E NÃO PODE CONTINUAR JOGANDO')                        