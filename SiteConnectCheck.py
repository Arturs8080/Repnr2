import requests

url = input('Enter URL: ')
req = requests.get(url)

req.status_code
print(req.status_code)

if req.status_code == 200:
    print('URL is reachable')
else:
    print('URL is not reachable')
