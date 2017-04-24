# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 12:39:15 2017

@author: psilva
"""

import sys,getopt
import urllib3

def inf(argv):
    parse = ''
    website = ''
    try:
        opts,args = getopt.getopt(argv,"hp:w:",["parse=","website="])
    except getopt.GetoptError:
        print ('Something is weird - Try to use : cassandra_test.py -u <username> -p <password> -s <server> -k <keyspace> -q <query>')
        sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
           print ('cassandra_test.py -u <username> -p <password> -s <server> -k <keyspace> -q <query>')
           sys.exit()
       elif opt in ("-p", "--parse"):
           parse = arg
       elif opt in ("-w", "--website"):
           website = arg
    test_website(parse,website)

def test_website(parse,url):
    try:
        master = urllib3.PoolManager()        
        block = master.request('GET',url, timeout=0.5).data.decode("utf-8")
        if parse in block:
            print ('OK - 0')
    except Exception:
        print ('error - 1')
        sys.exit()

if __name__ == "__main__":
   inf(sys.argv[1:])  
