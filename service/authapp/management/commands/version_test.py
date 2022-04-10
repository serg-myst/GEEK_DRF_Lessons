import requests

response = requests.get('http://127.0.0.1:8000/api/users_ver/', headers={'Accept': 'application/json; version=0.1'})
print(response.json())
