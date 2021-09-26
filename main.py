import requests
import json

# just prepends the common url to a string
def url(short_url, api_included = True):
    if api_included:
        return "https://statsapi.web.nhl.com/api/v1{}".format(short_url)
    else:
        return "https://statsapi.web.nhl.com{}".format(short_url)

#get the list of games on the date given in the console args TODO
schedule = requests.get(url("/schedule?date=2019-06-12")).json()

#for now get the first game on that date and find its id
game_link = schedule["dates"][0]["games"][0]["link"]

game_data = requests.get(url(game_link, False)).json()

#print(json.dumps(game_data))
#create a dictionary of players active in the current game
players = {}
for player in game_data["gameData"]["players"]:
    player_data = game_data["gameData"]["players"][player]
    players[player_data["fullName"]] = player_data["id"]

player_name = "Ryan O'Reilly"

# now that we have a player, run through every shot in the game, if they belong to our player add them to the list
shots = []
for play in game_data["liveData"]["plays"]["allPlays"]:
    if (play["result"]["event"] == "Shot" or play["result"]["event"] == "Goal") and play["players"][0]["player"]["id"] == players[player_name]:
        print(play)
        print("")
    pass