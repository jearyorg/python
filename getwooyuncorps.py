import urllib2
import sgmllib
class LinksParser(sgmllib.SGMLParser):  
  urls = []  
  def do_a(self, attrs):
    for name, value in attrs:  
      if name == 'href' and value not in self.urls:  
        if value.startswith('http'):  
          self.urls.append(value)  
          print value  
      else:  
        continue  
      return

def get_url(uu):
  p =  LinksParser()
  u = uu
  f = urllib2.urlopen(u)
  value = f.read()
  p.feed(value)
  for url in p.urls:
     print url
  f.close()
  p.close()

if __name__ == "__main__":
  for x in xrange(1,28):
    s = str(x)
    get_url('http://wooyun.org/corps/page/'+s)