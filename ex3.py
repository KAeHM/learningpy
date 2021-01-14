import random    
matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
for numberl in range(0, 10):
    for numberc in range(0, 10):
        if numberl < numberc:
            result = 2 * numberl +  7 * numberc - 2
            matriz[numberl][numberc] = result
        elif numberl == numberc:
            result = 3 * (numberl ** 2) - 1
            matriz[numberl][numberc] = result
        elif numberl > numberc:
            result = 4 * (numberl ** 3) - 5 * (numberc ** 2) + 1
            matriz[numberl][numberc] = result
for numberl in range(0, 10):
    for numberc in range(0, 10):
        print(f'[{matriz[numberl][numberc]}]', end = ' ')
    print('\n')