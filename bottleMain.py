from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<h1>Hello {{name}}!, Welcome to Bottle Framework</h1>', name=name)

run(host='localhost', port=8080)