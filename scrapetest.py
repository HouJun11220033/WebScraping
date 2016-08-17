from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html, read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/exercises")
if title == None:
    print("Title could not be found")
else:
    print(title)



# html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
# bsObj = BeautifulSoup(html.read())
# print(bsObj.h1)
