import menu


def get_name():
    name = input("Player name: ")
    if name == "quit":
        menu.menu()
    return name


def create_table():
    table = """_0_|_A_|_B_|_C_|_D_|_E_|_F_|_G_|_H_|_I_|_
_1_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_
_2_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_
_3_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_
_4_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_
_5_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_
_6_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_
_7_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_
_8_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_
_9_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_"""
    return table


def create_ships():
    ships = {0: "XXXXXX",
             1: "XXXXX",
             2: "XXXX",
             3: "XXX",
             4: "XX"}
    return ships


def get_ship_locations(player, table, ships):
    ship_locations = {}
    print(player + "Now it is time to place your ships on the battlefield!\nThese are your ships: " + str(ships) +
          """\nFirst choose a letter and a number where you want your ships to begin. Finally decide if you want to 
          place it horizontally or vertically!""")
    return ship_locations


def put_ships_on_table(table, ship_locations, player):
    print(player + "!\nPlease put your ships on the battlefield!")
    return table


def get_hidden_table(table):
    hidden_table = None
    return hidden_table


def get_player_attack(hidden_table):
    player_attack = input("Choose a filed to attack!\n")
    return player_attack


def attack_check(player_attack, table):
    attack_status = None
    return attack_status


def get_feedback(attack_status):
    feedback = None
    return feedback


def treat_locations(attack_status, ship_locations):
    ship_locations = None
    return ship_locations


def update_hidden_table(hidden_table, player_attack, attack_status):
    hidden_table = None
    return hidden_table
