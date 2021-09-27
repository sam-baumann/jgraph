import requests
import json

# just prepends the common url to a string
def url(short_url, api_included = True):
    if api_included:
        return "https://statsapi.web.nhl.com/api/v1{}".format(short_url)
    else:
        return "https://statsapi.web.nhl.com{}".format(short_url)

date = "2019-06-12"

#get the list of games on the date given in the console args TODO
schedule = requests.get(url("/schedule?date={}".format(date))).json()

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
        shots.append(play)

# now that we have the list of shots, we can begin jgraph output
print("newgraph")
print("xaxis min 0 max 100")
print("size 5")
print("yaxis min -43 max 43")
print("size 4.25")
# Draw the center red line
print("newcurve pts 0 -43 0 43")
print("color 1 0 0")
print("marktype xbar")
# now draw the end red line
print("newline pts 89 -36 89 36")
print("color 1 0 0")
print("linethickness 5")
# now draw the blue line
print("newcurve pts 25 -43 25 43")
print("color 0 0 1")
print("marktype xbar")
#draw around the rink
print("newline pts 0 43 72 43")
print("linethickness 5")
print("newline pts 0 -43 72 -43")
print("linethickness 5")
print("newline pts 100 -14.5 100 14.5")
print("linethickness 5")
#these are for the corners. They are just going to have to be an approximation because I don't really understand the bezier curve math and there are very few shots taken from this part of the rink anyway
print("newline bezier pts 72 -43 86 -43 100 -28.75 100 -14.5")
print("linethickness 5")
print("newline bezier pts 72 43 86 43 100 28.75 100 14.5")
print("linethickness 5")

print("newline pts 89 3 92.3 3 92.3 -3 89 -3")

for shot in shots:
    if shot["coordinates"]["x"] < 0:
        print("newcurve pts {} {}".format(-int(shot["coordinates"]["x"]), -int(shot["coordinates"]["y"])))
    else:
        print("newcurve pts {} {}".format(int(shot["coordinates"]["x"]), int(shot["coordinates"]["y"])))
    if shot["result"]["event"] == "Goal":
        print("color 1 0 0")
print("title : Shot selection for {} on {}".format(player_name, date))