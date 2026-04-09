from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)

# страница с инфинити скроллом
def test_scroll(driver):
    driver.get('https://people.onliner.by/2026/04/09/post-o-poiske-zheny')
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      sleep(2)  # Ждем подгрузки контента
      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
        break
      last_height = new_height

#другие варианты
#1
# element = driver.find_element(By.ID, "my-id")
# actions = ActionChains(driver)
# actions.scroll_to_element(element).perform()

#2
#driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

def test_upload_file(driver):
    driver.get('https://the-internet.herokuapp.com/upload')
    upload = driver.find_element(By.ID, 'file-upload')
    upload.send_keys(r'C:\Users\vmysh\Downloads\66f187c179cb5725e7915b867a7f2e10.jpg')
    driver.find_element(By.ID, 'file-submit').click()