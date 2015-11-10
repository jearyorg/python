#!/usr/bin/python
# encoding: utf-8
import urllib2
import re  
def get_url(u):   
  f = urllib2.urlopen(u)
  value = f.read()
  return value    
  f.close()
    
def ver(html):  
  ver = re.compile(r'''<span style='color:#666;font-site:12px;margin-left:7px; padding:0px;'>(.*?)</span>''').findall(html)
  return ver



if __name__ == "__main__":
	  #<span style='color:#666;font-site:12px;margin-left:7px; padding:0px;'>www.eastmoney.com</span>
      #u='http://top.chinaz.com/list.aspx?p=1&t='
      u = 'http://top.chinaz.com/list.aspx?t=202&p=';
      k=0;
      for x in xrange(1,23):
      	for i in ver(get_url(u+str(x))):
      		print i
      		k = k + 1;
      print k;		