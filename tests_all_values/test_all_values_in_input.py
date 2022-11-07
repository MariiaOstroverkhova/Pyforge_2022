from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import tkinter as tk
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_all_values_in_input():
    #buttins_work_with_empty_input_field
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome_driver.get("https://rioran.github.io/ru_vowels_filter/main.html")
    chrome_driver.maximize_window()
    output_field = chrome_driver.find_element("id", "text_output")
    input_field = chrome_driver.find_element("id", "text_input")
    input_field.clear()
    input_field.send_keys("а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ы ь ъ э ю я\n1234567890!@#$%^&*()_-+=\\|/{[}] ?,.")
    chrome_driver.find_element("css selector", ".btn:nth-child(1)").click()
    assert output_field.text == "аеёиоуыэюя"

    chrome_driver.find_element("css selector", ".btn:nth-child(2)").click()
    assert output_field.text == "а е ё и о у ы э ю я"

    chrome_driver.find_element("css selector", ".btn:nth-child(3)").click()
    assert output_field.text == "а е ё и о у ы э ю я\n!- ?,."

    chrome_driver.find_element("css selector", ".btn:nth-child(4)").click()
    a = ActionChains(chrome_driver)
    a.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()
    root = tk.Tk()
    root.withdraw()
    variable = root.clipboard_get()
    assert variable == "а е ё и о у ы э ю я\n!- ?,."

    chrome_driver.quit()