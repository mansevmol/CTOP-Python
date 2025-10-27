texto = ""

try:
    f = open("archivo.txt","w")
    # texto = f.read()
    f.write("hola que hase")
except IOError as e:
    print("ocurrio un error")
else:
    print("Fichero escrito")
finally:
    f.close()
