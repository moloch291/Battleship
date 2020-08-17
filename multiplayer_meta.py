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


def player_turn(table, hidden_table):
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


def update_hidden_table(hidden_table, player_attack, attack_status):
    hidden_table = multiplayer_functions.update_hidden_table(hidden_table, player_attack, attack_status)
    return hidden_table


def turn_barrier(player, enemy):
    os.system('clear')
    print(player + " 's turn! (" + enemy + " shouldn't look!!!")
    time.sleep(3)
