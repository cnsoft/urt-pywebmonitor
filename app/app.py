from bottle import get, post, run, request, response, template, static_file
from urtserver import get_server_info

@get('/')
def index():
    return static_file('index.html',root='./views/')

@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static/')

@get('/getconfig')
def getconfig():
	response.set_header('Content-Type' , 'application/javascript')
	return 'configured_server_list = %s' % open('config.json').read()

@post('/getstatus')
def getconfig():
	urt_id = request.forms.get('id')
	urt_host = request.forms.get('host')
	urt_port = request.forms.get('port')
	return get_server_info(urt_id, urt_host, urt_port)


#run(host='0.0.0.0', port=8080, debug = True)
run(host='localhost', port=8080, server='gunicorn', workers=4)