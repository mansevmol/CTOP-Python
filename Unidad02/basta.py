palabra = input("dame una palabra \n")
sumapalabra = palabra 
i = 1
while(palabra != "Basta"):
  i+=1
  palabra = input("dame una palabra\n")
  sumapalabra+= " "+palabra
  print(sumapalabra)

print(f"Has soportado estoicamente {i} preguntas")


"""
INICIO

  ESCRIBIR "Dame una palabra"
  LEER palabra

  sumapalabra <- palabra
  i <- 1

  MIENTRAS palabra ≠ "Basta" HACER
    i <- i + 1
    ESCRIBIR "Dame una palabra"
    LEER palabra
    sumapalabra <- sumapalabra + " " + palabra
    ESCRIBIR sumapalabra
  FIN MIENTRAS

  ESCRIBIR "Has soportado estoicamente ", i, " preguntas"

FIN

"""