import requests

response = requests.post('http://127.0.0.1:8000/api-token-auth/', data={'username':
                                                                            'serg', 'password': '1'})
print(response.status_code)
print(response.json())
