#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

import urllib2
from bs4 import BeautifulSoup
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# I have created a database by terminal whose name is test #
db = MySQLdb.connect("localhost","root","Nq4qVs7n","france_ligue_1")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS result_2014")
sql_order = """CREATE TABLE result_2014(
Team_1 varchar(255),
Team_2 varchar(255),
Score_1 int,
Score_2 int
)"""
cursor.execute(sql_order)

# stock all data in the DB

for j in range(5171,5209):
	url = "http://www.eurosport.com/_ajax_/results_v8_5/results_teamsports_v8_5.zone?O2=1&langueid=0&domainid=135&sportid=22&revid=323&seasonid=90&mime=text%2fxml&site=&roundid="+str(j)
	request = urllib2.urlopen(url) 
	response = request.read()
	soup = BeautifulSoup(response,"html.parser")
	matches = soup.find_all(attrs = {"class":"match"})
	for match in matches:
		Team_1 = match.find_all("span",class_ = "team__label")[0].text
		Team_2 = match.find_all("span",class_ = "team__label")[1].text
		Score_1 = int(match.find_all(attrs = {"class":"match__score-text"})[0].text)
		Score_2 = int(match.find_all(attrs = {"class":"match__score-text"})[1].text)
		sql = """INSERT INTO result_2014(Team_1,Team_2,Score_1,Score_2)
				VALUES (%s,%s,%s,%s)"""
		cursor.execute(sql,(Team_1,Team_2,Score_1,Score_2))
		db.commit()




db.close

#nb_match = len(soup.findAll(attrs = {"class":"match__score-text"}))


    


