#coding=utf-8
import urllib2,urllib
import simplejson
                                  
seachstr = 'site:baidu.com'
                                  
for x in range(10):
    print "page:%s"%(x+1)
    page = x * 8
                                      
    url = ('https://ajax.googleapis.com/ajax/services/search/web'
                  '?v=1.0&q=%s&rsz=8&start=%s') % (urllib.quote(seachstr),page)
    try:        
        request = urllib2.Request(
        url, None, {'Referer': 'http://www.google.com.hk'})
        response = urllib2.urlopen(request)                          
        
        results = simplejson.load(response)
        infoaaa = results['responseData']['results']
    except Exception,e:
        print e
        print url
    else:
        for minfo in infoaaa:
            print minfo['url']