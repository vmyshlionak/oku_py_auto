from playwright.sync_api import Page, expect
from time import sleep
import re

def test_visible(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/alert')
    reqs = page.locator('#req_text')
    expect(reqs).to_be_hidden()
    page.locator('#req_header').click()
    expect(reqs).to_be_visible()


def test_enabled_and_select(page: Page):
    sleep(3)
    page.goto('https://www.qa-practice.com/elements/button/disabled')
    button = page.locator('#submit-id-submit')
    expect(button).to_be_disabled()
    page.locator('#id_select_state').select_option('Enabled')
    expect(button).to_be_enabled()
    expect(button).to_have_text('Submit')
    expect(button).to_contain_text('ubm')
    sleep(2)


def test_value(page: Page):
    text = 'qwert'
    # sleep(3)
    page.goto('https://www.qa-practice.com/elements/input/simple')
    input_field = page.locator('#id_text_string')
    input_field.fill(text)
    expect(input_field, f'input value is not {text}').to_have_value(text)

#найти свое что-то
def test_sort_and_waits(page: Page):
    # sleep(3)
    page.goto('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    greet = page.locator('.greet.welcome').locator('nth=0')
    expect(greet).not_to_be_empty()
    first_man = page.locator('.product-item-link').locator('nth=0')
    print(first_man.inner_text())
    page.locator('#sorter').locator('nth=0').select_option('Price')
    expect(page).to_have_url(re.compile('price'))
    print(first_man.inner_text())
