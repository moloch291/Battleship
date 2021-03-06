import multiplayer_functions
import os
import time


def create_player_profiles():
    os.system('clear')
    print("Creating player profiles.")
    time.sleep(0.25)
    os.system('clear')
    print("Creating player profiles..")
    time.sleep(0.25)
    os.system('clear')
    print("Creating player profiles...")
    time.sleep(0.25)


def get_players():
    print("Player 1:")
    player1 = multiplayer_functions.get_name()
    print("Player 2:")
    player2 = multiplayer_functions.get_name()
    players = [player1, player2]
    print("Welcome " + player1 + " and " + player2 + "!\nLet's play!")
    time.sleep(2)
    return players


def get_tables():
    player1_table = multiplayer_functions.create_table()
    player2_table = multiplayer_functions.create_table()
    tables = [player1_table, player2_table]
    return tables


def get_ships():
    player1_ships = multiplayer_functions.create_ships()
    player2_ships = multiplayer_functions.create_ships()
    ships = [player1_ships, player2_ships]
    return ships


def get_locations(players, ships, tables):
    os.system('clear')
    print("Placing ships on the table... " + players[0] + " only!\n(Enemy shouldn't look...)")
    time.sleep(3)
    player1_table = get_ship_locations(players[0], ships[0], tables[0])
    os.system('clear')
    print("Placing ships on the table... " + players[1] + " only!\n(Enemy shouldn't look)")
    time.sleep(3)
    player2_table = get_ship_locations(players[1], ships[1], tables[1])
    tables = [player1_table, player2_table]
    return tables


def get_ship_locations(player, ships, table):
    ship_locations = {0: "",
                      1: "",
                      2: "",
                      3: ""}
    print(player + "! Now it is time to place your ships on the battlefield!\nThese are your ships:")
    print("""\nFirst choose a letter and a number where you want your ships to begin. You can place them horizontally 
or vertically. Please consider carefully the size of the ships and the battlefield! Also consider positioning wisely."""
          )
    for i in range(4):
        os.system('clear')
        print("Your ships:\n" + str(ships))
        print(table)
        print("Ship number {}!".format(i))
        ship_locations[i] = multiplayer_functions.get_details_for_location()
        table = multiplayer_functions.refresh_table(table, ship_locations, ships)
        print(ship_locations)
    return table


def get_hidden_tables(tables):
    player1_hidden_table = multiplayer_functions.get_hidden_table(tables[0])
    player2_hidden_table = multiplayer_functions.get_hidden_table(tables[1])
    hidden_tables = [player1_hidden_table, player2_hidden_table]
    return hidden_tables


def player_turn(table, hidden_table, enemy):
    os.system('clear')
    print(enemy + "'s table:\n" + hidden_table + "\nYour table:\n" + table)
    player_attack = multiplayer_functions.get_player_attack()
    player_attack = multiplayer_functions.player_attack_check(player_attack)
    return player_attack


def get_attack_status(player_attack, table):
    attack_status = multiplayer_functions.attack_status_check(player_attack, table)
    multiplayer_functions.get_feedback(attack_status)
    time.sleep(2)
    return attack_status


def update_player_locations(ship_locations, attack_status):
    ship_locations = multiplayer_functions.treat_locations(attack_status, ship_locations)
    return ship_locations


def update_hidden_tables(hidden_table, player_attack, attack_status):
    hidden_table = multiplayer_functions.update_hidden_table(hidden_table, player_attack, attack_status)
    return hidden_table


def turn_barrier(player, enemy):
    os.system('clear')
    print(player + " 's turn! (" + enemy + " shouldn't look!!!")
    time.sleep(3)


def get_results(locations):
    results = None
    return results
