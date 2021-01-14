import random
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for numberl in range(0, 4):
    for numberc in range(0, 4):
        if numberl == numberc:
            matriz[numberl][numberc] = 1
        else:
            matriz[numberl][numberc] = 0
for numberl in range(0, 4):
    for numberc in range(0, 4):
        print(f'[{matriz[numberl][numberc]}]', end = ' ')
    print('\n')