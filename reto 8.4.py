n = int(input("Ingrese un número: "))
for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        print(i, factorial)
