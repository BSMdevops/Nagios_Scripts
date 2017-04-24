# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:52:39 2017

@author: psilva
"""
import sys, getopt
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def inf(argv):
    user = ''
    passwd = ''
    server = ''
    key = ''
    query = ''
    try:
        opts,args = getopt.getopt(argv,"hu:p:s:k:q:",["user=","passwd=","server=","keyspace=","query="])
    except getopt.GetoptError:
        print ('Something is weird - Try to use : cassandra_test.py -u <username> -p <password> -s <server> -k <keyspace> -q <query>')
        sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
           print ('cassandra_test.py -u <username> -p <password> -s <server> -k <keyspace> -q <query>')
           sys.exit()
       elif opt in ("-u", "--user"):
           user = arg
       elif opt in ("-p", "--passwd"):
           passwd = arg
       elif opt in ("-s", "--server"):
           server = arg
       elif opt in ("-k", "--keyspace"):
           key = arg
       elif opt in ("-q", "--query"):
           query = arg
    consulta(user,passwd,server,key,query)

def consulta(user,passwd,server,key,query):
    try:
        auth_provider = PlainTextAuthProvider(username=user, password=passwd)
        cluster = Cluster([server],auth_provider=auth_provider)
        session = cluster.connect()
        session.set_keyspace(key)
        session.execute(query)
        cluster.shutdown()        
        print ('Ok - 0')
        sys.exit(1)
    except Exception:
        print ('error - 1')
        sys.exit(1)
if __name__ == "__main__":
   inf(sys.argv[1:])

#consulta("cassandra","p@ssw3rd","172.16.128.73","fc_att","select * from wo_report limit 1")