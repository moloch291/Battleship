import menu
import refresh_tables


def get_name():
    name = input("Player name: ")
    if name == "quit":
        menu.menu()
    return name


def create_table():
    table = """_0_|_A_|_B_|_C_|_D_|_E_|_F_|_G_|_H_|_I_|_\n_1_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_\n_2_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_\n_3_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_\n_4_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_\n_5_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_\n_6_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_\n_7_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_\n_8_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_\n_9_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_~_|_"""
    return table


def create_ships():
    ships = {0: "XXXXX",
             1: "XXXX",
             2: "XXX",
             3: "XX"}
    return ships


def get_details_for_location():
    letter = get_letter_for_location()
    number = get_number_for_location()
    type_of_placement = get_type_of_placement_for_location()
    location: str = letter + number + type_of_placement
    return location


def get_letter_for_location():
    letter = str(input("Type in a letter for your ship to start at!\nIt should be From A to I! ").capitalize())
    letter = letter_check(letter)
    return letter


def letter_check(letter):
    if letter in "ABCDEFGHI":
        return letter
    else:
        print("Invalid letter!")
        letter = get_letter_for_location()
        letter = letter_check(letter)
        return letter


def get_number_for_location():
    number = input("Type in a number between 1 and 9! ")
    number = number_check(number)
    return number


def number_check(number):
    if number in "123456789":
        return number
    else:
        print("Invalid number!")
        number = get_number_for_location()
        number = number_check(number)
        return number


def get_type_of_placement_for_location():
    type_of_placement = input("Place it horizontally or vertically? (h/v) ")
    type_of_placement = check_type_of_placement(type_of_placement)
    return type_of_placement


def check_type_of_placement(type_of_placement):
    if type_of_placement == "h" or type_of_placement == "v":
        return type_of_placement
    else:
        print("Invalid type!")
        type_of_placement = get_type_of_placement_for_location()
        type_of_placement = check_type_of_placement(type_of_placement)
        return type_of_placement


def get_hidden_table(table):
    hidden_table = table
    return hidden_table


def refresh_tables(table, locations, ships):
    for value in locations.items():
        if "h" in value:
            tables = refresh_tables.horizontally(table, locations, ships)
            return tables
        elif "v" in value:
            tables = refresh_tables.vertically(table, locations, ships)
            return tables


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
