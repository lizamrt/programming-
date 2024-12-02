import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def get_exchange_rate(date):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

currency_code = "USD"  
today = datetime.now()
dates = [(today - timedelta(days=i)).strftime("%Y%m%d") for i in range(7)]  

rates = []
dates_for_plot = []

for date in dates:
    data = get_exchange_rate(date)
    if data:
        for item in data:
            if item["cc"] == currency_code:
                rates.append(item["rate"])
                dates_for_plot.append(datetime.strptime(date, "%Y%m%d").strftime("%d-%m-%Y"))
                break

plt.figure(figsize=(10, 6))
plt.plot(dates_for_plot[::-1], rates[::-1], marker="o", label=currency_code)  
plt.title(f"Зміна курсу {currency_code} за останній тиждень")
plt.xlabel("Дата")
plt.ylabel("Курс (грн)")
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
