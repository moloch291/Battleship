import multiplayer_functions
import os
import time


def player_turn(table, hidden_table, ship_locations):
    print("Enemy's table:\n" + hidden_table + "\nYour field:\n" + table)
    player_attack = multiplayer_functions.get_player_attack(hidden_table)
    attack_status = multiplayer_functions.attack_check(player_attack, ship_locations)
    multiplayer_functions.get_feedback(attack_status)
    ship_locations = multiplayer_functions.treat_locations(attack_status, ship_locations)



def turn_barrier(player, enemy):
    os.system('clear')
    print(player + " 's turn! (" + enemy + " shouldn't look!!!")
    time.sleep(3)
