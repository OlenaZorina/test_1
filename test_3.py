import time
from selene import browser, by, be, have
from selene._managed import config

def click():
    pass

def test_friends():
    config.window_width = 1440
    config.window_height = 1000

    browser.open('http://opencart.qatestlab.net/index.php?route=common/home')
    browser.element(by.xpath('//*[text()="Аккаунт"][1]')).click()
    browser.element(by.xpath('//*[text()="Регистрация"]')).click()
    browser.element('#input-firstname').type('Olena').press_enter()
    browser.element('#input-lastname').type('2512').press_enter()
    browser.element('#input-email').type('zorinae83@gmail.com').press_enter()
    browser.element('#input-telephone').type('0958248814').press_enter()
    browser.element('#input-password').type('12345').press_enter()
    browser.element('#input-confirm').type('12345').press_enter()
    browser.element(by.css('[type="radio"][name="agree"]')).click()
    browser.element('[value="Продолжить"]').click()
    time.sleep(5)
    #


def should(param):
    pass


def test_authorization():
    browser.open('http://opencart.qatestlab.net')
    browser.driver.maximize_window()
    browser.element(by.xpath('//*[text()="Войти"]')).click()
    browser.element('#input-email').type('zorinae83@gmail.com')
    browser.element('#input-password').type('12345')
    browser.element('[value="Войти"]').click()
    # time.sleep(5)

    # browser.element('.list-unstyled>li>a:nth-of-type(1)').click()
    # browser.all('.list-unstyled>li:nth-of-type(1) [href="http://opencart.qatestlab.net/index.php?route=account/edit"]').should(have.texts('Учетная запись'))
    # browser.all('#input-firstname').should(have.texts('Olena'))
    time.sleep(10)

def test_auto():
    browser.open('http://opencart.qatestlab.net')
    browser.driver.maximize_window()
    browser.element('.sf-with-ul').click()
    browser.element(by.text('HDP Dog Boots Blue Set of 4 Medium')).click()
    browser.all('.sbHolder .sbToggle')[0].click()
    # browser.element('.sbToggle .sbToggleOpen').click()
    browser.element('.sbHolder>ul>li:nth-of-type(2)').click()
    browser.element('.quantity>button').click()
    time.sleep(10)

    browser.all('.cart-total2').should(have.texts('2'))
    time.sleep(10)




