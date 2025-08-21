frase = "programacion es divertida"
contador_vocales = 0
vocales = "aeiou"

for caracter in frase.lower():
    if caracter in vocales:
        contador_vocales += 1

print(f"La cantidad total de vocales en la frase es: {contador_vocales}")