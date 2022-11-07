from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.color import Color
from time import sleep


def test_button2():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome_driver.get("https://rioran.github.io/ru_vowels_filter/main.html")
    button1 = chrome_driver.find_element("css selector", ".btn:nth-child(2)")
    assert button1.text == "Ну и ещё пробелы"
    sleep(2)
    button_color = button1.value_of_css_property("background-color")
    button_color_hex = Color.from_string(button_color).hex
    assert button_color_hex == "#0d6efd"

    chrome_driver.quit()