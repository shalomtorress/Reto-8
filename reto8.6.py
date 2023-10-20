n = int(input("Ingrese un número natural: "))
x = float(input("Ingrese un número real: "))
operacion = 1

for i in range(n-1):
  operacion *= x

print("El resultado es: " + str(operacion))