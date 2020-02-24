from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import datetime
import random

html=urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs=BeautifulSoup(html, 'html.parser')
# links=bs.find_all('a')
# for link in links:
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

# for link in bs.find('div',{'id':'bodyContent'}).find_all('a', 
#     href=re.compile('^(/wiki/)((?!:).)*$')):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

#random walk
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html=urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs=BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id' : 'bodyContent'}).find_all('a',
href=re.compile('^(/wiki/)((?!:).)*$'))

links=getLinks('/wiki/Kevin_Bacon')

#print([link.attrs['href'] for link in links])
# for link in links:
#     print(link.attrs['href'])

for i in range(10):
    print(f"{i}th link: ")
    newArticleLink=links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticleLink)
    links=getLinks(newArticleLink)

# : 
#     newArticle=links[random.randint(0,len(links)-1)].attrs['href']
#     print(newArticle)
#     links=getLinks(newArticle)
