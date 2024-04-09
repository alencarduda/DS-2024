n1 = input("Digite a primeira nota:")
n1 = float(n1)

print(n1)
print(type(n1))

n2 = float(input("Digite a segunda nota:"))

print(n2)
print(type(n2))

n3 = float(input("Digite a terceira nota:"))
print(n3)
print(type(n3))

soma = n1 + n2 + n3
media = soma / 3

print("A média do aluno é:", media)

if media >= 7:
    print("Aprovado")

elif media <= 7:
    print("Em recuperação")

else:
    print("Reprovado")