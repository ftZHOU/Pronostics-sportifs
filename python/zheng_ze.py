import urllib2
import re

request = urllib2.Request("http://www.soccerstats.com/latest.asp?league=france")

try:
	response = urllib2.urlopen(request)
	content = response.read()
	#print content
	table3 = "<td height='22'>.*?<a href='team\.asp\?league.*?op'>(.*?)</a>.*?<font color='green'>(.*?)</font>.*?<td align='center'>(.*?)</TD>.*?<td align='center'>(.*?)</TD>.*?<td align='center'>(.*?)</TD>.*?<font color='blue'>(.*?)</font>.*?<font color='red'>(.*?)</font>.*?<td align='center'>(.*?)</TD>.*?b>(.*?)</b>"
	pattern = re.compile(table3,re.S)
	items = re.findall(pattern,content)
	#print items
	for item in items:
		print "team name:"+item[0]+"\n","GP:"+item[1],"W:"+item[2],"D:"+item[3],"L:"+item[4],"G:"+item[5],"F:"+item[6]
	
except urllib2.HTTPError,e:
	print e.code
except urllib2.URLError, e:
	print e.reason






