import json
players = [
    {'id' : 1, 'yasashwi' : 'jaiswal'},
    {'id' : 2 , 'shubhman' : 'gill' },
    {'id' : 3 , 'dinesh' : 'karthik' },

]

print(players)
with open('player.json','w') as file:
    json.dump(players, file) 
with open('player.json','r') as reader:
    players_from_json = json.load(reader)
    print(players_from_json)