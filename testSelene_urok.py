import time
from selene import have, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

s('https://todomvc.com/examples/emberjs/')
s('#new-todo').type('a').press_enter()
s('#new-todo').type('b').press_enter()
s('#new-todo').type('c').press_enter()

ss('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))
s('#todo-list>li:nth-of-type(2) .toggle').click()
s(by.text('Completed')).click()
ss('#todo-list>li.completed').should(have.texts('b'))

#time.sleep(10)
# browser.all('#todo-list>li:not(.completed)').should(have.exact_texts('a', 'c'))
# browser.element(by.text('Active')).click()
#
# browser.element('#ember9').click() - не вірно
# browser.quit()