import requests
import json
import webbrowser

base_url = "http://numbersapi.com/"
data = input("What kind of data are you looking for?")
url = base_url + data + "?json"
#print(url)

#webbrowser.open(url)

response = requests.get(url)
json_data = response.json()


print(json_data["text"])
