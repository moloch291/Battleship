import single_player


def menu():
    choice = input("Welcome to Battleship!\nChoose from the options below:\n1: Single-player\n2: Multi\n3: Exit\n")
    if choice == "1":
        single_player.game_cycle()
    elif choice == "2":
        multiplayer.game_cycle()
    elif choice == "3":
        print("Good bye!")
        quit()
