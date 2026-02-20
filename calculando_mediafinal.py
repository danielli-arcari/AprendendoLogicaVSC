#estudando estrutura for em python:
def quantidade_notas():
    quantidade = int(input("Vamos somar as notas e calcular a média. Quantas notas você deseja inserir? "))
    return quantidade

numero_de_notas = quantidade_notas()

soma = 0
for i in range(1, numero_de_notas + 1):
    nota = float(input(f'Informe a sua nota {i}: '))
    soma = soma + nota

media = soma / numero_de_notas

print("\n Resultados Finais - calculando_mediafinal.py:15")
print(f'A soma das {numero_de_notas} notas é: {soma} - calculando_mediafinal.py:16')
print(f'A média final é: {media:.2f} - calculando_mediafinal.py:17')