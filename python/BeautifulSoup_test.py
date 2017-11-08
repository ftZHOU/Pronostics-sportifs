import urllib2
from bs4 import BeautifulSoup

url = "https://www.packtpub.com/all"
response = urllib2.urlopen(url)
soup = BeautifulSoup(response,"html.parser")
