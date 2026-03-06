import requests

url = "http://localhost:8080"

data = {
    "name": "Alice",
    "age": 20
}

response = requests.get(url, json=data)

print(response.json())