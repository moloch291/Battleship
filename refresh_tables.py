def refresh_horizontally(table, locations, ships):
    for ship in ships:
        for value in ship:
            counter = len(value)
            table = draw_on_table_horizontally(counter, table, locations)
            return table


#def refresh_vertically(table, locations, ships):


def draw_on_table_horizontally(counter, table, locations):
    starting_point = get_starting_point(counter, table, locations)
    ending_point = get_ending_point(counter, table, locations)



def get_starting_point(counter, table, locations):


def get_ending_point(counter, table, locations):