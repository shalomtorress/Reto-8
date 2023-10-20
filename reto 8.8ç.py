import math

def aproximar_funcion_exponencial(x, n):
  """
  Aproxima la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin.

  Args:
    x: El valor de x para el que se desea calcular la aproximación.
    n: El número de términos de la serie de Maclaurin que se utilizarán.

  Returns:
    La aproximación de la función exponencial para el valor x.
  """

  # La serie de Maclaurin para la función exponencial es:
  #
  # e^x = 1 + x + x^2/2! + x^3/3! + ...

  aproximacion = 1
  for i in range(1, n + 1):
    aproximacion += x ** i / math.factorial(i)

  return aproximacion


def main():
  # Ingresamos el valor de x para el que deseamos calcular la aproximación.
  x = float(input("Ingrese el valor de x: "))

  # Ingresamos el número de términos de la serie de Maclaurin que deseamos utilizar.
  n = int(input("Ingrese el número de términos: "))

  # Calculamos la aproximación de la función exponencial.
  aproximacion = aproximar_funcion_exponencial(x, n)

  # Calculamos la diferencia entre el valor real y la aproximación.
  diferencia = math.exp(x) - aproximacion

  # Imprimimos la aproximación y la diferencia.
  print("La aproximación de la función exponencial es:", aproximacion)
  print("La diferencia entre el valor real y la aproximación es:", diferencia)


if __name__ == "__main__":
  main()
