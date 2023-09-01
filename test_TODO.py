import time

from selene import have, by
from selene.support.shared import browser
def test_complete_todo():
    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element('#new-todo').type('Olena').press_enter()
    browser.element('#new-todo').type('Eugenia').press_enter()
    browser.element('#new-todo').type('Eduard').press_enter()
    browser.element('#new-todo').type('Yacheslav').press_enter()
    browser.element('#new-todo').type('Iryna').press_enter()
    browser.element('#new-todo').type('Volodymyr').press_enter()
    browser.all('#todo-list>li').should(have.exact_texts('Olena', 'Eugenia', 'Eduard', 'Yacheslav', 'Iryna', 'Volodymyr'))
    #
    browser.element('#todo-list>li:nth-of-type(6) .toggle').click()
    time.sleep(2)
    #browser.element(by.text('Completed')).click()
    #browser.all('#todo-list>li.completed').should(have.texts('Volodymyr'))
    browser.element(by.text('Active')).click()
    browser.all('#todo-list>li. active').should(have.texts('Olena', 'Eugenia', 'Eduard', 'Yacheslav', 'Iryna'))
    time.sleep(5)
    #browser.element(by.text('Clear completed')).click()
    #browser.all('#todo-list>li').should(have.texts())
    #browser.quit()
    

