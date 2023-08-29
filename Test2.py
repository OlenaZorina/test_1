import time

from selene import browser, by, be, have

browser.open('https://google.com/ncr')
browser.element(by.name('q')).should(be.blank)\
    .type('selenium').press_enter()
time.sleep(10)
browser.all('#rso>div').should(have.size_greater_than(5))\
    .first.should(have.text('Selenium automates browsers'))
time.sleep(10)