#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
from bs4 import BeautifulSoup
import re

f = open("/Users/zhoufengting/Desktop/possession1.txt","r")

lines = f.readlines()

for line in lines:
	url = line
	request = urllib2.urlopen(url) 
	response = request.read()
	soup = BeautifulSoup(response,"html.parser")
	time = soup.find_all
	

