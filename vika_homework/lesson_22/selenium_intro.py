from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


options = Options()
options.add_argument('start-maximized')
# options.add_argument('window-size=500,1080')

# чтобы браузер не закрывался автоматически (для отладки):
options.add_experimental_option('detach', True )
driver = webdriver.Chrome(options=options)

# driver.maximize_window()
# driver.set_window_size(1920, 1080)
driver.get('https://www.google.com')
print(driver.title)
print(driver.current_url)

search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('cat')
# sleep(3)
# driver.find_element(By.NAME, 'btnK').click()
search_input.submit()

assert 'cat' in driver.title, f"Ожидалось 'cat' в заголовке, но получено: '{driver.title}'"

# Дожидание появления какого-либо элемента на странице:

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Ждем до 10 секунд, пока кнопка станет доступна для клика
# wait = WebDriverWait(driver, 10)
# btn = wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
# btn.click()
