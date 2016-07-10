import bottle
from bottle import route, run, request, post, redirect
from selflab.web import page
from selflab.web import newevent
from selflab.web.sqliteplugin import SQLitePlugin


@route('/')
def home():
    return page.html('selflab', newevent.html())


@post('/new_event')
def new_event(db):
    name = request.forms.get('name')
    quantity = request.forms.get('quantity')
    value = request.forms.get('value')
    details = request.forms.get('details')
    newevent.add(db, name, quantity, value, details)
    redirect('/')


def start(dbfile):
    sqlite = SQLitePlugin(dbfile=dbfile)
    bottle.install(sqlite)
    run(host='localhost', port=8080, debug=True)
