#crawler Part1

from urllib2 import urlopen
from bs4 import BeautifulSoup
import pprint


url = 'http://www.codingdojo.com'
hrefs = []
soup = BeautifulSoup(urlopen(url),"html.parser")
for link in soup.find_all('a'):
    hrefs.append(link.get('href'))

for item in hrefs
