
# Requests-HTML: HTML Parsing for Humans
# http://html.python-requests.org/

from requests_html import HTMLSession

url = "https://www.sogou.com/"
session = HTMLSession()
r = session.get(url)

print(type(r))  # <class 'requests_html.HTMLResponse'>
print(r)  # <Response [200]>

print(type(r.html.links))  # <class 'set'>
print(r.html.links)

print(r.html.absolute_links)

username = r.html.find("#news", first=True)
print(username.html)
print(username.text)
print(username.attrs)