
try:
    numero = int(input("Introduce un número: "))
    print(f"Has introducido el número {numero}")
except ValueError:
    print("Error: eso no es un entero.")
