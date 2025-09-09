# Inicializando listas e variáveis
alturas = []
alturas_masculino = []
contador_feminino = 0

# Coletando dados de 15 pessoas
for i in range(1, 16):
    print(f"\nPessoa {i}:")

    # Validar entrada da altura
    while True:
        try:
            altura = float(input("Digite a altura (em metros): "))
            if altura <= 0:
                print("Altura deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido.")

    # Validar entrada do gênero
    while True:
        genero = input("Digite o gênero (Masculino/Feminino): ").strip().lower()
        if genero in ['masculino', 'feminino']:
            break
        else:
            print("Gênero inválido. Digite 'Masculino' ou 'Feminino'.")

    # Armazenando os dados
    alturas.append(altura)

    if genero == 'masculino':
        alturas_masculino.append(altura)
    elif genero == 'feminino':
        contador_feminino += 1

# Processando os resultados
maior_altura = max(alturas)
menor_altura = min(alturas)

# Média de altura dos homens
if alturas_masculino:
    media_masculino = sum(alturas_masculino) / len(alturas_masculino)
else:
    media_masculino = 0

# Exibindo os resultados
print("\n=== RESULTADOS ===")
print(f"Maior altura do grupo: {maior_altura:.2f} m")
print(f"Menor altura do grupo: {menor_altura:.2f} m")
print(f"Média de altura dos homens: {media_masculino:.2f} m")
print(f"Número de mulheres: {contador_feminino}")
