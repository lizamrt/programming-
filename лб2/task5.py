from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

NBU_API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={}&json"

def get_exchange_rate(date):
    """Отримати курс валюти за вказану дату."""
    formatted_date = date.strftime('%Y%m%d')
    response = requests.get(NBU_API_URL.format(formatted_date))
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['rate']
    return None

@app.route('/currency', methods=['GET'])
def currency():
    param = request.args.get('param')

    if param == 'today':
        today = datetime.now()
        rate = get_exchange_rate(today)
        if rate:
            return jsonify({"date": today.strftime('%Y-%m-%d'), "USD": rate})

    elif param == 'yesterday':
        yesterday = datetime.now() - timedelta(days=1)
        rate = get_exchange_rate(yesterday)
        if rate:
            return jsonify({"date": yesterday.strftime('%Y-%m-%d'), "USD": rate})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
