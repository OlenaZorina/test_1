import time
from selene import browser, by, be, have
from selene._managed import config
from selene.support.shared.jquery_style import s, ss


def test_open():
    browser.open('https://www.ecosia.org/')
    browser.driver.maximize_window()
    browser.element(by.name('q')).type("respect ua").press_enter()
    browser.all(by.css('.result')).first.click()
    time.sleep(5)


def test_autirize():
    browser.open('https://respect-shoes.com.ua')
    browser.driver.maximize_window()
    browser.element('.login').click()
    browser.element('[placeholder="ЛОГІН"]').type('zorinae83@gmail.com')
    browser.element('[placeholder="ПАРОЛЬ"]').type('a0822a10f2')
    browser.element('.button').click()
    browser.all('.col-md-12>div').should(have.texts('Мій'))
    time.sleep(5)


def test_finding():
    browser.open('https://respect-shoes.com.ua')
    browser.driver.maximize_window()
    browser.element('#menu>ul>li>a').click()
    browser.element('.rowProducts.row8>div:nth-of-type(3)').click()
    browser.element('.pi-size-list>div:nth-of-type(4)').click()
    browser.element('.pi-cart').click()
    browser.element('.fa.fa-plus-square').click()
    browser.element('[title="Close"]').click()
    browser.element('.counter').click()
    browser.all('.counter').should(have.texts('2'))
    time.sleep(5)
    #browser.element('.col-xs-6 .remove').click()
    #time.sleep(15)
    #browser.element('.cart-products-remove>a').click()
    #browser.element('.empty').click()
    #browser.all('.col-md-12 .account').should(have.texts('Ваш кошик порожній!'))


