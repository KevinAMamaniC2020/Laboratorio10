def calcular_cuadrado(numero):
    # Función para calcular el cuadrado de un número
    return numero ** 2

def calcular_cubo(numero):
    # Función para calcular el cubo de un número
    return numero ** 3

def calcular_promedio(lista_numeros):
    # Función para calcular el promedio de una lista de números
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)

def procesar_datos(datos):
    # Función principal para procesar datos
    resultado = 0
    for dato in datos:
        if dato > 0:
            resultado += calcular_cuadrado(dato)
        elif dato < 0:
            resultado += calcular_cubo(dato)
        else:
            resultado += dato
    return resultado

def main():
    # Función principal del programa
    datos = [1, 2, 3, -1, -2, -3, 0]
    resultado = procesar_datos(datos)
    print(f"El resultado final es: {resultado}")

if __name__ == "__main__":
    main()
