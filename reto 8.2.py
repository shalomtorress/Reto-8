
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

