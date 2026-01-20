# TUTORIAL – ESTRUCTURAS DE DATOS EN PYTHON (CLI)

## EJERCICIO 1 – Listas

Crea una lista con 5 números enteros:

numeros = [1, 2, 3, 4, 5]

Añade un número al final

numeros.append(6)

Elimina el último número

numeros.pop()

Muestra solo los 3 primeros elementos

print(numeros[:3])

## EJERCICIO 2 – Listas

Dada una lista de nombres, comprueba si "Ana" está en la lista.

nombres = ["Luis", "Ana", "Pedro", "Marta"]

if "Ana" in nombres:

print("Ana está en la lista")

else:

print("Ana no está en la lista")

## EJERCICIO 3 – Tuplas

Crea una tupla con 4 colores y:

colores = ("azul", "verde", "rojo", "amarillo")

Accede al segundo color

print(colores[1])

Comprueba si "rojo" está en la tupla

print("rojo" in colores)

## EJERCICIO 4 – Tuplas

Intenta modificar un elemento de la tupla.
👉 Observa el error y entiende por qué ocurre.

colores[0] = "negro"
TypeError: 'tuple' object does not support item assignment

## EJERCICIO 5 – Arrays

Crea un array de enteros y:
from array import array

nums = array('i', [1, 2, 3, 4])

Cambia el valor del primer elemento

nums[0] = 10

Intenta asignar un valor de tipo incorrecto

nums[1] = "hola"

## EJERCICIO 6 – Diccionarios

Crea un diccionario con información de una persona:

nombre
edad

persona = {
"nombre": "Carlos",
"edad": 30
}

Luego, añade la clave "ciudad"

persona["ciudad"] = "Madrid"

Elimina la clave "edad"

del persona["edad"]

## EJERCICIO 7 – Diccionarios

Recorre el diccionario anterior e imprime las claves y valores.
for clave, valor in persona.items():
print(clave, ":", valor)

## EJERCICIO 8 – Pila (stack)

Simula una pila usando una lista:

pila = []

Añade 3 números

pila.append(1)

pila.append(2)

pila.append(3)

Elimina el último

pila.pop()

Muestra la pila final

print(pila)

## EJERCICIO 9 – Cola (queue)

Simula una cola usando deque:

from collections import deque
cola = deque()
Añade 3 elementos

cola.append("a")
cola.append("b")
cola.append("c")

Elimina el primero

cola.popleft()

Muestra la cola resultante

print(cola)

append() → añadir
popleft() → quitar el primero

## EJERCICIO 10 – Extra

Dada una lista de números:

nums = [4, 7, 1, 9, 2]

- Ordénala
  nums.sort()
- Obtén el valor máximo
  max(nums)
- Obtén el valor mínimo
  min(nums)
