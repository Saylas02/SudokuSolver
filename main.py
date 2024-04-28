import json
import time
import requests
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep


def read_data_from_config() -> str:
    """Get website Url from config file"""
    with open('config.json', 'r') as config_file:
        config_file = json.load(config_file)
        website = config_file['website']
    return website


def get_data_from_website(website: str):
    """Get Data (Sudoku Grid values) from website
    #TODO: setup accept cookie popup
    # chrome_path = 'C:\Program Files\Google\Chrome\Application'
    driver = webdriver.Chrome()
    driver.get(website)
    time.sleep(5)
    elem = driver.find_element(By.XPATH, '//*[@id="notice"]/div[4]/div[1]/button').click()
    """
    return True


if __name__ == "__main__":
    # website_url = read_data_from_config()
    # print(get_data_from_website(website_url))
    sudoku = [[1, 0, 0, 6, 4, 5, 9, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 5, 9, 7, 0, 2, 0, 1, 0],
              [0, 0, 4, 0, 1, 0, 0, 0, 5],
              [0, 8, 0, 5, 0, 0, 0, 0, 3],
              [0, 6, 7, 0, 0, 0, 0, 8, 0],
              [0, 3, 8, 0, 5, 6, 0, 2, 7],
              [9, 0, 0, 8, 0, 4, 0, 3, 0],
              [6, 0, 0, 3, 0, 1, 0, 0, 0]]