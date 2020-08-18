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
    ships = {1: "XXXXXX",
             2: "XXXXX",
             3: "XXXX",
             4: "XXX",
             5: "XX"}
    return ships


def get_ship_locations(player, ships):
    ship_locations = {1: "",
                      2: "",
                      3: "",
                      4: "",
                      5: ""}
    print(player + "! Now it is time to place your ships on the battlefield!\nThese are your ships: " + str(ships) +
          """\nFirst choose a letter and a number where you want your ships to begin. You can place them horizontally or 
          vertically!""")
    for i in range(5):
        print("Ship number {}!".format(i + 1))
        ship_locations[i + 1] = put_ships_on_table()
    return ship_locations


def put_ships_on_table():
    letter = input("Type in a letter! From A to I! ").capitalize()
    number = str(input("Type in a number between 1 and 9! "))
    type_of_placement: str = input("Place it horizontally or vertically? (h/v) ")
    location: str = letter + number + type_of_placement
    return location


def get_hidden_table(table):
    hidden_table = table
    return hidden_table


def get_player_attack():
    player_attack = input("Choose a filed to attack!\n")
    return player_attack


def player_attack_check(player_attack):
    player_attack = None
    return player_attack


def attack_status_check(player_attack, table):
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
