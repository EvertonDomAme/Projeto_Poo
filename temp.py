cargo = int(input(""" 
    Escolha como jogar(profissão definida ou não :
    0 - Padrão
    1 - Garçon
    2 - Enfermeiro
    """))

    if 0 >= cargo >= 2 :
        if cargo == 0:
           personagem = Personagem(nome)#inclusão de parametro nome
        elif cargo == 1:
            personagem = Garcon(nome)
        else :
            personagem = Enfermeiro(nome)
    else:
        print("Opção inválida, tente novamente")

print(personagem)
