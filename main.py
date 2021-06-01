# Proposta de projeto de ficção interativa para avaliação de OO
# Sugestão: completar com classes filhas colocando pessoas saudáveis, trabalhos menos remunerados, casas melhor equipadas et cetera
import random#Random inportado para implementação dos efeitos aleatórios
usuario = " "#variável que vai registrar/receber os dados de cadastro de usuário
senha = " "#variável que vai registrar/receber os dados de cadastro de senha

class AcessoSeguro: #classe definida para registro de usuário e senha
    def __init__(self, usuario, senha):
        self.__usuario = usuario
        self.__senha = senha

    @property#método com encapsulamento para retornar dados de usuário
    def usuario(self):
        return self.__usuario

    @property#método com encapsulamento para retornar dados de senha
    def senha(self):
        return self.__senha

    @usuario.setter#método com encapsulamento para alterar dados de usuário
    def usuario(self, novoUsuario):
        self.__usuario = novoUsuario
        
    @senha.setter#método com encapsulamento para alterar dados de senha
    def senha(self,novaSenha):
        self.__senha = novaSenha
        

usuario = input("Cadastre seu Usuário de acesso :")#Entrada para cadastro de usuário
senha =   input("Cadastre sua Senha de acesso :")#Entrada para cadastro de senha

#informação dos dados cadastrados de usuário e senha
print(f"""
Estes são seus dados de acesso, memorize-os :
Usuário : {usuario}
Senha :   {senha}
""")

while True:#Laço de repetição com input para, caso, o usuário queira alterar algum dado dos cadastros de usuário e senha
    alterar = int(input("""
    Alterar Usuário ou Senha:
    0 - Manter
    1 - Alterar Usuário
    2 - Alterar Senha
""") )
#Condicionais que geram opção para poder ou não alterar usuário e ou senha
    if alterar not in (0,1,2) :
        print("Opção inválida")   
    elif alterar == 1 :
        usuario = input("Informe seu novo Usuário de acesso : ")
    elif alterar == 2 :
        senha = input("Informe sua nova Senha de acesso : ")
    else :     
        break

print("Informe Usuário e Senha para acesso.")#Orientação ao usuário

usuarioA = input("Usuário : ")#entrada para acesso com usuário
while usuarioA != usuario:#Laço para validar usuário
    print("Usuário não encontrado!\nVerifique seu usuário de acesso e tente novamente.")
    usuarioA = input("Informe seu usuário de acesso novamente\nUsuário : ")

senhaA = input("Senha : ")#entrada para acesso com senha
while senhaA != senha :#laço para validar senha
    print("Senha incorreta!\nVerifique sua senha de acesso e tente novamente!")
    senhaA = input("Informe sua senha de acesso novamente!\nSenha : ")

class Relogio:
    def __init__(self):
        self.horas = 6 
        self.minutos = 0
    
    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1

    def atrasado(self):
        return (self.horas > 7 or (self.horas == 7 and self.minutos > 30))
        #alteração no horario de atraso para 07:30hr

class Personagem:
    def __init__(self, nome):#inclusão do parametro nome
        self.nome = nome#inclusão do parametro nome
        self.sujo = True
        self.fome = True
        self.medicado = False
        self.disposicao = False#inclusão de academia
        self.dinheiro = 0
        self.salario = 100
        self.valorRemedios = 20#Valor dos remédios que era definido, agora é atributo da classe Personagem
        self.valorComida = 15#Valor da comida que era definido, agora é atributo da classe Personagem

    @property#
    def classe0(self):
        return Personagem(nome)

    def __str__(self):
        return  f"{self.nome} você está " + ("sujo(a)" if self.sujo else "limpo(a)")+", "+("com" if self.disposicao else "sem")+" disposição, "+("com" if self.fome else "sem")+" fome e "+("" if self.medicado else "não ")+"tomou sua medicação. Você tem "+str(self.dinheiro)+" reais na sua conta."
                    #inclusão de nome no print
    def dormir(self):
        self.sujo = True
        self.fome = True
        self.disposicao = False#inclusão de disposição relacionado a opçao de academia
        self.medicado = False

class Garcon(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        # self.nome = nome#inclusão do parametro nome
        self.sujo = True
        self.fome = True
        self.medicado = False
        self.disposicao = False#inclusão de academia
        self.dinheiro = 0
        self.salario = 110#Salário de Garçom 10% maior
        self.valorRemedios = 20
        self.valorComida = 7 #Garçon tem valor de comida reduzido

    @property
    def classe0(self):
        return Garcon(nome)

    def __str__(self):
        return  f"{self.nome} você está " + ("sujo(a)" if self.sujo else "limpo(a)")+", "+("com" if self.disposicao else "sem")+" disposição, "+("com" if self.fome else "sem")+" fome e "+("" if self.medicado else "não ")+"tomou sua medicação. Você tem "+str(self.dinheiro)+" reais na sua conta."
                    #inclusão de nome no print
    def dormir(self):
        self.sujo = True
        self.fome = True
        self.disposicao = False#inclusão de disposição relacionado a opçao de academia
        self.medicado = False

class Enfermeiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.sujo = True
        self.fome = True
        self.medicado = False
        self.disposicao = False#inclusão de academia
        self.dinheiro = 0
        self.salario = 110#Salário de Enfermeior 10% maior
        self.valorRemedios = 10#Enfermeiro tem vaor de remédio reduzido
        self.valorComida = 15

    @property
    def classe0(self):
        return Enfermeiro(nome)

    def __str__(self):
        return  f"{self.nome} você está " + ("sujo(a)" if self.sujo else "limpo(a)")+", "+("com" if self.disposicao else "sem")+" disposição, "+("com" if self.fome else "sem")+" fome e "+("" if self.medicado else "não ")+"tomou sua medicação. Você tem "+str(self.dinheiro)+" reais na sua conta."
                    #inclusão de nome no print
    def dormir(self):
        self.sujo = True
        self.fome = True
        self.disposicao = False#inclusão de disposição relacionado a opçao de academia
        self.medicado = False

class Casa:
    def __init__(self):
        self.remedios = 1      
        self.comida = 5

if(__name__ == "__main__"):
    dia = 1
    relogio = Relogio()
    nome = input("Digite o nome do seu personagem :").title()#inclusão de nome ao personagem com entrada pelo usuário
    cargo = int(input(""" 
                    Escolha como jogar(profissão definida ou não :
                    0 - Padrão
                    1 - Garçon
                    2 - Enfermeiro
                    """))
    while True:
        if cargo == 0:
            personagem = Personagem(nome)#inclusão de parametro nome
            break
        elif cargo == 1:
            personagem = Garcon(nome)
            break
        elif cargo == 2:
            personagem = Enfermeiro(nome)
            break
        else:
            print("Opção inválida, tente novamente")
            cargo = int(input(""" 
                    Escolha como jogar(profissão definida ou não :
                    0 - Padrão
                    1 - Garçon
                    2 - Enfermeiro
                    """))

    #personagem = Personagem(nome)
    casa = Casa()
    cafe_da_manha = False
    
    while True:
        print("---")
        print(f"{nome}... São "+str(relogio)+" do dia "+str(dia)+". Você tem que sair pro trabalho até às 07:30.")
        print(personagem)
        print("")
        print("Ações:")
        print("1 - Tomar banho e escovar os dentes")
        print("2 - Fazer café da manhã")
        print("3 - Pedir café da manhã")
        print("4 - Tomar café da manhã")
        print("5 - Tomar remédio")
        print("6 - Comprar remédio")
        print("7 - Ir para Academia")#inclusa ação de ir a academia
        print("8 - Ir trabalhar")#opção Ir Trabalhar passa a ser a opção 8
        print("0 - Sair do jogo")
        
        opcao = input(f"{nome} escolha sua ação:")
        if dia > 10 :#10 dias definidos para maximo de dias jogáveis
            print("Os 10 dias do simulador se encerraram, você concluiu com sucesso! Obrigado por jogar nosso jogo!")    
            break
        elif(opcao == "1"):          
            personagem.sujo = False
            relogio.avancaTempo(20)
        elif(opcao == "2"):
            if(casa.comida > 0):
                casa.comida -= 1
                cafe_da_manha = True
            else:
                print(f"{nome}, não há comida em casa.")
            relogio.avancaTempo(15)
        elif(opcao == "3"):
            if(personagem.dinheiro >= personagem.valorComida):#Novo atributo da classe Personagem
                personagem.dinheiro -= personagem.valorComida
                cafe_da_manha = True
            else:          #inclusão de nome no print
                print(f"{nome}, o café da manhã custa R${personagem.valorComida},00 reais, você não tem dinheiro suficiente.")
            relogio.avancaTempo(5)                          #Novo atributo da classe Personagem
        elif(opcao == "4"):
            if(cafe_da_manha):
                personagem.fome = False
                cafe_da_manha = False
                relogio.avancaTempo(15)
            else:
                print(f"{nome}, não tem café da manhã na sua casa.")
                relogio.avancaTempo(5)
        elif(opcao == "5"):
            if(casa.remedios > 0):
                casa.remedios -= 1
                personagem.medicado = True
            else:
                print(f"{nome}, não tem remédio na sua casa")
            relogio.avancaTempo(5)
        elif(opcao == "6"):
            if(personagem.dinheiro >= personagem.valorRemedios):#Novo atributo da classe Personagem
                casa.remedios += 10
                personagem.dinheiro -= personagem.valorRemedios
                relogio.avancaTempo(10)
            else:
                print(f"{nome}, a cartela com 10 remédios custa 20 reais, você não tem dinheiro suficiente.")
                relogio.avancaTempo(5)
        #inclusão de academia nas condicionais
        elif(opcao == "7"):
            if(personagem.dinheiro >= 30):#Condição para 
                personagem.disposicao = True#Personagem recebe o bônus de disposição
                personagem.sujo = True#Personagem recebe 'True" ao atributo sujo
                personagem.dinheiro -= 30#Desconto do valor do dis de academia
                relogio.avancaTempo(25)#Custo de tempo para ir a academia
            else :
                print('-=-=-'*25)
                print(f"{nome}o dia na academia custa R$30,00,você não tem dinheiro... Hoje você não conseguiu ir a academia, se sentiria mais disposto e poderia render melhor no trabalho!!! Uma pena!!!")
                relogio.avancaTempo(10)#Custo de tempo por tentar ir a academia sem ter dinheiro suficiente
        elif(opcao == "8"):
            recebido = personagem.salario#recebido, definido antes para podeer executar os calculos das adversidades
            adversidade = random.randint(1,100)#Random de 1 a 100 - entre 1:40 uma dentre 8 adversidades é executada
            #print(adversidade)
            if adversidade <= 5  :#Primeiro random, se o valor de adversidade for entre 1 e 5 resulta nesse random
                print(f"""
                {nome}, O transporte coletivo está em greve...
                Você pode ir caminhando ou pedir um taxi(Caso tenha dinheiro suficiente)!
                1 - Caminhar até o trabalho por 20 min.
                2 - Solicitar um taxi, custo : R$25,00 e 05 min.
                """)
                escolha1 = int(input("O que fazer? (1 ou 2) :"))#Entrada de opção de ação dentreo da primeira adversidade
                if escolha1 != 1 and escolha1 != 2 :#validação de escolha
                    print("Opção inválida, tente novamente")
                elif escolha1 == 1 :
                    relogio.avancaTempo(20)
                    print("Você caminhou por 20 minutos até o trabalho!")
                else :
                    relogio.avancaTempo(5)
                    personagem.dinheiro -= 25  
                    print("Você economizou tempo, mas não dinheiro...  A corrida custou R$25,00.")              
            elif adversidade <= 10  :
                print(f"""
                {nome},
                No caminho para o trabalho, você vê um Sr. sentado na calçada, pedindo
                ajuda para se levantar, mas as pessoas passam a sua volta sem ajudá-lo!
                Ele pede sua ajuda para se levantar... 
                1 - Ajudar o Sr. a se levantar.
                2 - Passar sem ajudar e ir direto para o trabalho.
                """)
                escolha2 = int(input("O que fazer? (1 ou 2) :"))
                if escolha2 != 1 and escolha2 != 2 :
                    print("Opção inválida, tente novamente")
                elif escolha2 == 1 :
                    personagem.dinheiro -= 25
                    print("Toda boa ação tem sua punição... você decidiu ajudar o Sr. que por sua vez\nfurtou sua carteira, por sorte só haviam R$25,00 na carteira.")
                else :
                    personagem.sujo = True
                    print("Você decidiu passar direto pelo Sr. e ao tentar passar apressado,\ntropeçou na calçada e caiu direto em uma poça...\nAgora você está sujo! (DEVE SER KARMA!!!")                    
                relogio.avancaTempo(5)
                
            elif adversidade <= 15  :
                print(f"""
                {nome}, 
                Você está chegando ao trabalho e percebe uma Senhora, que precisa de ajuda para  atravessar a rua...
                Ajudar a Senhora ou correr para bater o cartão?
                1 - Ajudar a Senhora a atravessar a rua.
                2 - Correr para bater o cartão.
                """)
                escolha3 = int(input("O que fazer? (1 ou 2) :"))
                if escolha3 != 1 and escolha3 != 2 :
                    print("Opção inválida, tente novamente")
                elif escolha3 == 1 :
                    relogio.avancaTempo(10)
                    personagem.dinheiro += 15
                    print("A senhora que ajudou a atravessar a rua, é mãe do seu chefe...\nSeu chefe presenciou seu ato de bondade e lhe reconpensou!")
                else :
                    personagem.salario = 90
                    print("Seu chefe presenciou a sua falta de empatia com a necessidade dos mais velhos e não gostou do que viu...\nVocê teve seu cargo rebaixado e seu salário passou a ser de R$90,00 por dia.")
            elif adversidade <= 20 :
                print(f"""
                {nome}, 
                No caminho para o trabalho você presencia uma criança que se engasgou com uma bala...
                Você pode ajudá-la?
                1 - Sim
                2 - Não
                """)
                escolha4 = int(input("O que fazer? (1 ou 2) :"))
                if escolha4 != 1 and escolha4 != 2 :
                    print("Opção inválida, tente novamente")
                elif escolha4 == 1 :
                    relogio.avancaTempo(20)
                    casa.remedios += 10
                    print("Você ajudou a filha da sua Farmaceutica!\nComo reconpensa ela te forneceu uma cartela do seu remédio!")
                else :      
                    personagem.valorRemedios += 5
                    print("Você deixou de ajudar a filha da Farmaceutica que fornece seus remédios!")
            elif adversidade <= 25 :
                print(f"""
                {nome},  
                Hoje a caminho do trabalho, viu um rapaz caminhando em direção ao Banco
                e percebeu que ele deixou cair um envelope, esse envelope aparenta estar bem cheio!
                Agora...
                Você pode pegar o envelope pra si e seguir seu caminho ou pegar esse envelope
                e entregar ao rapaz que o perdeu a caminho do banco!
                1 - Pegar o envelope e seguir seu caminho!
                2 - Pegar o envelope e entregar ao rapaz no banco
                """)
                escolha5 = int(input("O que fazer? (1 ou 2) :"))
                if escolha5 != 1 and escolha5 != 2 :
                    print("Opção inválida, tente novamente")
                elif escolha5 == 1 :
                    relogio.avancaTempo(5)
                    personagem.medicado = False
                    print(f"""{nome}, você foi capaz de pegar o envelope de forma que ninguém percebesse,
                    nesse envelope havia um material estranho e ao abrir você inalou um pouco desse material!
                    E isso cortou o efeito do seu remédio!""")
                else :
                    relogio.avancaTempo(15)
                    print("""
                    Você conseguiu encontrar o rapaz, que ficou muito contente com sua atitude!
                    Se sinta orgulhoso, você não ganhou nada e perdeu 15 minutos! 
                    Mas ajudou uma família inteira!
                    Como dizem : Toda boa ação tem sua punição!
                    """)
                  
            elif adversidade <= 30 :
                if personagem.fome == False :
                    print(f"""
                    {nome}, 
                    Seu café da manhã, aparentemente não te fez bem!
                    Você está com mal estar estomacal, além dos gases, que exalam um mal cheiro terrível!
                    Suas opçoes são :
                    1 - Trabalhar normalmente e fingir que nada está acontecendo!
                    2 - Procurar por uma farmácia no caminho e comprar um medicamento!
                    """)
                    escolha6 = int(input("O que fazer? (1 ou 2) :"))
                    if escolha6 != 1 and escolha6 != 2 :
                        print("Opção inválida, tente novamente")
                    elif escolha6 == 1 :
                        personagem.sujo = True
                        print("O mal cheiro incomodou seus colegas de trabalho!")
                    else :
                        relogio.avancaTempo(15)
                        personagem.dinheiro -= 15
                        print("Você perdeu 15 minutos, mas encontrou uma farmácia e o medicammento resolveu seu problema!")
            elif adversidade <= 35 :
                print(f"""
                {nome}, 
                A caminho do trabalho, você vê dois cães brigando...
                Você separa ou deixa brigar?
                1 - Separar a briga dos cães.
                2 - Seguir seu caminho.
                """)
                escolha7 = int(input("O que fazer? (1 ou 2) :"))
                if 1> escolha7 > 2 :
                    print("Opção inválida, tente novamente")
                elif escolha7 == 1 :
                    relogio.avancaTempo(15)
                    personagem.dinheiro -= 10
                    print("""
                    Você separou a briga dos cães e um deles te mordeu...
                    Você teve que provcurar uma farmácia para que fosse feito curativo e tomar vacina antirrábica!
                    """)
                else :
                    relogio.avancaTempo(25)
                    personagem.dinheiro -= 35
                    personagem.sujo = True
                    print("""
                    Você não separou a briga dos cães...
                    Passou direto por eles, que por sua vez pararam de brigar e ambos avançaram em sua direção!
                    Você teve que correr, e mesmo assim um dos cães conseguiu te morder!
                    Você ficou com aspecto 'Sujo', além de ter gastos com ferimentos e vacina antirrábica!
                    """)
            elif adversidade <= 40  :
                print(f"""
                {nome}, 
                Um belo dia a caminho do trabalho e você encontra duas pessoas ilustres!
                O Presidente do 'Python' da Gama, Eurico;
                e...
                Gabriel o 'Programador', fazendo rimas em Python!
                Ambos te ofereceraum uma oportunidade...
                A oportunidade de se juntar a eles em uma jornada de aprendizado
                A de adquirir vasto conhecimento em Python e conseguir imprimir 'Hello World!'...
                Você topa ou não topa?
                1 - Vamos lá, quero me tornar Programador!
                2 - Vamos lá, vou me tornar Programador!
                """)
                escolha8 = int(input("O que fazer? (1 ou 2) :"))
                if 1 > escolha8 > 2 :
                    print("Opção inválida, tente novamente")
                elif escolha8 == 1 :
                    personagem.salario += 25
                    print('Você fez uma escolha estupenda... Vai mudar o rumo da sua vida! Foco!')
                else :
                    personagem.dinheiro += 25
                    print('Você fez uma escolha maravilhosa... Vai mudar sua vida para melhor! Foco!')
            else:
                print("-=-=-")
                print(f"{nome}, você chegou ao trabalho.")
                print(personagem)
                print("-=-=-")
                recebido = personagem.salario
            if(not personagem.medicado):
                print(f"{nome}, como você não tomou seu remédio, você ficou doente no caminho e não chegou no trabalho")
                recebido = 0
            elif(personagem.sujo):
                print(f"{nome}, como você não fez sua higiene pessoal, seus colegas reclamaram para seu chefe, e você levou uma advertência.")
                recebido *= 0.9
            elif(personagem.fome):
                print(f"{nome}, como você estava com fome, você trabalhou metade do que consegue trabalhar.")
                recebido *= 0.5
            elif(relogio.atrasado()):
                print(f"{nome}, como você chegou atrasado, você produziu menos do que de costume.")
                recebido *= 0.8
            elif(personagem.disposicao):#inclusão de academia no fator salario
                print(f"{nome}, como você conseguiu ir a academia, se sentiu mais disposto e teve melhor produtividade do que de costume.")
                recebido *= 1.15
            print(f"{nome}, você recebeu "+str(recebido)+" reais pelo seu trabalho hoje.")
            print("-=-=-")

            personagem.dinheiro += recebido
            personagem.dormir()
            relogio = Relogio()
            dia+=1
        elif(opcao == "0"):#adicionado contagem de dias para encerrar o jogo(or dia == 7)
            print("Obrigado por jogar!")
            break
        else:
            print("Opção inválida!")
            relogio.avancaTempo(5)