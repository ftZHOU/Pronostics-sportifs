#catch all the links for each team

import urllib2
from bs4 import BeautifulSoup
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

for j in range(1,21):
	url = "http://www.soccerstats.com/team.asp?league=france_2014&teamid="+str(j)
	request = urllib2.urlopen(url) 
	response = request.read()
	soup = BeautifulSoup(response,"html.parser")
	Home = soup.find_all(attrs = {"class":"tabbertab"})[1]


	#Home = soup.find_all("table",{"width":"'98%'"})

	PPG = str(Home.find_all("td",{"align":"center"})[0].find_all("b")[1].text)
	Wins = str(Home.find_all("td",{"align":"center"})[1].text#find_all("b")[1].text)