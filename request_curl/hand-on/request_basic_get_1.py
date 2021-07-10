import requests

r = requests.get("https://xkcd.com/")

print(r)
print(type(r))

print(dir(r))
#print(help(r))