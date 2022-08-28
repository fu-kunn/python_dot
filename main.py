import requests

url = 'https://jsonplaceholder.typicode.com/posts/'
res = requests.get(url)
res.status_code

print(res.status_code)