def horizontally(table, locations, ships):
    for ship in ships:
        for value in ship:
            counter = len(value)
            table = draw_on_table_horizontally(counter, table, locations)
            return table
        return table
    return table


def draw_on_table_horizontally(counter, table, locations):
    starting_point = get_horizontal_starting_point(table, locations)
    table = draw_horizontal_ship(table, counter, starting_point)
    return table


def get_horizontal_starting_point(table, locations):
    letter = locations[0]
    number = locations[1]
    starting_point = 0
    for char in table:
        if letter == char:
            starting_point = table.index(char) + 41 * int(number)
            return starting_point
        return starting_point
    return starting_point


def get_horizontal_ending_point(counter, starting_point):
    return starting_point + 4 * counter


def draw_horizontal_ship(table, counter, starting_point):
    for swap in range(counter):
        table = table.replce(table[starting_point + 4 * swap], "X")
        return table
    return table


def vertically(table, locations, ships):
    for ship in ships:
        for value in ship:
            counter = len(value)
            table = draw_on_table_vertically(counter, table, locations)
            return table


def draw_on_table_vertically(counter, table, locations):
    starting_point = get_vertical_starting_point(table, locations)
    table = draw_vertical_ship(table, counter, starting_point)
    return table


def get_vertical_starting_point(table, locations):
    starting_point = None
    return starting_point


def draw_vertical_ship(table, counter, starting_point):
    table = None
    return table
