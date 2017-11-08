import urllib2
from bs4 import BeautifulSoup
import re

from xlrd import open_workbook 
from xlwt import easyxf
from xlutils.copy import copy
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# get a workbook to deposit all the data
excel_address = r'/Users/zhoufengting/projet/donnee.xls'
work_book = open_workbook(excel_address,formatting_info = True)
wb = copy(work_book)
sheet = wb.get_sheet(0)
col = 0;
raw = 0;

url = "http://www.soccerstats.com/latest.asp?league=france"
request = urllib2.urlopen(url) 
response = request.read()#.decode('iso-8859-1').replace(u'\xa0', u' ').encode('utf-8')
#print response 
soup = BeautifulSoup(response,"html.parser")


# the first element is rank
ranks = soup.find_all("table",{"id":"btable"})[2].find_all("td",{"height":"20"})
#print len(ranks)
#print ranks[0].text
for rank in ranks:
	sheet.write(raw,col,int(rank.text))
	raw = raw + 1
os.remove(excel_address)
wb.save(excel_address)
#for rank in ranks:
#	rank_int = int(rank.text)
#	while rank.text!= null:
#		sheet.write(col,raw,rank_int)
#		raw = raw + 1
#os.remove(excel_address)
#wb.save(excel_address)
	
	#print int(rank.text)



# build a list to consult the value of each element
#dict1 = dict.fromkeys(("name","Rk","GP","W","D","L","GF","GD","Pts","ppg","cs","fts"), None)
#print x


#items = soup.find_all("table",{"id":"btable"})[1].find_all("td",{"align":"center"})
#for item in items:
	#print item.text
