import json
import time
import requests
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep


def get_data_from_website(website: str):
    """Get Data (Sudoku Grid values) from website
    #TODO: setup accept cookie popup
    website = "https://sudoku.zeit.de/"
    # chrome_path = 'C:\Program Files\Google\Chrome\Application'
    driver = webdriver.Chrome()
    driver.get(website)
    time.sleep(5)
    elem = driver.find_element(By.XPATH, '//*[@id="notice"]/div[4]/div[1]/button').click()
    """
    return True