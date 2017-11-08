#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

import urllib2
from bs4 import BeautifulSoup
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

for j in range(5171,5209):
	url = "http://www.eurosport.com/_ajax_/results_v8_5/results_teamsports_v8_5.zone?O2=1&langueid=0&domainid=135&sportid=22&revid=323&seasonid=92&mime=text%2fxml&site=&roundid="+str(j)
	request = urllib2.urlopen(url) 
	response = request.read()
	soup = BeautifulSoup(response,"html.parser")
	matches = soup.find_all(attrs = {"class":"match"})
	for match in matches:
		hrefs_matches = soup.find_all("a")
		for href_match in hrefs_matches:
			url_match = "http://www.eurosport.com"+href_match['href']
			request = url_match.urlopen(url_match)
		#Team_1 = match.find_all("span",class_ = "team__label")[0].text
		#Team_2 = match.find_all("span",class_ = "team__label")[1].text
		#Score_1 = int(match.find_all(attrs = {"class":"match__score-text"})[0].text)
		#Score_2 = int(match.find_all(attrs = {"class":"match__score-text"})[1].text)
		#print Score_2