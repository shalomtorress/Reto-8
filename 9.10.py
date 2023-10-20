import math

def aproximar_funcion_arctangente(x, n):
  """
  Aproxima la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin.

  Args:
    x: El valor de x para el que se desea calcular la aproximación.
    n: El número de términos de la serie de Maclaurin que se utilizarán.

  Returns:
    La aproximación de la función arcotangente para el valor x.
  """

  # La serie de Maclaurin para la función arcotangente es:
  #
  # arctan(x) = x - x^3/3 + x^5/5 - x^7/7 + ...

  aproximacion = x
  for i in range(2, n + 1, 2):
    aproximacion += x ** i / (i * (i + 1))

  return aproximacion


def main():
  # Ingresamos el valor de x para el que deseamos calcular la aproximación.
  x = float(input("Ingrese el valor de x: "))

  # Validamos que el valor de x esté en el rango [-1, 1].

  if x < -1 or x > 1:
    print("El valor de x debe estar en el rango [-1, 1].")
    return

  # Ingresamos el número de términos de la serie de Maclaurin que deseamos utilizar.
  n = int(input("Ingrese el número de términos: "))

  # Calculamos la aproximación de la función arcotangente.
  aproximacion = aproximar_funcion_arctangente(x, n)

  # Calculamos la diferencia entre el valor real y la aproximación.
  diferencia = math.atan(x) - aproximacion

  # Imprimimos la aproximación y la diferencia.
  print("La aproximación de la función arcotangente es:", aproximacion)
  print("La diferencia entre el valor real y la aproximación es:", diferencia)


if __name__ == "__main__":
  main()