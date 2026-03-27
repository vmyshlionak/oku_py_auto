from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pytest

@pytest.fixture
def driver():
     chrome_driver = webdriver.Chrome()
     chrome_driver.maximize_window()
     yield chrome_driver
     sleep(3)


def test_id_name(driver):
    input_data = 'some_random_text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    # поиск по class_name содержит ньюанс: такое имя 'textinput textInput form-control' - это имена 3 классов, можно использовать любой, но один
    # поиск по tag_name подходит для заголовков высшего уровня (например, h1)
    text_string.send_keys(input_data)
    text_string.submit()
    result_string = driver.find_element(By.ID, 'result-text')
    assert result_string.text == input_data

def test_link_name(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    # первый способ добраться до ссылки вне зоны видимости:
    # driver.execute_script("document.body.style.zoom='75%'")
    contact_link = driver.find_element(By.LINK_TEXT, 'Contact')
    # второй способ добраться до ссылки вне зоны видимости (требует доп. импорта)
    # ActionChains(driver).move_to_element(contact_link).perform()
    contact_link.click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Contact us'

def test_css_selector(driver):
    input_data = 'smth'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.CSS_SELECTOR, '[placeholder]')
    text_string.send_keys(input_data)
    text_string.submit()
    result_string = driver.find_element(By.ID, 'result-text')
    assert result_string.text == input_data