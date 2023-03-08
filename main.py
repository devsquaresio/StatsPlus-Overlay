VERSION=0.53


delay = 0.05


# Demo: Basic stats features, grabs everyone in games
# Modules
try:
    import os
    import time
    import json
    import sys
    import tkinter
    import logging

    os.system('cls' if os.name == 'nt' else 'clear')

    logging.basicConfig(level=logging.DEBUG, format="{asctime} {levelname:<8} {message}", style='{', filename='debug.log', filemode='a')

    def install_package(pk):
        os.system(f"{sys.executable} -m pip install {pk}")

    try:
        import requests
    except ModuleNotFoundError:
        install_package("requests")
        import requests

    try:
        from pathlib import Path as Pathlib
    except ModuleNotFoundError:
        install_package ("pathlib")
        from pathlib import Path as Pathlib

    try:
        import customtkinter as ctk
    except ModuleNotFoundError:
        install_package("customtkinter")
        import customtkinter as ctk

except:
    print("There was an error importing the required libraries. The program will most likely encounter errors.")
    logging.critical("PACKAGES WEREN'T ABLE TO BE IMPORTED PROPERLY")


os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(2)
print('DONT CHANGE THE NAME OF ANY OF THE FILES!')
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(2)


# Auto-Update, Add EXE later...
# Thanks kopamed for this
latest_overlay_code = requests.get("https://raw.githubusercontent.com/devsquaresio/StatsPlus-Overlay/main/main.py")
if latest_overlay_code.status_code == 200:
    latest_overlay_code = latest_overlay_code.text
    latest_version = float(latest_overlay_code.split("\n")[0].split("=")[-1])
    if latest_version > VERSION:
        print(f"An update is available. {VERSION} -> {latest_version}.Update? [y/n]")
        u = input("> ")
        if "n" not in u.lower():
            with open("main.py", "w") as f:
                f.write(latest_overlay_code)
            time.sleep(1)
            print("Update complete! Re-run the app.")
            logging.info(f"Updated. {VERSION} -> {latest_version}")
            input()
        else:
            print("Ignored update.")
            logging.debug(f"Update version {latest_version} ignored.")



time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')


print("Welcome to the Stats+ Bedwars Overlay!")
# Get paths
badlion_client_path = "C:\Program Files\Badlion Client\\"
lunar_client_path = str(Pathlib.home()) + "\.lunarclient"
vanilla_client_path = str(Pathlib.home()) + "\AppData\Roaming\.minecraft"
bd_logs = str(Pathlib.home()) + "\AppData\Roaming\.minecraft\logs\\blclient\minecraft\latest.log"
lunar_logs = str(Pathlib.home()) + "\.lunarclient\offline\multiver\logs\latest.log"
vn_logs = str(Pathlib.home()) + "\AppData\Roaming\.minecraft\logs\latest.log"
olunar_logs = str(Pathlib.home()) + "\.lunarclient\offline\logs\latest.log"
confirmed_clients = []
confirmed_logs = []

# Basic debug feature 
def arr_to_str(array: list) -> str:
    value = ""
    for element in array:
        value += element
        if array.index(element) != (len(array) - 1):
            value += ", "
    
    return value

# Check if clients exist, need for users not meant for my purposes
def check_clients(empty_client_list: list) -> list:
    global badlion_client_path
    global lunar_client_path
    global vanilla_client_path
    if os.path.exists(badlion_client_path):
        empty_client_list.append("Badlion")
    if os.path.exists(lunar_client_path):
        empty_client_list.append("Lunar")
    if os.path.exists(vanilla_client_path):
        empty_client_list.append("Vanilla")

def check_logs(empty_client_list: list) -> list:
    global bd_logs
    global lunar_logs
    global vn_logs
    if os.path.exists(bd_logs):
        empty_client_list.append("Badlion")
        logging.debug("Badlion client found on computer.")
    if os.path.exists(lunar_logs):
        empty_client_list.append("Lunar")
        logging.debug("Lunar client found on computer.")
    if os.path.exists(olunar_logs):
        empty_client_list.append("Lunar")
        logging.debug("Lunar client found on computer.")
    if os.path.exists(vn_logs):
        empty_client_list.append("Vanilla")
        logging.debug("Regular Minecraft found on computer.")


# Thanks kopamed
def fix_line(line):
    return line.split("] ")[-1].strip("\n")


check_clients(confirmed_clients)
check_logs(confirmed_logs)

print("Clients found on computer: " + arr_to_str(confirmed_clients))
print("Game files found on the computer: " + arr_to_str(confirmed_logs) + "\n")
print("Which client are you playing on?")
print("[1] Badlion")
print("[2] Lunar")
print("[3] Vanilla")
print("[4] Custom")

client_choice = input("> ")

if client_choice == "1":
    if os.path.exists(bd_logs):
        path = bd_logs
        logging.debug("Badlion client logs had been added")
    else:
        print("Log not found")
        logging.error("Badlion client not found on computer.")
    
elif client_choice == "2":

    if os.path.exists(lunar_logs):
        path = lunar_logs
        logging.debug("Lunar client logs had been added")
    elif os.path.exists(olunar_logs):
        path = olunar_logs
        logging.debug("Lunar client logs had been added")
    else:
        print("Log not found")
        logging.error("Lunar client logs not found on computer.")

elif client_choice == "3":
    if os.path.exists(vn_logs):
        path = vn_logs
        logging.debug("Regular Minecraft logs had been added")
    else:
        print("Log not found")
        logging.error("Vanilla client logs not found on computer.")

elif client_choice == "4":
    # Check until the path exists
    while True:
        print("Enter custom client log path")
        log_path = input("> ")
        if os.path.exists(log_path):
            print("Log Found!")
            logging.info("Logs found on computer.")
            break
        else:
            print("Log not found. Try again!\n")
            logging.warning("Log not found.")
    path = log_path


time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
# Todo: Add random tips later
print("TIP: Don't give your API Key to anyone...")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')


# If file exists but empty, then ask to give api key
if os.path.exists("apikey.txt"):
    with open("apikey.txt", "r") as f:
        api_key = f.read()
        #print(api_key)
        if api_key == "":
            print(r"Api Key NOT found. Type /api new.")
            logging.error("Api key not found")
            # keeps reading until api key found
            while True:
                with open(path, "r") as h:
                    latest_line = fix_line(h.readlines()[-1])
                    if latest_line.startswith("Your new API key is"):
                        api_key = latest_line.split(" ")[-1]
                        with open("apikey.txt", "w") as i:
                            i.write(api_key)
                            print("Api Key found. Join a game of bedwars to try the overlay!")
                            logging.info("Api key found")
                            break
                time.sleep(delay)
        else:
            print("Api Key found. Join a game of bedwars to try the overlay!")
            logging.info("Api Key saved in file already")


# If file doesn't exist, then create it and ask to give api key
else:
    with open("apikey.txt", "x") as f:
        print(r"Api Key NOT found. Type /api new.")
        logging.error("Api key not found")
        while True:
            with open(path, "r") as i:
                latest_line = fix_line(i.readlines()[-1])
                if latest_line.startswith("Your new API key is"):
                    api_key = latest_line.split(" ")[-1]
                    with open("apikey.txt", "w") as j:
                        j.write(api_key)
                        print("Api Key found. Join a game of bedwars to try the overlay!")
                        logging.info("Api key found")
                        break
            time.sleep(delay)
    
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
# ADD MORE TIPS
print("TIP: Turn on AutoWho mod on Lunar and Badlion. Or, do /who everytime you join for Vanilla\n(NOT MORE THAN ONCE!)")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')


print("Join a game to start the overlay!")


readlen = 0
# Get length of file
with open(path, "r") as f:
    readlen = len(f.readlines())

queue = []

player_list = {}

def update_stats(queue, player_list, api_key):
    os.system('cls' if os.name == 'nt' else 'clear')
    for player in queue:
        # Added player dictionary to help speed up instead of making a request every single time queue updates
        if player in player_list:
            data = player_list[player]
            # check if invalid
            if data == "NULL":
                print(f'{player}: UNABLE TO FETCH STATS')
                logging.debug(f"Unable to fetch stats for {player}")
            # Check if nick
            elif data == "NICKED":
                print(f'{player}: NICKED')
            else:
                print(f"[{data[0]}]{player}, {data[1]}: [WINSTREAK: {data[2]}], [WLR: {data[3]}], [KDR: {data[4]}], [FKD: {data[5]}]")
        else:
            url = f'https://api.mojang.com/users/profiles/minecraft/{player}?'
            # Get uuid
            response = s.get(url)
            # Tells that player does not exist
            if response.status_code == 204:
                print(f"{player}: NICKED")
                player_list[player] = "NICKED"
                logging.debug(f"{player} was nicked.")
            else:
                try:
                    uuid = response.json()['id']
                    logging.debug(f"{player} has uuid {uuid}")
                    # Use api key to help grab data
                    requestlink = str(f"https://api.hypixel.net/player?key={api_key}&uuid=" + uuid)
                    hydata = s.get(requestlink).json()
                    # Self-Explanatory
                    lvl = int(hydata['player']['achievements']['bedwars_level'])
                    wins = int(hydata['player']['stats']['Bedwars']['wins_bedwars'])
                    losses = int(hydata['player']['stats']['Bedwars']['losses_bedwars'])
                    kills = int(hydata['player']['stats']['Bedwars']['kills_bedwars'])
                    deaths = int(hydata['player']['stats']['Bedwars']['deaths_bedwars'])
                    winstreak = int(hydata['player']['stats']['Bedwars']['winstreak'])
                    final_kills = int(hydata['player']['stats']['Bedwars']['final_kills_bedwars'])
                    final_deaths = int(hydata['player']['stats']['Bedwars']['final_deaths_bedwars'])
                    if losses == 0: wl = wins
                    else: wl = round(wins/losses, 2)
                    
                    if deaths == 0: kd = kills
                    else: kd = round(kills/deaths, 2)
                    if final_deaths == 0: fkd = final_kills
                    else: fkd = round(final_kills/final_deaths, 2)
                    
                    try: # Check if has mvp++
                        rank = hydata['player']['monthlyPackageRank']
                    except KeyError:
                        try: # Check if it has rank
                            rank = hydata['player']["newPackageRank"]
                        except KeyError: # Then non
                            rank = "NON"
                    if str(rank) == "NONE": # Confirming
                        rank = "NON"
                    # Better formatting
                    if str(rank) == "VIP_PLUS":
                        rank = "VIP+"
                    elif str(rank) == "MVP_PLUS":
                        rank = "MVP+"
                    elif (str(rank) == "SUPERSTAR"):
                        rank = "MVP++"
                    player_list[player] = [rank, lvl, winstreak, wl, kd, fkd] # Makes it easy to grab data
                    print(f"[{rank}]{player}, {lvl}: [WINSTREAK: {winstreak}], [WLR: {wl}], [KDR: {kd}], [FKD: {fkd}]")
                    logging.debug(f"Stats for {player} were given.")
                    # Todo: Add more things like party                
                except:
                    player_list[player] = "NICK"
                    print(f"{player}: NICKED")
                    logging.debug(f"{player} was NICKED.")
        
# File Reader
while True:
    new_lines = []
    s = requests.Session()
    with open(path, "r") as f:
        try:
            latest_line = fix_line(f.readlines()[readlen])
            if " has quit!" in latest_line: # Check if player left
                name = latest_line.split(" ")[0]
                logging.debug(f"{name} has left the bedwars lobby")
                queue.remove(name)
                update_stats(queue, player_list, api_key)
            elif latest_line.lower().startswith("online: "): # /who SHOULD ONLY BE RAN ONCE
                queue.clear()
                player_list = {}
                for player in latest_line.strip("ONLINE: ").split(", "):
                    queue.append(player)
                logging.debug("New game has started")
                
                update_stats(queue, player_list, api_key)
            elif " has joined" in latest_line.lower(): # Check if player joined
                name = latest_line.split(" ")[0]
                if name not in queue:
                    queue.append(name)
                logging.debug(f"{name} joined the bedwars lobby")
                update_stats(queue, player_list, api_key)
            elif "protect your bed and destroy the enemy beds." in latest_line.lower():
                # Todo: Handle minimization
                pass
            elif "has disconnected" in latest_line: # Check if player left mid-game idk why
                name = latest_line.split(" ")[0]
                queue.remove(name)
                logging.debug(f"{name} left in the middle of the game")
                update_stats(queue, player_list, api_key)
            elif "reconnected" in latest_line: # Check if player left mid-game idk why
                name = latest_line.split(" ")[0]
                queue.append(name)
                logging.debug(f"{name} rejoined in the middle of the game")
                update_stats(queue, player_list, api_key)
            
            elif latest_line.startswith("Your new API key is"): # Check if player changed api-key midway
                api_key = latest_line.split(" ")[-1]
                with open("apikey.txt", "w") as f:
                    f.write(api_key)
                logging.info(f"{name} new API key found!")
            readlen += 1

        except:
            pass # just doesn't work? 
        
        
    time.sleep(delay) # Todo: Add config file and be able to change settings

