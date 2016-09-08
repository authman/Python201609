#crawler assignment
from urllib2 import urlopen
from bs4 import BeautifulSoup
import pprint
import re

url = 'https://www.codingdojo.com'

soup = BeautifulSoup(urlopen(url), "html.parser")

print soup
