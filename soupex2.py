import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#http://py4e-data.dr-chuck.net/known_by_Mir.html
#http://py4e-data.dr-chuck.net/known_by_Fikret.html
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
#Retrieve
pos = 18
count = 7
temp = 0
for i in range(count):
    tags = soup('a')
    for tag in tags:
        temp = temp + 1
        if temp == pos:
            print(tag.get('href', None))
        temp = 0
#    for tag in tags:
#        print(tag.get('href', None))

#tags = soup('a')
