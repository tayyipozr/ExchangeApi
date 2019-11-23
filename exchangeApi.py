import requests
import json

apiUrl = "https://api.exchangeratesapi.io/latest?base="

exchange_input = input("Which currency do you want to exchange : ")
exchange_output = input("Which currency do you want to get : ")

money = int(input(f"How much {exchange_input} do you want to exchange : "))

result = requests.get(apiUrl+exchange_input)
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(exchange_input, result["rates"][exchange_output], exchange_output))
print("{0} {1} = {2} {3}".format(money, exchange_input, money * result["rates"][exchange_output], exchange_output))