import urllib2
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')




#txt_path = r"/Users/zhoufengting/Desktop/href_2013_2014.txt"
#fp = open(txt_path)
#print len(fp)
#for line in fp:
	#print line
url = r"http://www.eurosport.com/football/ligue-1/2013-2014/montpellier-hsc-paris-saint-germain_mtc616155/live.shtml"
request = urllib2.urlopen(url)
response = request.read()
soup = BeautifulSoup(response,"html.parser")
Names_major = soup.find_all("ul",class_ = "players away-team")[0]
print Names_major.find_all("span",class_="replacement").text

	#print response

	#soup = BeautifulSoup(response,"html.parser")
	#print line
#lines = fp.readline()
#print lines
