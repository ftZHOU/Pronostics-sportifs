#!/usr/bin/python
# -*- coding: UTF-8 -*-


# in order to get table_2 from eurosport, first have to get the link list for all 380 matches during a year


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
	hrefs_matches = soup.find_all("a")
	for href_match in hrefs_matches:
		url_match = "http://www.eurosport.com"+href_match['href']
		#print url_match 
		
