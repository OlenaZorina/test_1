import time
import selene
import typing_extensions
from selene import browser, by, be, have
from selene._managed import config

browser.open('https://www.ecosia.org/')
browser.driver.maximize_window()

browser.element(by.name('q')).type('python').press_enter()
browser.all(by.css('.result'))[2].click()
time.sleep(5)

page_text = browser.driver.page_source.lower()
count = page_text.count('python')
print('Слово на цій сторінці повторюється: ', count, 'разів')
