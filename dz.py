#!/usr/bin/python
# encoding: utf-8
import urllib2
import re  
def get_url(u):   
  f = urllib2.urlopen(u)
  value = f.read()
  return value    
  f.close() 
def txt_wrap_by(start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()

if __name__ == "__main__":
      #u='http://home.artsbj.com/home.php?mod=space&uid=1&do=profile'
      guanli='http://example.com/home.php?mod=spacecp&amp;ac=usergroup&amp;gid=1"'     
      for x in xrange(1,1000):
         html = get_url('http://example.com/home.php?mod=space&uid='+str(x)+'&do=profile')               
         if guanli in html:
            print txt_wrap_by('<h2 class="mbn">','<',html)+"-"+str(x)
         else:
           #print str(x)+"-no"
           pass
