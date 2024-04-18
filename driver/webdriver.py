from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_driver():
    SERVICE = Service(executable_path="driver/chromedriver.exe")
    driver = webdriver.Chrome(service=SERVICE)
    return driver
