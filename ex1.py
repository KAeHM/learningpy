import random
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for numberl in range(0, 4):
    for numberc in range(0, 4):
        matriz[numberl][numberc] = input(f'linha: {numberl}\ncoluna {numberc}\ndigite: ')
for numberl in range(0, 4):
    for numberc in range(0, 4):
        print(f'[{matriz[numberl][numberc]}]', end = ' ')
    print('\n')