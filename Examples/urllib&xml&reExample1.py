import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1636408.xml'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'xml')

total = 0
lista = [int(s) for s in re.findall("[0-9]+", str(soup.find('comments')))]
for i in lista:
    total += i
    
print(total)