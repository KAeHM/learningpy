import random
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
for numberl in range(0, 3):
    for numberc in range(0, 3):
        matriz[numberl][numberc] = random.choice(numbers)
for l in range(0,2):
    for c in range(1, 3):
        soma += matriz[l][c]
        print(matriz[l][c])
for numberl in range(0, 3):
    for numberc in range(0, 3):
        print(f'[{matriz[numberl][numberc]}]', end = ' ')
    print('\n')
print(soma - matriz[1][1])
