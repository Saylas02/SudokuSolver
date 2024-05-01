def sudoku_matrix_generator():
    for y in range(9):
        for x in range(9):
            yield y, x


def reset_possible_numbers(grid: list):
    return [[[1, 2, 3, 4, 5, 6, 7, 8, 9] if grid[y][x] == 0 else [] for x in range(0, 9)] for y in range(0, 9)]


def check_rows(grid: list, arr_pos_nr: list):
    for y, x in sudoku_matrix_generator():
        if grid[y][x] != 0:
            continue
        for i in range(9):
            if grid[y][i] != 0 and grid[y][i] in arr_pos_nr[y][x]:
                arr_pos_nr[y][x].remove(grid[y][i])
    return


def check_columns(grid: list, arr_pos_nr: list):
    for y, x in sudoku_matrix_generator():
        if grid[y][x] != 0:
            continue
        for i in range(9):
            if grid[i][x] != 0 and grid[i][x] in arr_pos_nr[y][x]:
                arr_pos_nr[y][x].remove(grid[i][x])
    return


def check_blocks(grid: list, arr_pos_nr: list):
    block_coordinates = {
        (0, 0): [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
        (0, 1): [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
        (0, 2): [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],

        (1, 0): [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
        (1, 1): [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
        (1, 2): [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],

        (2, 0): [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
        (2, 1): [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
        (2, 2): [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)],
    }
    for y, x in sudoku_matrix_generator():
        if grid[y][x] != 0:
            continue
        block_y, block_x = (y//3), (x//3)
        for bar, foo in block_coordinates[(block_y, block_x)]:
            if grid[bar][foo] != 0 and grid[bar][foo] in arr_pos_nr[y][x]:
                arr_pos_nr[y][x].remove(grid[bar][foo])
    return


def pretty_print_sudoku(grid: list) -> None:
    for y in range(9):
        for x in range(9):
            if x % 3 == 0 and x != 0 and x != 8:
                print("| ", end="")
            print(grid[y][x], end=" ")
        if y % 3 == 2 and y != 0 and y != 8:
            print("\n- - - + - - - + - - -", end="")
        print()
    return


def is_solved(grid: list) -> bool:
    for y, x in sudoku_matrix_generator():
        if grid[y][x] == 0:
            return False
    return True


if __name__ == "__main__":
    board = [[1, 0, 0, 6, 4, 5, 9, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 5, 9, 7, 0, 2, 0, 1, 0],
             [0, 0, 4, 0, 1, 0, 0, 0, 5],
             [0, 8, 0, 5, 0, 0, 0, 0, 3],
             [0, 6, 7, 0, 0, 0, 0, 8, 0],
             [0, 3, 8, 0, 5, 6, 0, 2, 7],
             [9, 0, 0, 8, 0, 4, 0, 3, 0],
             [6, 0, 0, 3, 0, 1, 0, 0, 0]]

    possible_nr = reset_possible_numbers(board)
    pretty_print_sudoku(board)
    check_rows(board, possible_nr)
    check_columns(board, possible_nr)
    check_blocks(board, possible_nr)
    is_solved(board)
