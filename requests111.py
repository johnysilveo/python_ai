import requests

res = requests.get("https://api.monobank.ua/bank/currency")
print(res.json())