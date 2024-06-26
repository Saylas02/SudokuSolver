import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import solver


def main():
    website = "https://sudoku.tagesspiegel.de/mittel"
    driver = webdriver.Chrome()
    driver.get(website)

    time.sleep(1.5)

    cookie_iframe = driver.find_element(By.XPATH, '/html/body/div[2]/iframe')
    driver.switch_to.frame(cookie_iframe)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div[3]/div[1]/div/button').click()
    driver.switch_to.parent_frame()

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

    for square, entries in enumerate(solved_grid):
        square_element = driver.find_element(By.XPATH, f'//*[@id="game-square"]/div[{square+1}]/div')
        #TODO: mark given elemtes with flag, performance boost
        if square_element.text != '':
            continue
        else:
            square_element.click()
            actions = ActionChains(driver)
            actions.send_keys(entries).perform()

    time.sleep(15)


if __name__ == "__main__":
    main()
