import random
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for numberl in range(0, 4):
    for numberc in range(0, 4):
<<<<<<< HEAD
        matriz[numberl][numberc] = random.choice(numbers)
=======
        matriz[numberl][numberc] = random.choice(numbers) # Manually or not 
>>>>>>> f6fc8256f7670680c38ac8f0824d2bdb0a578e73
for numberl in range(0, 4):
    for numberc in range(0, 4):
        print(f'[{matriz[numberl][numberc]}]', end = ' ')
    print('\n')
