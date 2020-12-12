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

tags = soup('a')
all_num_list = list()
link_position = 18
Process_repeat = 7
while Process_repeat - 1  >= 0 :
    print("Process round", Process_repeat)
    target = tags[link_position - 1]
    print("target:", target)
    url = target.get('href', 2)
    print("Current url", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    Process_repeat = Process_repeat - 1
