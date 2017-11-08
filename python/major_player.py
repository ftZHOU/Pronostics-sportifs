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

excel_address = r'/Users/zhoufengting/Desktop/major_player_home_2013_2014.xls'
work_book = open_workbook(excel_address)
wb = copy(work_book)
sheet = wb.get_sheet(0)
raw = 0

# using same link list as in eurosport_table2
txt_path = r"/Users/zhoufengting/Desktop/href_2013_2014.txt"
fp = open(txt_path)
for url in fp:
	request = urllib2.urlopen(url)
	response = request.read()	
	soup = BeautifulSoup(response,"html.parser")
	Names_major = soup.find_all("ul",class_ = "players home-team")[0].find_all("li")
	for col in range(0,len(Names_major)):
		data = Names_major[col].find_all("span",class_="name")[0].text
		sheet.write(raw,col,data)
	raw = raw+1

os.remove(excel_address)
wb.save(excel_address)
