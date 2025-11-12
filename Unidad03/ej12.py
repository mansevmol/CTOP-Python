def calcular_media(num1, num2):

  return (num1 + num2) / 2


def calcular_mediaPro(*args):
  suma = 0
  for n in args:
    suma +=n
  return suma/len(args)

print(calcular_media(1,2))

print(calcular_mediaPro(10,5,10,5))

