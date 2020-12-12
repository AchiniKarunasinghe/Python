import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# http://py4e-data.dr-chuck.net/comments_1072155.html
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0
sum = 0
tags = soup('span')
for tag in tags:
    count = count + 1;
    x = int(tag.text)
    sum = sum+x
print(count)
print(sum)
