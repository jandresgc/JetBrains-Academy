
# Método-1
print([i for i in range(2, 20) if all(i % j != 0 for j in range(2, i-1))])

# Método-2
for i in range(2, 20):
    cont = 0
    for j in range(2, i-1):
        if i % j == 0:
            cont += 1
            break
    if cont == 0:
        print(i, end = " ")