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
	is_cms ='CMS_Str'
	http = 'http://'
	j = 1
	for i in open("domain.txt"):
		j=j+1		
		try:
			html = get_url(http+i)
			if is_cms in html:
				print i.strip()+" >>>> is that cms!"
			else:
				print i.strip()+" >>>>>>>>>>>>>>>>>>>>  this is no!  <<<<<<<<<<<<<<<"
		except Exception, e:
			continue		
		finally:
			pass
	print "Count:"+j
		