def create_empty_2d_array(rows, columns):
    return [[False for _ in range(columns)] for _ in range(rows)]

def parse_pattern(pattern):
    cells_to_enable = []

    for row_index, row in enumerate(pattern.splitlines()):
        for column_index, column in enumerate(row):
            if column == "#":
                cells_to_enable.append([column_index, row_index])

    return cells_to_enable