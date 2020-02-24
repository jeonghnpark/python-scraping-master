from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print("Http error")
except URLError as e:
    print("server error")
else:
    #bs = BeautifulSoup(html.read(), 'html.parser')
    print(html.read())

