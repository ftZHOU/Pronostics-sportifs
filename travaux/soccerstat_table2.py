# collecting all the attributes which describing performance 

import urllib2
from bs4 import BeautifulSoup
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# stock the data in an existing workbook excel
excel_address = r'/Users/zhoufengting/projet/soccerstat_1.xls'
work_book = open_workbook(excel_address)
wb = copy(work_book)
sheet = wb.get_sheet(0)

# I find the differences of all the links for all 20 teams is just the final number
for j in range(1,21):
	url = "http://www.soccerstats.com/team.asp?league=france_2014&teamid="+str(j)
	request = urllib2.urlopen(url) 
	response = request.read()
	soup = BeautifulSoup(response,"html.parser")

	# collect data from table "home" and table "away"
	Home = soup.find_all(attrs = {"class":"tabbertab"})[1]
	Away = soup.find_all(attrs = {"class":"tabbertab"})[2]

	i = 1
	col = 1
	while i < 23:
		attributes = str(Home.find_all("td",{"align":"center"})[i].text)
		sheet.write(j,col,data)		
		i = i+3
		col = col +1

os.remove(excel_address)
wb.save(excel_address)
