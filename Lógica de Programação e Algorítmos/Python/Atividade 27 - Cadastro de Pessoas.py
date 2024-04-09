def adicionar_pessoa( ):
    nome = input("Digite o nome da pessoa:")
    email = input("Digite o email da pessoa:")

    with open ("pessoa.txt", "a") as arquivo:
        arquivo.write(f"{nome} , {email}")

        print("Pessoa cadastrada com sucesso!")

adicionar_pessoa( )

def listar_pessoa( ):
    with open("pessoa.txt", "r") as arquivo:
        print("Pessoas Cadastradas:")
        for linha in arquivo:
            nome, email = linha.split(",")
            print(f"Nome: {nome} , Email: {email}")

            #adicionar_pessoa( )
            listar_pessoa( )