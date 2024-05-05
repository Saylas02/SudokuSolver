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


def check_unions(grid: list, possible_nr: list):
    patterns = [
        [[(0,0),(0,1),(1,0),(1,1),  (0,7),(0,8),(1,7),(1,8),    (7,0),(7,1),(8,0),(8,1),    (7,7),(7,8),(8,7),(8,8)],
        [(2,2),(2,3),(2,4),(2,5),(2,6), (6,2),(6,3),(6,4),(6,5),(6,6),  (3,2),(4,2),(5,2),  (3,6),(4,6),(5,6)]],
    ]
    allDigitsSet = {1,2,3,4,5,6,7,8,9}
    
    for pattern in patterns:
        blue_pattern, purple_pattern = pattern[0], pattern[1]
        blue_set, purple_set = set(), set()
        
        for y,x in blue_pattern:
            blue_set = blue_set.union(set(possible_nr[y][x])).union(set([grid[y][x]]))
            
        for y,x in purple_pattern:
            purple_set = purple_set.union(set(possible_nr[y][x])).union(set([grid[y][x]]))
            
        left_possibleNums = allDigitsSet.difference(blue_set.intersection(purple_set))
        
        for y,x in (blue_pattern + purple_pattern):
            for l in left_possibleNums:
                if l in possible_nr[y][x]:
                    possible_nr[y][x].remove(l)


def set_single_possible_number(grid: list, possible_nr: list):
    for y, x in sudoku_matrix_generator():
        if grid[y][x] != 0:
            continue
        if len(possible_nr[y][x]) == 1:
            grid[y][x] = possible_nr[y][x][0]
            possible_nr[y][x] = []


def pretty_print_sudoku(grid: list) -> None:
    for y in range(9):
        for x in range(9):
            if x % 3 == 0 and x != 0 and x != 8:
                print("| ", end="")
            print(grid[y][x], end=" ")
        if y % 3 == 2 and y != 0 and y != 8:
            print("\n- - - + - - - + - - -", end="")
        print()
    print()
    return


def is_solved(grid: list) -> bool:
    for y, x in sudoku_matrix_generator():
        if grid[y][x] == 0:
            return False
    return True


def solve(grid: list):
    pretty_print_sudoku(grid)
    count, maxIters = 1, 100
    while not is_solved(grid) and count < maxIters:
        #Reset Setup
        possible_nr = reset_possible_numbers(grid)
        
        #Sort out not possible Numbers
        check_rows(grid, possible_nr)
        check_columns(grid, possible_nr)
        check_blocks(grid, possible_nr)
        check_unions(grid, possible_nr)
        
        #Set safe numbers
        set_single_possible_number(grid, possible_nr)
        
        #Other Stuff
        print(f"Iteration: {count}")
        pretty_print_sudoku(grid)
        count += 1

    print(f"Solved with {count-1} iterations")


def string_to_grid(sudoku_str : str) -> list:
    grid = [[0]*9 for _ in range(9)]
    for y,x in sudoku_matrix_generator():
        grid[y][x] = int(sudoku_str[y*9+x])
    return grid


if __name__ == "__main__":
    board = string_to_grid("000000008309806120000153940500260370003008500401007090600300000900040000872000010")
    solve(board)
