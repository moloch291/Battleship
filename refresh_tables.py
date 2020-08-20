def horizontally(table, locations, ships):
    for ship in ships:
        for value in ship:
            counter = len(value)
            table = draw_on_table_horizontally(counter, table, locations)
            return table


def vertically(table, locations, ships):
    for ship in ships:
        for value in ship:
            counter = len(value)
            table = draw_on_table_horizontally(counter, table, locations)
            return table


def draw_on_table_vertically(counter, table, locations):
    starting_point = get_vertical_starting_point(table, locations)
    ending_point = get_vertical_ending_point(table, counter, starting_point)
    table = draw_vertical_ship(table, counter, starting_point, ending_point)
    return table


def draw_on_table_horizontally(counter, table, locations):
    starting_point = get_horizontal_starting_point(table, locations)
    ending_point = get_horizontal_ending_point(table, counter, starting_point)
    table = draw_horizontal_ship(table, counter, starting_point, ending_point)
    return table


def get_vertical_starting_point(table, locations):
    return table[46 + (4 * locations[2])]


def get_vertical_ending_point(table, counter, starting_point):
    return


def draw_vertical_ship(table, counter, starting_point, ending_point):
    table = None
    return table


def get_horizontal_starting_point(table, locations):
    return table[46 + (4 * locations[2])]


def get_horizontal_ending_point(table, counter, starting_point):
    ending_point = None
    return ending_point


def draw_horizontal_ship(table, counter, starting_point, ending_point):
    table = None
    return table
