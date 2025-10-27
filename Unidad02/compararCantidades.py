
try:
  num1 = float(input("Introduce el primer número: "))
  num2 = float(input("Introduce el segundo número: "))

  if num1 > num2:
    print("El 1º es mayor que el 2º")
  elif num1 < num2:
    print("El 2º es mayor que el 1º")
  else:
    print("Ambos son iguales")
except ValueError:
  print("Error: No has introducido un valor de tipo numerico ")
