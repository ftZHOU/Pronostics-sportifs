import urllib2
from bs4 import BeautifulSoup
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://www.soccerstats.com/latest.asp?league=france"
request = urllib2.urlopen(url) 
response = request.read()#.decode('iso-8859-1').replace(u'\xa0', u' ').encode('utf-8')
#print response 
soup = BeautifulSoup(response,"html.parser")


# the 0th element is team name
all_teams_names = soup.find_all("table",{"id":"btable"})[2].find_all("a",{"target":"_top"})
for team_name in all_teams_names:
	print team_name.text

# the first element is rank
ranks = soup.find_all("table",{"id":"btable"})[2].find_all("td",{"height":"20"})
for rank in ranks:
	print rank.text

# the seconde element is games played
i = 0
while i <= 39:
	if (i % 2) ==0:
		GPs =soup.find_all("table",{"id":"btable"})[2].find_all("font",{"color":"green"})[i]
		print GPs.text
	i = i + 1

# the third element is games won
j = 0
while j <= 19 :
	W =soup.find_all("table",{"id":"btable"})[2].find_all("tr",class_ ="trow8")[j].find_all("td")[3]
	print W.text
	j=j+1

# the 4th element is Draws
j = 0
while j <= 19 :
	D =soup.find_all("table",{"id":"btable"})[2].find_all("tr",class_ ="trow8")[j].find_all("td")[4]
	print D.text
	j=j+1

# the 5th element is Lose
j = 0
while j <= 19 :
	L =soup.find_all("table",{"id":"btable"})[2].find_all("tr",class_ ="trow8")[j].find_all("td")[5]
	print int(L.text)
	j=j+1


# the 6th element is Goals For
i = 0
while i <= 39:
	if (i % 2) ==0:
		GF = soup.find_all("table",{"id":"btable"})[2].find_all("font",{"color":"blue"})[i]
		print GF.text
	i = i + 1

# the 7th element is Goals Against
i = 0
while i <= 39:
	if (i % 2) ==0:
		GA = soup.find_all("table",{"id":"btable"})[2].find_all("font",{"color":"red"})[i]
		print GA.text
	i = i + 1

# the 8th element is Goal difference
i = 0
while i <= 139:
	if (i % 7) ==0:
		GDs = ranks = soup.find_all("table",{"id":"btable"})[2].find_all("font",{"color":"gray"})[i]
		print GDs.text
	i = i + 1

# the 9th element is Points
Ptss = soup.find_all("table",{"id":"btable"})[2].find_all("font",{"size":"2"})
for Pts in Ptss:
	print Pts.text

# the 11th element is Points Per Game
i = 0
while i <= 39:
	if (i % 2) ==1:
		ppg = soup.find_all("table",{"id":"btable"})[2].find_all("font",{"color":"green"})[i]
		print ppg.text
	i = i + 1

# the 12th element is clean sheets
i = 0
while i <= 39:
	if (i % 2) == 1:
		cs = soup.find_all("table",{"id":"btable"})[2].find_all("font",{"color":"blue"})[i]
		print cs.text
	i = i + 1

# the 13th element is Failed to Score
i = 0
while i <= 39:
	if (i % 2) ==1:
		fts = soup.find_all("table",{"id":"btable"})[2].find_all("font",{"color":"red"})[i]
		print fts.text
	i = i + 1










