import time
from selene import browser, by, be, have


def open(self):
    browser.open('https://todomvc4tasj.herokuapp.com/')
    app_loaded = "return $._data($('#clear-completed')[0], 'events')" \
                 ".hasOwnProperty('click')"
    browser.should(have.js_returned(True, app_loaded))
    return self