import time as t
try:
  N = int(input("Introduce un número entre 5 y 50: "))
  
  if 5 <= N <= 50:
    print(f"\nCuenta atrás desde {N} hasta 1:")
    for i in range(N, 0, -1):
      print(i)
      t.sleep(0.5)
  else:
    print("Error: El número debe estar entre 5 y 50.")
except ValueError:
  print("Error: No has introducido un número válido.")
