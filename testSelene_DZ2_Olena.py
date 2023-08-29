import time

from selene import by, have
from selene.support.shared import browser
from selenium.webdriver.common.by import By

browser.open('https://www.ecosia.org/')
browser.element(by.name('q')).type('yashaka selene').press_enter()
browser.all(by.css(' .result'))[0].click()
time.sleep(10)

browser.all(by.css('[href="/yashaka/selene"]'))[0].click()
time.sleep(10)

print(len(browser.all(by.css('[href="/yashaka/selene"]'))))



# CSS [href='https://github.com/yashaka/selene/'][class='result__link']
