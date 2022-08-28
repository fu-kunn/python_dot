import requests

url = 'https://jsonplaceholder.typicode.com/posts/'
res = requests.get(url)


# print(res.status_code)
# print(res.json()[:5])
datum = res.json()[0]
print(datum['title'])