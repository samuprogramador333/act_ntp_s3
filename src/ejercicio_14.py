import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 10)
    adivinado = False

    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número entre el 1 y el 10.")
    
    while not adivinado:
        try:
            intento = int(input("Adivina el número: "))
            
            if intento < numero_secreto:
                print("¡Demasiado bajo! Intenta de nuevo.")
            elif intento > numero_secreto:
                print("¡Demasiado alto! Intenta de nuevo.")
            else:
                adivinado = True
                print(f"¡Felicitaciones! ¡Adivinaste el número! El número era {numero_secreto}.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

adivina_el_numero()