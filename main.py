import requests

url = 'https://jsonplaceholder.typicode.com/posts/'
body = {
  'id': 5
}
res = requests.get(url, body)


# print(res.status_code)
print(res.json())
# datum = res.json()[0]
# print(datum['title'])