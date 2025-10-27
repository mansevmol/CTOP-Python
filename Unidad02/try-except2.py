import sys

lista = [1,2,3,4,5]

try:
    for l in lista:
        print(l)
except IndexError as e:
    print("Error: ",e)

else:
    print("finalizo sin errores")
finally:
    sys.exit()
