import urllib2
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

for j in range(21,41):
	url = "http://www.soccerstats.com/team.asp?league=france_2015&teamid="+str(j)
	request = urllib2.urlopen(url) 
	response = request.read()
	soup = BeautifulSoup(response,"html.parser")
	Home = soup.find_all(attrs = {"class":"tabbertab"})[1]
	PPG =  str(Home.find_all("td",{"align":"center"})[0].find_all("b")[1].text)
	Wins = str(Home.find_all("td",{"align":"center"})[3].find_all("b")[1].text)
	lines = Home.find_all("tr")
	#print len(lines)
	Draws = lines[5].find_all("b")[1]
	Defeated = lines[5].find_all("b")[3]
	GSP = lines[10].find_all("b")[1]
	GCP = lines[13].find_all("b")[1]
	TGP = lines[15].find_all("b")[1]
	GO = lines[18].find_all("b")[1]
	print TGP.text
	#print Wins



	#print Wins
	#print GSP.text