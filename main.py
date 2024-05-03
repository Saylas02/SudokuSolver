import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_data_from_website():
    website = "https://sudoku.tagesspiegel.de/"
    driver = webdriver.Chrome()
    driver.get(website)

    time.sleep(2)

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

    print(grid)


if __name__ == "__main__":
    get_data_from_website()
