from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest

@pytest.fixture
def driver():
     chrome_driver = webdriver.Chrome()
     chrome_driver.maximize_window()
     # chrome_driver.implicitly_wait(10) //неявное ожидание - общая настройка всех действий с элементами
     yield chrome_driver
     sleep(3)

def test_clear(driver):
    input_data = 'some_random_text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    text_string.clear()

    # если не работает clear:
    # entered_value= text_string.get_attribute('value')
    # for _ in range(len(entered_value)):
    #     text_string.send_keys(Keys.BACKSPACE

def test_enabled_ans_select(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    button = driver.find_element(By.NAME, 'submit')
    assert (button.is_enabled() == False)
    select = driver.find_element(By.NAME, 'select_state')
    dropdown = Select(select)
    dropdown.select_by_value('enabled')
    assert (button.is_enabled() == True)

def test_5_sec(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    button = driver.find_element(By.ID, 'visibleAfter')
    button.click()

def test_5_sec2(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'visibleAfter')))
    button = driver.find_element(By.ID, 'visibleAfter')
    button.click()
    driver.add_cookie({'name': 'test_cookie', 'value': 'test_value'})
    print(driver.get_cookies())

