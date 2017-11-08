#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

import urllib2
from bs4 import BeautifulSoup
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#db = MySQLdb.connect("localhost","root","Nq4qVs7n","result_2014_ligue_1")
#cursor = db.cursor()

url = "http://www.eurosport.com/_ajax_/results_v8_5/results_teamsports_v8_5.zone?O2=1&langueid=0&domainid=135&sportid=22&revid=323&seasonid=88&mime=text%2fxml&site=&roundid=5171"
request = urllib2.urlopen(url) 
response = request.read()
#print response
soup = BeautifulSoup(response, "html.parser")
matches = soup.find_all(attrs = {"class":"match"})
#team = matches[0].find_all("span",class_ = "team__label")
#print team[0].text
Score_1 = int(matches[0].find_all(attrs = {"class":"match__score-text"})[0].text)
print Score_1
#sql = """INSERT INTO result_2014(Score_1)
#VALUE(%s) """
#cursor.execute(sql,(Score_1))


#lines = table.find_all("tr",class_ ="trow8")


