# Reto-8
## Punto 1 
+ Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
````python
y = 1 
for y in range (1, 101):
    cuadrado = y**2
    print (y, y**2)
````
+ se declara la variable y para almacenar el numero atual
+ se utiliza el ````for```` para iterar en los numerosdel 1, 100, la lsta de numeros esta en ````range(1, 101)```` en este estan los njumeros del 1 al 100
+ en el bucle se calcula el cuadrado utilizando ````**```` y se almacena en la varable ````cuadrado````
  ## Punto 2
  +Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
````python
impares = []
for i in range(1, 1000):
    if i % 2 != 0:
        impares.append(i)

pares = []
for i in range(2, 1001):
    if i % 2 == 0:
        pares.append(i)

print("Números impares: "+ str(impares))

print("Números pares:" +str (pares))
````
+ se declaran las listas para almacenas los numeros pares e impares
+ Utilizamos ```` for```` para iterar sobre los números del 1 al 1000
+ dentro del bucle usamos una condicion para ver si el numero es impar ```` if i % 2 != 0:````
+ se agrega el numero a la lista utilizando ````impares.append(i)````
+ se hace lo mismo para sacar los pares esta vez usado ````if i % 2 == 0````
## Punto 3 
+ Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
```python
n = int(input("Ingrese un número mayor o igual a 2: "))
for i in range(n, 0, -1):
        if i % 2 == 0:
            print(i)
 ```
+ se le pide al usuario ingresar un numero igual omayor a dos
+  Declaramos una variable ````i```` para tener el numero actual, ````for```` itera sobre los números del n al 2.
+ Dentro del bucle usamos una condicion para ver si el numero es par ```if i % 2 == 0:```
## Punto 4
 + Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
````python
n = int(input("Ingrese un número: "))
for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        print(i, factorial)
````
+ se le pide al usuario ingresar un numero natural
+ se declara la variable ```i``` para almacenar el numero
+ El for itera los numeros desde 1 al n
+ Dentro del bucle calculamos la factorial usando ````factorial````
## Punto 5
+ Calcular el valor de 2 elevado a la potencia n usando ciclos for
````python
n = int(input("Ingrese la potencia: "))
resultado = 1
for i in range(n):
        resultado *= 2
        print(resultado)
````
+ Declaramos una variable ````resultado```` para almacenar el resultado.
+ el ```` for ```` para iterar sobre los números del 1 al n.
+ Dentro del bucle, multiplicamos el resultado por 2

## Punto 6 
+ Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**)

````python
n = int(input("Ingrese un número natural n: "))
x = float(input("Ingrese un numero  real x: "))
resultado = 1
for i in range(n):
        resultado *= x
print(resultado)
````
+ se solicita a el usuario ingresar los numeros n y x
+ Declaramos una variable resultado para almacenar el resultado.
+ se utiliza el ````for```` para iterar en los numeros de 1 a n
+ Dentro del bucle, multiplicamos el resultado por x, el resultado es igual al resultado anterior multiplicado por x
## Punto 7 
+ Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
````python
for i in range(1, 10):
    print("Tabla de multiplicar del: " + str(i))
    for j in range(1, 11):
        tabla = i * j
        print(str(i) + " x " + str(j) + " = " + str(tabla))
    print()
````
+ se impora math
+ se inicia con un bucle ````for```` que itera los numeros del 1 al 9
+ dentro del bucle for, se imprime un mensaje que indica qué tabla de multiplicar se está imprimiendo
+ se crea otro bucle for que itera sobre los números del 1 al 10.
+ Dentro del segundo bucle ````for````, se define una variable ````tabla```` que contiene el resultado de multiplicar el valor de ````i```` por el valor  de ````j````.
## Punto 8 
+ Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
````python

import math

def aproximar_funcion_exponencial(x, n):

  aproximacion = 1
  for i in range(1, n + 1):
    aproximacion += x ** i / math.factorial(i)

  return aproximacion

def main():
 
  x = float(input("Ingrese el valor de x: "))
 
  n = int(input("Ingrese el número de términos: "))
 
  aproximacion = aproximar_funcion_exponencial(x, n) 
  diferencia = math.exp(x) - aproximacion
 
  print("La aproximación de la función exponencial es:", aproximacion)
  print("La diferencia entre el valor real y la aproximación es:", diferencia)

if __name__ == "__main__":
  main()
````
+ Declaramos la función aproximar_funcion_exponencial(), la función aproximar_funcion_exponencial() recibe dos valores: el valor de x para el que se desea calcular la aproximación y el número de términos de la serie de Maclaurin que se utilizarán.
+ Calculamos la aproximación de la función exponencial utilizando la serie de Maclaurin,La serie de Maclaurin para la función exponencial es una suma infinita de términos, el primer término es 1, el segundo término es x, el tercer término es x^2 / 2!, y así sucesivamente.
+ Devolvemos la aproximación usando el ````return````
+ Definimos la función ````main()````
+ Ingresamos el valor de x para el que deseamos calcular la aproximación
## Punto 9 
+ Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
````python
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
````
+ se importa math
+  Declaramos la función aproximar_funcion_seno(), La función aproximar_funcion_seno() recibe dos valores: el valor de x para el que se desea calcular la aproximación y el número de términos.
+  La serie de Maclaurin para la función seno es una suma infinita de términos del tipo x^(2n - 1) / (2n - 1)!. El primer término es x, el segundo término es x^3 / 3!, el tercer término es x^5 / 5!, y así sucesivamente
+  se devuelve la prximacion utilizando el ````return````
+  Ingresamos el valor de x para el que deseamos calcular la aproximación.
## Punto 10
+ Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación
````python
import math

def aproximar_funcion_arctangente(x, n):

  aproximacion = x
  for i in range(2, n + 1, 2):
    aproximacion += x ** i / (i * (i + 1))

  return aproximacion


def main():
  
  x = float(input("Ingrese el valor de x: "))


  if x < -1 or x > 1:
    print("El valor de x debe estar en el rango [-1, 1].")
    return

  n = int(input("Ingrese el número de términos: "))

  aproximacion = aproximar_funcion_arctangente(x, n)

  diferencia = math.atan(x) - aproximacion

  print("La aproximación de la función arcotangente es:", aproximacion)
  print("La diferencia entre el valor real y la aproximación es:", diferencia)


if __name__ == "__main__":
  main()
````
+ se importa math
+ la funcion es iguala las de los puntos 8 y 9, recibe los valores x para el que se desea calcular la aproximación y el número de términos de la serie de Maclaurin que se utilizarán.
+ Calculamos la aproximación de la función arcotangente utilizando la serie de Maclaurin, arctan(x) = x - x^3/3 + x^5/5 - x^7/7 + ...
+ devolvemos la aproximacion +
+ ingresamos el valor de x para el deseamos calcular la aproximación.
