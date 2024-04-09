"""lista = [ ]

lista.append (1)
lista.append("Fulano")
lista.append(33.7)
lista.append(True)

print(type(lista))
print(lista[0])
"""

lista = [ ]

nome = input("Nome do Produto:")
print(nome)
print(type(nome))

valor = input("Valor do Produto:")
print(valor)
print(type(valor))

quantidade = input("Quantidade do Produto:")
print(quantidade)
print(type(quantidade))

descricao = input("Descrição do Produto:")
print(descricao)
print(type(descricao))

adicionar_produto( )

def listar_produto( ):
    with open("produto.txt", "r") as arquivo:
        print("Produtos registrados:")
        for linha in arquivo:
            nome, valor, quantidade, descricao = linha.split(",")
            print(f"Nome: {nome} , Valor: {valor} , Quantidade: {quantidade}, Descricao: {descricao}")

            #adicionar_produto( )
            listar_produto ( )