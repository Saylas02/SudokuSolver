import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import solver


def main():
    website = "https://sudoku.tagesspiegel.de/"
    driver = webdriver.Chrome()
    driver.get(website)

    values = []
    for square in range(1, 82):
        elements = driver.find_element(By.XPATH, f'// *[ @ id = "game-square"] / div[{square}]').text
        if elements == '':
            values.append(0)
        else:
            values.append(int(elements))

    grid, depth = [[], [], [], [], [], [], [], [], []], 0
    for count, elements in enumerate(values):
        if count % 9 == 0:
            depth += 1
            grid[depth-1].append(elements)
        else:
            grid[depth-1].append(elements)

    solved_grid = solver.solve(grid)


#TODO: setup push entries to cell
"""
    for square, entries in enumerate(solved_grid):
        print(square+1, entries)
        elements = driver.find_element(By.XPATH, f'// *[ @ id = "game-square"] / div[{square+1}]')
        elements.send_keys(entries)
"""


if __name__ == "__main__":
    main()
