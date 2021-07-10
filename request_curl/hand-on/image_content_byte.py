import requests

r = requests.get("https://imgs.xkcd.com/comics/circuit_diagram.png")

#print (r.content)   #  this will give you byte, so we need to write this byte into .png file

with open("image.png", "wb") as fimg :
    fimg.write(r.content)

