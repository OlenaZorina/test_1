import time
from selene import have, by
from selene.support.shared import browser

browser.open('https://todomvc.com/examples/emberjs/')
browser.element('#new-todo').type('a').press_enter()
browser.element('#new-todo').type('b').press_enter()
browser.element('#new-todo').type('c').press_enter()
browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))
#
browser.element('#toggle-all').click()
browser.element(by.text('Clear completed')).click()
browser.all('#todo-list>li').should(have.exact_texts())
time.sleep(10)

