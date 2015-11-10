#encoding=gbk

import httplib

import threading

import Queue





lock = threading.Lock()

queue = Queue.Queue()



def scan_http_service():

    while True:

        try:

            item = queue.get(timeout=1.0)

        except:

            break

        for i in range(3):

            try:

                conn = httplib.HTTPConnection('tuanbai.baidu.com', timeout=3)

                url = 'http://%s:%s/' % (item['ip'], item['port'])

                conn.request('GET', '/apiCheckv1/?url=' + url)

                html_doc = conn.getresponse().read().decode('gbk')

                conn.close()

                if html_doc.find(u'从API 获取数据不符合我们规定的XML格式') >= 0:

                    lock.acquire()

                    print '\n[Alive]',url

                    lock.release()

                    break

                else:

                    print '.',

            except Exception, e:

                pass





for port in [80, 8080, 8888]:

    for i in range(1, 256):    

        queue.put({'ip': '10.42.7.%s' % i, 'port': port})



threads = []

for i in range(10):

    t = threading.Thread(target=scan_http_service)

    t.start()

    threads.append(t)

for t in threads:

    t.join()

    

print 'All Done'