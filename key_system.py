import uuid
import random
import colorama
import plyer
import time
import sys
import os
from datetime import datetime, timedelta
from time import sleep
from colorama import Fore, Back, Style
from VCSD import display_crosshair
from VCSD import edit_config

def clear():
    os.system('cls' if os.name == 'nt' else clear)
clear()

def Nuke_em():
    print()
    print(Fore.LIGHTRED_EX + "      __   __         _                              ")
    print(Fore.LIGHTRED_EX + "     |  \ |  |__   __| | ______     ____ _ __ _____  ")
    print(Fore.LIGHTRED_EX + "     |   \|  |  | |  | |/ /  _ \   /  _ \ '__`  __ \ ")
    print(Fore.LIGHTRED_EX + "     |  |\   |  |_|  |   <   __/  |   __/ |  | |  | |")
    print(Fore.LIGHTRED_EX + "     |__| \__|\___,__|_|\_\____|   \____|_|  |_|  |_|")
    print()

def keyboard_logo():
    print()
    print(Fore.LIGHTRED_EX + ",---,---,---,---,---,---,---,---,---,---,---,---,---,-------, ")
    print(Fore.LIGHTRED_EX + "|1/2| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | + | ' | <-    | ")
    print(Fore.LIGHTRED_EX + "|---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----| ") 
    print(Fore.LIGHTRED_EX + "| ->| | Q | W | E | R | T | Y | U | I | O | P | ] | ^ |     | ")
    print(Fore.LIGHTRED_EX + "|-----',--',--',--',--',--',--',--',--',--',--',--',--'|    | ")
    print(Fore.LIGHTRED_EX + "| Caps | A | S | D | F | G | H | J | K | L | \ | [ | * |    | ")
    print(Fore.LIGHTRED_EX + "|----,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'----| ")
    print(Fore.LIGHTRED_EX + "|    | < | Z | X | C | V | B | N | M | , | . | - |          | ")
    print(Fore.LIGHTRED_EX + "|----'-,-',--'--,'---'---'---'---'---'---'-,-'---',--,------| ")
    print(Fore.LIGHTRED_EX + "| ctrl |  | alt |                          |altgr |  | ctrl | ")
    print(Fore.LIGHTRED_EX + "'------'  '-----'--------------------------'------'  '------' ")
    print()

def prankem():
    print(Fore.LIGHTRED_EX +"  ____                  _                           _       _            ") 
    print(Fore.LIGHTRED_EX +" |  _ \ _ __ __ _ _ __ | | __   ___ _ __ ___       | | ___ | |__  _ __   ") 
    print(Fore.LIGHTRED_EX +" | |_) | '__/ _` | '_ \| |/ /  / _ \ '_ ` _ \   _  | |/ _ \| '_ \| '_ \  ")
    print(Fore.LIGHTRED_EX +" |  __/| | | (_| | | | |   <  |  __/ | | | | | | |_| | (_) | | | | | | | ")
    print(Fore.LIGHTRED_EX +" |_|   |_|  \__,_|_| |_|_|\_\  \___|_| |_| |_|  \___/ \___/|_| |_|_| |_| ")


def timedisplay():
    current_datetime= datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    print(Fore.YELLOW + "Current Date:", formatted_date)

print("Version 1")
timedisplay()

def helpmenu():
    print()
    print(Fore.MAGENTA + "Commands: ")
    print(Fore.MAGENTA + "START VCSD: Start, start, Start VCSD, start vcsd")
    print(Fore.MAGENTA + "CREDITS: Credits, credits, cred")
    print(Fore.MAGENTA + "CONFIG: Config, config, conf")
    print(Fore.MAGENTA + "HELP: Help, help, hel")
    print(Fore.MAGENTA + "EXIT: Exit, exit")
    print(Fore.MAGENTA + "----------------------------------------------------")
    print(Fore.MAGENTA + "Start starts the Crosshairs after you get your key"  )
    print(Fore.MAGENTA + "Credits shows the Creator and where to find him.    ")
    print(Fore.MAGENTA + "The Config option allows you to change between one"  )
    print(Fore.MAGENTA + "or 2 crosshairs. It also allows you to change color.")
    print(Fore.MAGENTA + "Help shows you all of this.")
    print(Fore.MAGENTA + "Exit exits the program.")
    print(Fore.MAGENTA + "----------------------------------------------------")
    print(Fore.MAGENTA + "You get your key fron the key.txt file in the dist. ")
    print(Fore.MAGENTA + "Dist is where you should always start file from."    )

def loading_bar(duration, steps = 20):
    for i in range(steps + 1):
        progress = i / steps
        bar_length = int(progress * 50)
        bar = "[" + "*" * bar_length + " " * (50 - bar_length) + "]"
        sys.stdout.write("\r" + bar + "{:.0%}".format(progress))
        sys.stdout.flush()
        sleep(duration / steps)

def generate_key():
    return str(uuid.uuid4())

def save_key(key, filename='key.txt'):
     with open(filename, 'w') as file:
        file.write(key)

functions_list = [Nuke_em, keyboard_logo, prankem]

def print_random_function():
    # Randomly select a function from the list
    random_function = random.choice(functions_list)
    
    # Call the selected function
    random_function()
random.seed()

generated_key = generate_key()
save_key(generated_key)
sleep(1)
print_random_function()
sleep(1)
print(Fore.RED + f"Generated Key: Found In key_XX.txt file")
loading_bar(3)

def is_valid_key(user_key, stored_key):
    return user_key == stored_key

key = generated_key

save_key(key, 'key.txt')

#Code for MENU
while True:
    print(Fore.GREEN + "\nMenu:")
    print(Fore.GREEN + "[+] Start VCSD")
    print(Fore.GREEN + "[+] Credits")
    print(Fore.GREEN + "[+] Config")
    print(Fore.GREEN + "[+] Help")
    print(Fore.GREEN + "[+] Exit")

    choice = input("Choose one (type it out): ")

    #Code for START, CREDITS, EXIT
    if choice in ["Start", "start", "Start VCSD", "start vcsd", "strt"]:
        user_provided_key = input(Fore.RED + "Enter your Key: ")
        if is_valid_key(user_provided_key, generated_key):
            print()
            print("Valid lifetime key")
            display_crosshair()
    elif choice in ["Config", "config", "conf",]:
        edit_config()
    elif choice in ["Credits", "credits", "cred"]:
        print()
        print(Fore.CYAN + "Made by Vibezys")
        print("GITHUB: https://github.com/Vibezys")
    elif choice in ["Help", "help", "hel"]:
        helpmenu()
    elif choice in ["Exit", "exit"]:
        sys.exit()
    else:
        print("Invalid Choice.")