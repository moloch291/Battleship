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
            table = draw_on_table_vertically(counter, table, locations)
            return table


def draw_on_table_horizontally(counter, table, locations):
    starting_point = get_horizontal_starting_point(table, locations)
    ending_point = get_horizontal_ending_point(counter, starting_point)
    table = draw_horizontal_ship(table, counter, starting_point, ending_point)
    return table


def draw_on_table_vertically(counter, table, locations):
    starting_point = get_vertical_starting_point(table, locations)
    ending_point = get_vertical_ending_point(table, counter, starting_point)
    table = draw_vertical_ship(table, counter, starting_point, ending_point)
    return table


def get_vertical_starting_point(table, locations):
    starting_point = None
    return starting_point


def get_vertical_ending_point(table, counter, starting_point):
    ending_point = None
    return ending_point


def draw_vertical_ship(table, counter, starting_point, ending_point):
    table = None
    return table


def get_horizontal_starting_point(table, locations):
    letter = locations[0]
    number = locations[1]
    for char in table:
        if letter == char:
            return table.index(char) + 41 * int(number)


def get_horizontal_ending_point(counter, starting_point):
    return starting_point + 4 * counter


def draw_horizontal_ship(table, counter, starting_point, ending_point):
    for char in table:
        if starting_point
