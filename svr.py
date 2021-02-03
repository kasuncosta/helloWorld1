from bottle import route, run, template
@route('/')
def index():
    return template('index.tpl')
    #return index.tpl page

@route('/test')
def index():
    output = '<b>It Works!</b>'
    return output

run(host='localhost', port='8080', debug='True', reloader='True')
#reloader will allow you to edit the index.tpl page
# without refreshing server from git bash