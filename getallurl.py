#!/usr/bin/python
# encoding: utf-8
import urllib2
import re  
def get_html(u):   
  f = urllib2.urlopen(u)    #利用urllib2类库，直接建立一个链接
  value = f.read()          # 调用读取访问
  f.close()                #关闭流
  return value           #返回结果
 
    
def ver(html):  
  ver = re.compile(r'''href="(.*)">''').findall(html)  #正则匹配所有href里面的
  return ver



if __name__ == "__main__":
      u='http://www.hao123.com'   #设置url 
      html = get_url(u)           #调用getHtml获取源码
      for u in ver(html):         #循环调用正则匹配所有链接
        print u          