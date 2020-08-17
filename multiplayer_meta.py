import multiplayer_functions
import os
import time


def get_players():
    print("Player 1:")
    player1 = multiplayer_functions.get_name()
    print("Player 2:")
    player2 = multiplayer_functions.get_name()
    players = [player1, player2]
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


def get_locations(tables, ships):
    player1_locations = multiplayer_functions.get_ship_locations(tables[0], ships[0])
    player2_locations = multiplayer_functions.get_ship_locations(tables[1], ships[1])
    locations = [player1_locations, player2_locations]
    return locations


def refresh_tables(tables, locations):
    player1_table = multiplayer_functions.put_ships_on_table(tables[0], locations[0])
    player2_table = multiplayer_functions. put_ships_on_table(tables[1], locations[1])
    tables = [player1_table, player2_table]
    return tables


def get_hidden_tables(tables):
    player1_hidden_table = multiplayer_functions.get_hidden_table(tables[0])
    player2_hidden_table = multiplayer_functions.get_hidden_table(tables[1])
    hidden_tables = [player1_hidden_table, player2_hidden_table]
    return hidden_tables


def player_turn(table, hidden_table):
    os.system('clear')
    print("Enemy's table:\n" + str(hidden_table) + "\nYour field:\n" + table)
    player_attack = multiplayer_functions.get_player_attack(hidden_table)
    return player_attack


def get_attack_status(player_attack, ship_locations):
    attack_status = multiplayer_functions.attack_check(player_attack, ship_locations)
    multiplayer_functions.get_feedback(attack_status)
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
