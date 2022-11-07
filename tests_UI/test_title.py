from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def test_title():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome_driver.get("https://rioran.github.io/ru_vowels_filter/main.html")
    chrome_driver.maximize_window()
    assert chrome_driver.title == "Фильтр для гласных"

    chrome_driver.quit()