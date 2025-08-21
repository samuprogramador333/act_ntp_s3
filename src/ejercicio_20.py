edad_maxima = -1
edad = 0

print("Ingresa edades una a una. Para terminar, ingresa -1.")

while edad != -1:
    try:
        edad = int(input("Ingresa una edad: "))
        if edad > edad_maxima and edad != -1:
            edad_maxima = edad
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")

if edad_maxima == -1:
    print("No se ingresaron edades válidas.")
else:
    print(f"La edad mayor ingresada es: {edad_maxima}")