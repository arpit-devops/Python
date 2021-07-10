import requests

r = requests.get("https://xkcd.com/")

print (r.status_code)
print(r.ok)   # True for anything that is less that 400 response code