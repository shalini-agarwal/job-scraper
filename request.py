import requests

# r = requests.get('https://xkcd.com/2285/')
# r = requests.get('https://imgs.xkcd.com/comics/recurring_nightmare.png')

# payload = {'page': 2, 'count': 25}
# r = requests.get('https://httpbin.org/get', params=payload)

# payload = {'username': 'corey', 'password': 'testing'}
# r = requests.post('https://httpbin.org/post', data=payload)

r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('coreyms', 'testing'))

# print(help(r)) 
# print(dir(r))
# print(r.text)
# r.status_code, r.ok, r.headers
# with open('comic.png', 'wb') as f:
#     f.write(r.content)

# print(r.headers)
# print(r.url)

# r_dict = r.json()
# print(r_dict['form'])

# form based authentication vs basic authentication

print(r)

