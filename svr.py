from bottle import route, run, template
@route('/')
def index():
    return template('index.tpl')

@route('/test')
def index():
    output = '<b>It Works!</b>'
    return output

run(host='localhost', port='8080', debug='True', reloader='True')