import multiplayer_meta
import menu


def game_cycle():
    multiplayer_meta.create_player_profiles()
    players = multiplayer_meta.get_players()
    tables = multiplayer_meta.get_tables()
    ships = multiplayer_meta.get_ships()
    locations = multiplayer_meta.get_locations(players, ships)
    tables = multiplayer_meta.refresh_tables(tables, locations, players)
    hidden_tables = multiplayer_meta.get_hidden_tables(tables)
    while locations[0] and locations[1]:
        multiplayer_meta.turn_barrier(players[0], players[1])
        player1_attack = multiplayer_meta.player_turn(tables[0], hidden_tables[1], players[1])
        player1_attack_status = multiplayer_meta.get_attack_status(player1_attack, tables[1])
        hidden_tables = multiplayer_meta.update_hidden_tables(hidden_tables[1], player1_attack, player1_attack_status)
        multiplayer_meta.turn_barrier(players[1], players[0])
        player2_attack = multiplayer_meta.player_turn(tables[1], hidden_tables[0], players[0])
        player2_attack_status = multiplayer_meta.get_attack_status(player2_attack, tables[0])
        hidden_tables = multiplayer_meta.update_hidden_tables(hidden_tables[0], player2_attack, player2_attack_status)
    results = multiplayer_meta.get_results(locations)
    print(results)
    menu.menu()
