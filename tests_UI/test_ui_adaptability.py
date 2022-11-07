from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_buttons_adaptability():
    #horizontal_alignment_with_max_window
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome_driver.get("https://rioran.github.io/ru_vowels_filter/main.html")
    chrome_driver.maximize_window()
    button1_location = chrome_driver.find_element("css selector", ".btn:nth-child(1)").location
    button2_location = chrome_driver.find_element("css selector", ".btn:nth-child(2)").location
    button3_location = chrome_driver.find_element("css selector", ".btn:nth-child(3)").location
    button4_location = chrome_driver.find_element("css selector", ".btn:nth-child(4)").location
    assert button1_location["y"] == button2_location["y"] == button3_location["y"] == button4_location["y"]

    #vertical_alignment_with_min_window
    chrome_driver.set_window_size(230, 824)
    chrome_driver.execute_script("document.body.style.zoom='200%'")
    button1_location = chrome_driver.find_element("css selector", ".btn:nth-child(1)").location
    button2_location = chrome_driver.find_element("css selector", ".btn:nth-child(2)").location
    button3_location = chrome_driver.find_element("css selector", ".btn:nth-child(3)").location
    button4_location = chrome_driver.find_element("css selector", ".btn:nth-child(4)").location
    assert button1_location["x"] == button2_location["x"] == button3_location["x"] == button4_location["x"]

    chrome_driver.quit()

