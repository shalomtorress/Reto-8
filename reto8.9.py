import math

def aproximar_funcion_seno(x, n):
 
  aproximacion = x
  for i in range(2, n + 1, 2):
    aproximacion += (-1)**(i - 1) * x ** i / math.factorial(i)

  return aproximacion


def main():
  x = float(input("Ingrese el valor de x: "))
  n = int(input("Ingrese el número de términos: "))
  aproximacion = aproximar_funcion_seno(x, n)

  diferencia = math.sin(x) - aproximacion

  print("La aproximación de la función seno es:", aproximacion)
  print("La diferencia entre el valor real y la aproximación es:", diferencia)


if __name__ == "__main__":
  main()
