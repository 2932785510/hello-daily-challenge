from urllib.request import urlopen

resp = urlopen("https://www.runoob.com/python3/python3-tutorial.html")
print(resp.status)
print(resp.read()[:100])