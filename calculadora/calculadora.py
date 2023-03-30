def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

while True:
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 5:
        print("¡Adiós!")
        break

    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Por favor, ingrese números válidos")
        continue

    if opcion == 1:
        resultado = sumar(num1, num2)
    elif opcion == 2:
        resultado = restar(num1, num2)
    elif opcion == 3:
        resultado = multiplicar(num1, num2)
    elif opcion == 4:
        try:
            resultado = dividir(num1, num2)
        except ValueError as e:
            print(e)
            continue

    print("El resultado es: ", resultado)
