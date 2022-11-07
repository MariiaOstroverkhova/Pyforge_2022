from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import tkinter as tk
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_empty_input():
    #buttins_work_with_empty_input_field
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome_driver.get("https://rioran.github.io/ru_vowels_filter/main.html")
    chrome_driver.maximize_window()
    output_field = chrome_driver.find_element("id", "text_output")
    input_field = chrome_driver.find_element("id", "text_input")
    input_field.clear()
    chrome_driver.find_element("css selector", ".btn:nth-child(1)").click()
    assert output_field.text == ""

    chrome_driver.find_element("css selector", ".btn:nth-child(2)").click()
    assert output_field.text == ""

    chrome_driver.find_element("css selector", ".btn:nth-child(3)").click()
    assert output_field.text == ""

    chrome_driver.find_element("css selector", ".btn:nth-child(4)").click()
    assert output_field.text == ""

    chrome_driver.quit()
