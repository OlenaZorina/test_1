import time
from selene import have, by
from selene.support.shared import browser
from TodoMVC_testing.model import todos

def test_e2e():
    todos.open()
    todos.add('a', 'b', 'c')
    todos.should_be('a', 'b', 'c')
    todos.edit('a', 'd')
    todos.should_be('d', 'b', 'c')
    todos.edit_by_focus_change('d', 'a')
    todos.cancel_edit('a', 'd')
    todos.toggle('a')
    todos.toggle_all()
    todos.should_be_completed('a', 'b', 'c')
    todos.should_be_active('a', 'b', 'c')
    todos.delete('a')



def test_complete_todo():
    todos.open()
    todos.add('a', 'b', 'c')

def test_add_todos():
    todos.open()
    todos.add('a', 'b', 'c')
    todos.should_be('a', 'b', 'c')

    # todos.should_be_items_left(3)

def test_edit():
    todos.given_opened('a', 'b', 'c')
    todos.should_be('a', 'b', 'c')
    todos.edit('a', 'd')
    todos.should_be('d', 'b', 'c')
    time.sleep(5)
def test_edit_by_focus_change():
    todos.given_opened('d', 'b', 'c')
    todos.edit_by_focus_change('d', 'a')
    time.sleep(5)

def test_cancel_edit():
    todos.given_opened('d', 'b', 'c')
    todos.edit_by_focus_change('d', 'a')
    todos.cancel_edit('a', 'd')

def test_toggle():
    todos.given_opened('a', 'b', 'c')
    todos.toggle('a')

def test_toggle_all():
    todos.given_opened('a', 'b', 'c')
    todos.toggle_all()

def test_should_be_completed():
    todos.given_opened('a', 'b', 'c')
    todos.toggle_all()
    todos.should_be_completed('a', 'b', 'c')

def test_should_be_active():
    todos.given_opened('a', 'b', 'c')
    todos.toggle_all()
    todos.should_be_active('a', 'b', 'c')

def test_delete():
    todos.open()
    todos.add('a', 'b', 'c')
    time.sleep(5)
    todos.delete('a')




    #browser.all('#todo-list>li').should(have.exact_texts('Olena', 'Eugenia', 'Eduard', 'Yacheslav', 'Iryna', 'Volodymyr'))
    #
    #browser.element('#todo-list>li:nth-of-type(6) .toggle').click()
    #time.sleep(2)
    #browser.element(by.text('Completed')).click()
    #browser.all('#todo-list>li.completed').should(have.texts('Volodymyr'))
    #browser.element(by.text('Active')).click()
    #browser.all('#todo-list>li. active').should(have.texts('Olena', 'Eugenia', 'Eduard', 'Yacheslav', 'Iryna'))
    #time.sleep(10)
    #browser.element(by.text('Clear completed')).click()
    #browser.all('#todo-list>li').should(have.texts())
    #browser.quit()


