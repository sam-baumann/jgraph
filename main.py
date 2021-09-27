import requests
import sys

# just prepends the common url to a string
def url(short_url, api_included = True):
    if api_included:
        return "https://statsapi.web.nhl.com/api/v1{}".format(short_url)
    else:
        return "https://statsapi.web.nhl.com{}".format(short_url)

if len(sys.argv) != 3:
    print("bad number of args")
    exit(1)

#date = "2021-09-25"
date = sys.argv[1]
#player_name = "James Neal"
player_name = sys.argv[2]

#get the list of games on the date given in the console args TODO
schedule = requests.get(url("/schedule?date={}".format(date))).json()

# now get the game based on the player's name given. This won't always work if two players have the same name but there aren't any current players that have the same name as far as I know
game_link = None
game_data = None
for game in schedule["dates"][0]["games"]:
    #for the current game, get its link and run through its player link
    temp_game_link = game["link"]
    temp_game_data = requests.get(url(temp_game_link, False)).json()
    for player in temp_game_data["gameData"]["players"]:
        player_data = temp_game_data["gameData"]["players"][player]
        if player_data["fullName"] == player_name:
            game_link = temp_game_link
            game_data = temp_game_data
            break
    if not game_link is None:
        break

#if we don't have game data now, we have a bad input or something else
if game_data is None:
    print("wrong input!")
    exit(1)
            
#create a dictionary of players active in the current game
players = {}
for player in game_data["gameData"]["players"]:
    player_data = game_data["gameData"]["players"][player]
    players[player_data["fullName"]] = player_data["id"]

# now that we have a player, run through every shot in the game, if they belong to our player add them to the list
shots = []
goals = []
for play in game_data["liveData"]["plays"]["allPlays"]:
    if play["result"]["event"] == "Shot" and play["players"][0]["player"]["id"] == players[player_name]:
        shots.append(play)
    elif play["result"]["event"] == "Goal" and play["players"][0]["player"]["id"] == players[player_name]:
        goals.append(play)

# now that we have the list of shots, we can begin jgraph output
print("newgraph")
print("xaxis min 0 max 100")
print("size 5")
print("yaxis min -43 max 43")
print("size 4.25")
# goal outline
print("newline pts 89 3 92.3 3 92.3 -3 89 -3")
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

if len(shots) > 0:
    print("newcurve pts")
    for shot in shots:
        if shot["coordinates"]["x"] < 0:
            print("{} {}".format(-int(shot["coordinates"]["x"]), -int(shot["coordinates"]["y"])))
        else:
            print("{} {}".format(int(shot["coordinates"]["x"]), int(shot["coordinates"]["y"])))
if len(goals) > 0:
    print("newcurve color 1 0 0 pts")
    for shot in goals:
        if shot["coordinates"]["x"] < 0:
            print("{} {}".format(-int(shot["coordinates"]["x"]), -int(shot["coordinates"]["y"])))
        else:
            print("{} {}".format(int(shot["coordinates"]["x"]), int(shot["coordinates"]["y"])))
print("title : Shot selection by {} on {}.".format(player_name, date))
print("newstring hjl x 27 y 40 : Goals are marked in red, all markings are in feet")