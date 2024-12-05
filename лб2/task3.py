from bottle import route, run, request

@route('/currency')
def get_currency():
    today = request.query.today
    key = request.query.key

    if today is not None and key == "value":
        return "USD - 41,5"

if __name__ == '__main__':

    run(host='localhost', port=8000)
