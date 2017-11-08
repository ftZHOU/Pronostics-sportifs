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

excel_address = r'/Users/zhoufengting/Desktop/replacingg_player_2013_2014.xls'
work_book = open_workbook(excel_address)
wb = copy(work_book)
sheet = wb.get_sheet(0)
raw = 0

txt_path = r"/Users/zhoufengting/Desktop/href_2013_2014.txt"
fp = open(txt_path)
for url in fp:
	request = urllib2.urlopen(url)
	response = request.read()	
	soup = BeautifulSoup(response,"html.parser")
	Names_replacing = soup.find_all("ul",class_ = "players home-team")[0].find_all("span",class_="replacement")
	#print len(Names_replacing)
	for col in range(0,len(Names_replacing)):

		data = Names_replacing[col].text
		sheet.write(raw,col,data)
	raw = raw+1

os.remove(excel_address)
wb.save(excel_address)