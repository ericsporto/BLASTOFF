frase = str(input("Digite a sua frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print("Temos um Palíndromo")
else:
    print("A frase digitada não é um Palíndromo")