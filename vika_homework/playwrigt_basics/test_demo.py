from playwright.sync_api import Page, expect
import re
from time import sleep


def test_first(page: Page):
    page.set_extra_http_headers({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })
    page.goto('https://www.yandex.by/')
    search_field = page.get_by_role('combobox')
    search_field.fill('cat')
    search_field.press('Enter')
    expect(page).to_have_title(re.compile('^cat')) # ^cat = startswith, cat$ = endswith, просто cat - includes

def test_roles(page: Page):
    page.goto('https://testpages.eviltester.com/pages/mobile/')
    sleep(3)
    page.get_by_role('link', name='User Agent').first.click() #на странице 2 одинаковые сссылки -> first
    page.get_by_role('button', name='Check for Mobile Browser').click()


def test_by_text(page: Page):
    sleep(3)
    page.goto('https://www.qa-practice.com/')
    page.get_by_text('Single UI Elements').click()
    sleep(3)


def test_by_label(page: Page):
    sleep(3)
    page.goto('https://www.qa-practice.com/elements/input/simple')
    field = page.get_by_label('Text string')
    field.press_sequentially('ksjdfhksjdfh', delay=500)
    sleep(1)
    field.press('Control+a')
    sleep(1)
    field.press('Backspace')
    sleep(3)


def test_by_placeholder(page: Page):
    sleep(3)
    page.goto('https://www.qa-practice.com/elements/input/simple')
    page.get_by_placeholder('Submit me').fill('skdjfhsdf')
    sleep(3)

#мой
def test_by_alt_text(page: Page):
    sleep(3)
    page.goto('https://testpages.eviltester.com/apps/basiccart/?page=1&limit=10')
    page.get_by_alt_text('Mystic Apparatus 1').click()
    sleep(3)


def test_by_title(page: Page):
    sleep(3)
    page.goto('https://www.google.com/')
    page.get_by_title('Шукаць').fill('cat')
    sleep(3)


def test_by_testid(page: Page):
    sleep(3)
    page.goto('https://www.airbnb.com/')
    sleep(2)
    page.get_by_test_id('structured-search-input-search-button').click()
    sleep(3)

#ниже мои варианты

def test_by_css_selector(page: Page):
    sleep(3)
    page.goto('https://testpages.eviltester.com/pages/forms/number-inputs/')
    page.locator('#toggle-required').click()
    sleep(3)


def test_by_xpath(page: Page):
    sleep(3)
    page.goto('https://testpages.eviltester.com/pages/forms/number-inputs/')
    page.locator('//button[text()="Add Validation Attributes"]').click()
    sleep(3)

