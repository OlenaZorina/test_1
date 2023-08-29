import time
from selene import by
from selene.support.shared import browser

browser.open('https://www.ecosia.org/')
browser.element(by.name('q')).type('it step academy').press_enter()
browser.element(by.css('[href="https://itstep.org/uk"][tabindex="-1"]')).click()
browser.all('.marker-city.cremenchug-small  .marker-point').first.click()

page_text = browser.driver.page_source.lower()
# Джерело сторінки драйвера браузера нижче
count = page_text.count('it step')
print('Слово на цій сторінці повторюється: ', count, 'разів')