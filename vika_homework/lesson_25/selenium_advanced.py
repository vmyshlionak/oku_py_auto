from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from time import sleep
import pytest

@pytest.fixture
def driver():
     chrome_driver = webdriver.Chrome()
     chrome_driver.maximize_window()
     # chrome_driver.implicitly_wait(10) //неявное ожидание - общая настройка всех действий с элементами
     yield chrome_driver
     sleep(3)

def test_new_tab(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    driver.find_element(By.ID, 'new-page-link').click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    assert driver.current_url == 'https://www.qa-practice.com/elements/new_tab/new_page'
    assert driver.find_element(By.ID, 'result-text').text == 'I am a new page in a new tab'

def test_stale_error(driver):
    driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    checkbox = driver.find_element(By.ID, 'id_checkbox_0')
    checkbox.click()
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()
    assert driver.find_element(By.ID, 'result-text').text == 'select me or not'
    checkbox.click() # вот здесь будет StaleElementReferenceException, потому что страничка перезагрузилась на submit и Selenium потерял элемент
    # решается повторным поиском элемента

def test_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/iframe')
    iframe = driver.find_element(By.TAG_NAME,'iframe')
    driver.switch_to.frame(iframe)
    burger_menu = driver.find_element(By.CLASS_NAME, 'navbar-toggler-icon')
    burger_menu.click()
    driver.switch_to.default_content()
    driver.find_element(By.LINK_TEXT, 'Iframe').click()

def test_drag_and_drop(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    first_box = driver.find_element(By.ID, 'rect-draggable')
    second_box = driver.find_element(By.ID, 'rect-droppable')
    action = ActionChains(driver)
    action.drag_and_drop(first_box, second_box).perform()

def test_alert(driver):
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    driver.find_element(By.CLASS_NAME, 'a-button').click()
    alert = Alert(driver)
    alert.accept()

