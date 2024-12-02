import requests
from datetime import datetime, timedelta

NBU_API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

def get_currency_rate(date):
    formatted_date = date.strftime("%Y%m%d")  
    url = f"{NBU_API_URL}?date={formatted_date}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Помилка отримання даних за {date}: {response.status_code}")
        return None

today = datetime.now()
dates = [(today - timedelta(days=i)).date() for i in range(1, 8)]

currency_data = {}
for date in dates:
    print(f"Отримання даних за {date}...")
    data = get_currency_rate(date)
    if data:
        currency_data[date] = data

for date, rates in currency_data.items():
    print(f"\nКурс валют за {date}:")
    for rate in rates:
        print(f"{rate['cc']} - {rate['rate']} (Назва: {rate['txt']})")
