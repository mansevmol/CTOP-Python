
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


# INICIO

#     INTENTAR
#         ESCRIBIR "Introduce el primer número: "
#         LEER num1

#         ESCRIBIR "Introduce el segundo número: "
#         LEER num2

#         CONVERTIR num1 y num2 A NÚMERO (REAL)

#         SI num1 > num2 ENTONCES
#             ESCRIBIR "El 1º es mayor que el 2º"
#         SINO SI num1 < num2 ENTONCES
#             ESCRIBIR "El 2º es mayor que el 1º"
#         SINO
#             ESCRIBIR "Ambos son iguales"
#         FIN SI

#     CAPTURAR ERROR DE TIPO (ValueError)
#         ESCRIBIR "Error: No has introducido un valor de tipo numérico"

# FIN