numero_str = input("Por favor, ingresa un número entero positivo: ")
suma_digitos = 0
if numero_str.isdigit():
    for digito in numero_str:
        suma_digitos += int(digito)
    print(f"La suma de los dígitos es: {suma_digitos}")
else:
    print("Entrada no válida. Por favor, ingresa un número entero positivo.")