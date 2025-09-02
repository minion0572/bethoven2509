players = [
    {'id' : 101, 'yasashwi' : 'jaiswal'},
    {'id' : 102 , 'shubhman' : 'gill' }
]
print(players)
player = {}
player['id'] = 103
player['name'] = 'abhisek'
print(players)

players.append(player)
print(players)

for player in players:
    if player['id'] == 103:
        print(player)

player_dict = {101:players[0],102:players[1],103:players[2]}
print(player_dict)