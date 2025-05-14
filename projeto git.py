print("Hello Word")

nome = "Matheus"
idade = 17
altura = 1.71

#exibir informação
print("Nome:", nome)
print("idade:",idade, "anos")
print("altura:", altura, "m")

#somando dois numeros
numero1 = int(input("Digite o primeiro numero"))
numero2 = int(input("Digite o segundo numero"))
resultado = numero1 + numero2
print("0 resultado é:", resultado)

#receba nome, idade e cidade
idade = (input("Digite sua idade"))
nome = int(input("Digite seu nome"))
cidade = (input("Digite sua cidade"))


print("seu nome é:", nome)
print("sua idade é:", idade)
print("seu cidade é:", cidade)




#para pre programar o valor basta colocar o numero desejado
numero1 = 15
numero2 = int(input("Digite a quantidade:"))
resultado = numero1 * numero2
print("0 resultado é:", resultado)




#while siguinifica enquanto
contador=1
while contador <=5:
    numero= int(input("digiteum numero"))
    soma = soma + numero
    contador = contador +1
    print ("o resultado e:" ,soma)




    # Solicita ao usuário que digite um número
numero = int(input("Digite um número para ver a tabuada: "))

# Mostra a tabuada de 1 a 10
print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")





    # Solicita dois números ao usuário
inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))

# Garante que o início seja menor que o fim
if inicio > fim:
    inicio, fim = fim, inicio

print(f"\nNúmeros pares entre {inicio} e {fim}:")

# Percorre os números no intervalo e exibe apenas os pares
for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        print(numero)







print 
nome = input("insira seu nome:")
quantidade = int(input("insira a quantidade do produto:"))
valor = int(input("escreva o valor do produto:"))
resultado = valor * quantidade
print (f"ola {nome}")
print (f"valor do produto: {valor}")
print (f"o resultado foi de:{resultado} reais")





alunos = []

for i in range(5):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    av1 = float(input(f"Digite a nota da AV1 de {nome}: "))
    av2 = float(input(f"Digite a nota da AV2 de {nome}: "))
    media = (av1 + av2) / 2
    alunos.append([nome, av1, av2, media])

print("\nDados dos alunos:")
for aluno in alunos:
    print(f"Nome: {aluno[0]}, AV1: {aluno[1]:.2f}, AV2: {aluno[2]:.2f}, Média: {aluno[3]:.2f}")


