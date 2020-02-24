from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

URL="http://www.pythonscraping.com/pages/page1.html"

def getTitle(url):
    try:
        html=urlopen(URL)
    except HTTPError as e:
        print("html open error")
        return None
    try:
        bs=BeautifulSoup(html.read(), 'lxml')
        title=bs.body.h1
    except AttributeError as e:
        print("Attribute error")
        return None

    return title

title=getTitle(URL)
print(title)

html=urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs=BeautifulSoup(html.read(), 'html.parser')
nameList=bs.findAll("span", {"class": "green"}) #
for name in nameList:
    print(name.get_text())
titles=bs.findAll(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
print('===')
print([title for title in titles])
print('--')
for title in titles:
    print(title)
print('----')
allTextGreenRed=bs.find_all('span', {'class' : {'green', 'red'}}) #greek OR red
print([text for text in allTextGreenRed])
print('--the prince')
nameList=bs.find_all(text={'the prince', 'The prince'})
print(len(nameList))

html=urlopen('http://www.pythonscraping.com/pages/page3.html')
bs=BeautifulSoup(html, 'html.parser')
print("---line46")
for child in bs.find('table', {'id' : 'giftList'}).children:
    print(child)

print(bs.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
images=bs.find_all('img',{'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
for image in images:
    print(image['src'])

attr2=bs.find_all(lambda tag:len(tag.attrs)==2)
print('attr2 list ================')

j=0
for i in attr2:
    print(f'{j}th')
    print(i)
    j=j+1
    
