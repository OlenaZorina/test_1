import time
from shutil import nt

from selene import have, by
from selene.support.shared import browser

browser.open('https://todomvc.com/examples/emberjs/')
browser.element('#new-todo').type('a').press_enter()
browser.element('#new-todo').type('b').press_enter()
browser.element('#new-todo').type('c').press_enter()
browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))
#
browser.element('#todo-list>li:nth-of-type(1) .toggle').click()
browser.element('#todo-list>li:nth-of-type(2) .toggle').click()
browser.element('#todo-list>li:nth-of-type(3) .toggle').click()
browser.element(by.text('Completed')).click()
browser.all('#todo-list>li.completed').should(have.texts('a', 'b', 'c'))
browser.element(by.text('Clear completed')).click()
browser.all('#todo-list>li').should(have.texts())
browser.quit()


#time.sleep(20)




