import random

def generar_numero_secreto():
    """Genera un número secreto aleatorio entre 1 y 100."""
    return random.randint(1, 100)

def adivinar_numero():
    """Permite al usuario adivinar el número secreto."""
    intentos = 0
    numero_secreto = generar_numero_secreto()

    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        try:
            guess = int(input("Adivina el número: "))
            intentos += 1

            if guess == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
            elif guess < numero_secreto:
                print("Demasiado bajo. Intenta nuevamente.")
            else:
                print("Demasiado alto. Intenta nuevamente.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    adivinar_numero()
