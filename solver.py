def possible(grid, y, x, value):
    for i in range(0, 9):
        if grid[y][i] == value:
            return False
    for i in range(0, 9):
        if grid[i][x] == value:
            return False
    block_x = (x//3)*3
    block_y = (x//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[block_y+i][block_x+j] == value:
                return False
    return True


def solve_grid(grid: []) -> []:
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for value in range(1, 10):
                    if possible(grid, y, x, value):
                        grid[y][x] = value
                        solve_grid(grid)
                        grid[y][x] = 0
                return grid


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

    print(solve_grid(grid))