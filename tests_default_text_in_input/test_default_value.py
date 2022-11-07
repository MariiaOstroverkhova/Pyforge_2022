from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import tkinter as tk
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


def test_default_value_in_input():
    #buttins_work_with_empty_input_field
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome_driver.get("https://rioran.github.io/ru_vowels_filter/main.html")
    chrome_driver.maximize_window()
    output_field = chrome_driver.find_element("id", "text_output")
    chrome_driver.find_element("css selector", ".btn:nth-child(1)").click()
    assert output_field.text == "еяиееауоои\nияеоауаыееи\nоеоиееуиеи\nаиоыиоыуееи\n\nауияоеиаа"

    chrome_driver.find_element("css selector", ".btn:nth-child(2)").click()
    assert output_field.text == "еяи ее ауо ои\nияе оа уаые еи\nо еои е еу и е и\nаи оы и оы уееи\n\nауи яоеи аа"

    chrome_driver.find_element("css selector", ".btn:nth-child(3)").click()
    assert output_field.text == "еяи ее ауо ои,\nияе оа уаые еи.\nо еои е еу и е и\nаи оы и оы уееи.\n\nауи яоеи аа"

    chrome_driver.find_element("css selector", ".btn:nth-child(4)").click()
    a = ActionChains(chrome_driver)
    sleep(2)
    a.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()
    root = tk.Tk()
    root.withdraw()
    variable = root.clipboard_get()
    assert variable == "еяи ее ауо ои,\nияе оа уаые еи.\nо еои е еу и е и\nаи оы и оы уееи.\n\nауи яоеи аа"

    chrome_driver.quit()