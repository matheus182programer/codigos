dados = []

for i in range(3):
    print(f"\nPessoa {i+1}")

    nome = input("fale seu nome:")
    filme = input("filme assistido:")

    while True:
        try:
            nota = float(input("digite uma nota de (0 a 10)"))
            if 0 <= nota <= 10:
                break
            else:
                print("sua nota não e valida.")
        except ValueError:
            print("Por favor, digite um número válido.")

    dados.append((nome, filme, nota))

print("\nDados cadastrados:")
for pessoa in dados:
    print(f"Nome: {pessoa[0]} | Filme: {pessoa[1]} | Nota: {pessoa[2]}")





