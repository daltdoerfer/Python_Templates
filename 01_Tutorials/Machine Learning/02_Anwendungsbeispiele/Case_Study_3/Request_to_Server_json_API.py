import requests

url = "http://localhost:5000/api"

r = requests.post(url, json={'x': [1, 20, 10, 10]})
print(r.json())

r = requests.post(url, json={'x': [0, 40, 10, 10]})
print(r.json())

r = requests.post(url, json={'x': [0, 60, 10, 10]})
print(r.json())