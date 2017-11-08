# collect data from soccerstat and stock it in an excel file #

import urllib2
from bs4 import BeautifulSoup
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from xlrd import open_workbook 
from xlwt import easyxf
from xlutils.copy import copy
import os

# stock all data in an existing workbook excel
excel_address = r'/Users/zhoufengting/projet/soccerstat_1.xls'
work_book = open_workbook(excel_address)
wb = copy(work_book)
sheet = wb.get_sheet(0)

# get the website link
url = "http://www.soccerstats.com/latest.asp?league=france"
request = urllib2.urlopen(url) 
response = request.read()
soup = BeautifulSoup(response,"html.parser")

# the table to be downlode is table3
table = soup.find_all("table",{"id":"btable"})[3]
lines = table.find_all("tr",class_ ="trow8")
line_nb = len(lines)
list_nb = len(lines[0].find_all("td"))



# catch and save every element in table 2 to the file excel
# find all the online elements line by line
for raw in range(0,line_nb):
	for col in range(0,list_nb):
		data = lines[raw].find_all("td")[col].text
		sheet.write(raw,col,data)

os.remove(excel_address)
wb.save(excel_address)


