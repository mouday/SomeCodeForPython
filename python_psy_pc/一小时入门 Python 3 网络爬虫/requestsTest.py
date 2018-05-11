import requests
target="http://www.biqukan.com/1_1094/5403177.html"
req=requests.get(target)
print(req.text)