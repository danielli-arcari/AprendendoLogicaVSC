import random

# Gerar um número inteiro aleatório entre 1 e 10

numero_aleatorio = random.randint(1, 10)
contador = 0
acertou = False

print("Você tem 5 tentativas para acertar o número secreto entre 1 e 10. - acerte_o_numero.py:9")

while contador < 5:
    numero_escolhido = int(input(f"Tentativa {contador + 1}: Digite um número de 1 a 10: "))
    contador += 1

    if numero_escolhido == numero_aleatorio:
        print("Parabéns, você acertou! 🎉 - acerte_o_numero.py:16")
        acertou = True
        break
    else:
        print("Você errou, tente novamente! - acerte_o_numero.py:20")

if not acertou:
    print(f"Suas tentativas acabaram. O número secreto era {numero_aleatorio}. - acerte_o_numero.py:23")


