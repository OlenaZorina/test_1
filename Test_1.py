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

#browser.element('#todo-list>li:nth-of-type(2) .toggle').click()
# browser.element('#ember9').click()
#browser.element(by.text('Completed')).click()
#browser.all('#todo-list>li.completed').should(have.texts('b'))
#
# browser.element(by.text('Active')).click()
# browser.all('#filters>li.active').should(have.exact_texts('a', 'c'))
# time.sleep(60)
# browser.element('#ember9').click() - не вірно
