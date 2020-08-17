import multiplayer_functions
import multiplayer_meta
import os


def game_cycle():
    players = multiplayer_meta.get_players()
    player1_table = multiplayer_functions.create_table()
    player2_table = multiplayer_functions.create_table()
    player1_ships = multiplayer_functions.create_ships()
    player2_ships = multiplayer_functions.create_ships()
    player1_locations = multiplayer_functions.get_ship_locations(player1_table, player1_ships)
    player2_locations = multiplayer_functions.get_ship_locations(player2_table, player2_ships)
    player1_table = multiplayer_functions.put_ships_on_table(player1_table, player1_locations)
    player2_table = multiplayer_functions. put_ships_on_table(player2_table, player2_locations)
    player1_hidden_table = multiplayer_functions.get_hidden_table(player1_table)
    player2_hidden_table = multiplayer_functions.get_hidden_table(player2_table)
    while player1_locations and player2_locations:
        multiplayer_meta.turn_barrier(players[0], players[1])
        player1_attack = multiplayer_meta.player_turn(player1_table, player2_hidden_table)
        player1_attack_status = multiplayer_meta.get_attack_status(player1_attack, player2_locations)
        player2_hidden_table = multiplayer_meta.update_hidden_table(player2_hidden_table, player1_attack, player1_attack_status)
        multiplayer_meta.turn_barrier(players[1], players[0])
        multiplayer_meta.player_turn(player2_table, player1_hidden_table)
