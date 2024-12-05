from bottle import route, run, request, response

@route('/header')
def handle_headers():

    content_type = request.get_header('Content-Type')

    if content_type == 'application/json':
        response.content_type = 'application/json'
        return {'currency': 'USD', 'rate': 41.5}
    elif content_type == 'application/xml':
        response.content_type = 'application/xml'
        return '''<currency>
    <name>USD</name>
    <rate>41.5</rate>
</currency>'''
    else:
    
        response.content_type = 'text/plain'
        return 'USD - 41.5'

if __name__ == '__main__':
    run(host='localhost', port=8000)
