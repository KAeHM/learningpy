#vars
cmd = True
players = []
oneplayers = []
allvotes = []
cont = 0
qtyvotes = 0
a = 0

# main program
while cmd:
    player = int(input('Choose your favorite player: '))
    if player == 0:
        cmd = False
    else:
        if player >= 1 and player <= 23:
            if player in oneplayers:
                players.append(player)
            else:
                players.append(player)
                oneplayers.append(player)

# logic of result
for p in players:
    votes = players.count(p)
    if p != a:
        allvotes.append(votes)
    qtyvotes += 1
    a = p

# output of result
for p in oneplayers:
    print(f'Player: {p}')
    print(f'Votes: {allvotes[cont]}')
    print(f'% {(allvotes[cont] / qtyvotes) * 100}')
    cont += 1

# Winner
higher = max(allvotes)
winner = allvotes.index(higher)
print(f'The winner is the {oneplayers[winner]}') 
    
