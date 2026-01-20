estudiantes = ["Ana", "Luis", "Marta"]

print("Lista inicial de estudiantes:", estudiantes)

nuevo_alumno = input("Introduce el nombre de un nuevo alumno: ")
estudiantes.append(nuevo_alumno)

alumno_a_eliminar = input("Introduce el nombre del alumno a eliminar: ")
if alumno_a_eliminar in estudiantes:
  estudiantes.remove(alumno_a_eliminar)
else:
  print(f"El alumno {alumno_a_eliminar} no está en la lista.")

estudiantes.sort()

print("Lista actualizada de estudiantes:", estudiantes)

calificaciones = {
  "Ana": 8.0,
  "Luis": 7.0,
  "Marta": 9.1
}

nombre = input("Introduce el nombre del alumno para añadir/actualizar nota: ")
try:
  nota = float(input(f"Introduce la nota de {nombre} (0-10): "))
except ValueError :
  print("Nita un numero")
else:
  if 0 <= nota <= 10:
    calificaciones[nombre] = nota
  else:
    print("Nota inválida, debe ser entre 0 y 10.")

print("\nListado de alumnos y sus calificaciones:")
for alumno, nota in calificaciones.items():
  print(f"{alumno} - {nota}")

if calificaciones:
  promedio = sum(calificaciones.values()) / len(calificaciones)
  print(f"\nLa nota media de la clase es: {promedio:.2f}")
else:
  print("No hay calificaciones para calcular la media.")

archivo = "alumnos.txt"
with open(archivo, "w") as f:
  for alumno, nota in calificaciones.items():
    f.write(f"{alumno} - {nota}\n")

print(f"\nInformación guardada en el archivo '{archivo}' correctamente.")
