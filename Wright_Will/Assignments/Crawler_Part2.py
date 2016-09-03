#crawler Part2

from urllib2 import urlopen
from bs4 import BeautifulSoup
import pprint


url = 'http://www.codingdojo.com'
hrefs = {}
soup = BeautifulSoup(urlopen(url),"html.parser")  #parse website
for link in soup.find_all('a'):
    link_str = link.get('href')
    if link_str in hrefs:
        hrefs[link_str]+=1
    else:
        if link_str[0] =="/":
            link_str = url + link_str
        hrefs[link_str] = 1

for each in hrefs:
    print each + ": " +str(hrefs[each])
