import single_player
import multiplayer
import os
import time


def menu():
    os.system('clear')
    choice = input("Welcome to Battleship!\nChoose from the options below:\n1: Single-player\n2: Multi\n3: Exit\n")
    if choice == "1":
        single_player.game_cycle()
    elif choice == "2":
        multiplayer.game_cycle()
    elif choice == "3":
        print("Good bye!")
        quit()
    else:
        os.system('clear')
        print("Invalid input!\nPlease type in an available option or it's number!")
        time.sleep(2)
        menu()
