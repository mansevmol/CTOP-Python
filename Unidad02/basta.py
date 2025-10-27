
palabra = input("dame una palabra \n")
sumapalabra = palabra 
i = 1
while(palabra != "Basta"):
  i+=1
  palabra = input("dame una palabra\n")
  sumapalabra+= " "+palabra
  print(sumapalabra)

print(f"Has soportado estoicamente {i} preguntas")