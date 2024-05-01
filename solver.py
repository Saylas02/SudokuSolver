def sudoku_matrix_generator():
    for y in range(9):
        for x in range(9):
            yield y, x


def reset_possible_numbers():
    arr_possible_numbers = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for y in range(0, 9)] for x in range(0, 9)]
    print(arr_possible_numbers)


if __name__ == "__main__":
    grid = [[1, 0, 0, 6, 4, 5, 9, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 9, 7, 0, 2, 0, 1, 0],
            [0, 0, 4, 0, 1, 0, 0, 0, 5],
            [0, 8, 0, 5, 0, 0, 0, 0, 3],
            [0, 6, 7, 0, 0, 0, 0, 8, 0],
            [0, 3, 8, 0, 5, 6, 0, 2, 7],
            [9, 0, 0, 8, 0, 4, 0, 3, 0],
            [6, 0, 0, 3, 0, 1, 0, 0, 0]]

    reset_possible_numbers()
