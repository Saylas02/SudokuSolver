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
    for x, y in sudoku_matrix_generator():

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
    print(possible_nr)
