import multiplayer_functions
import multiplayer_meta


def game_cycle():
    players = multiplayer_meta.get_players()
    tables = multiplayer_meta.get_tables()
    ships = multiplayer_meta.get_ships()
    locations = multiplayer_meta.get_locations(tables, ships)
    tables = multiplayer_meta.refresh_tables(tables, locations)
    hidden_tables = multiplayer_meta.get_hidden_tables(tables)
    while player1_locations and player2_locations:
        multiplayer_meta.turn_barrier(players[0], players[1])
        player1_attack = multiplayer_meta.player_turn(player1_table, player2_hidden_table)
        player1_attack_status = multiplayer_meta.get_attack_status(player1_attack, player2_locations)
        player2_hidden_table = multiplayer_meta.update_hidden_table(player2_hidden_table, player1_attack, player1_attack_status)
        multiplayer_meta.turn_barrier(players[1], players[0])
        multiplayer_meta.player_turn(player2_table, player1_hidden_table)
