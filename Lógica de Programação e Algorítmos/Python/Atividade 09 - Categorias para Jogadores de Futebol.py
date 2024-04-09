idade = input("Escreva sua idade:")
idade = float(idade)

if idade <= 13:
    print("Selecionado para a Categoria Infantil")

elif idade <= 17:
    print("Selecionado para a Categoria Junvenil")

else:
    print("Selecionado para a Categoria Sênior")