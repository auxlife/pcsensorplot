#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import commands
import os

logfile = '/var/log/pcsensor.log' 
errfile = '/var/log/pcsensor.err'

if os.path.exists(logfile):
        openmethod = 'a'
else:
        openmethod = 'w'
logfile = open(logfile, openmethod)

if os.path.exists(errfile):
        openmethod = 'a'
else:
        openmethod = 'w'
errfile = open(errfile, openmethod)

output = commands.getoutput('/usr/local/bin/pcsensor')
cols = output.split()
output = output + '\n'
try:
    con = mdb.connect('DBHOST', 'DBUSER', 'DMPASS', 'DB');
    cur = con.cursor()
    sql = "INSERT INTO `readings` (`ID`, `datetime`, `temp`) VALUES (NULL, '" + cols[0].replace('/','-') + " " + cols[1] +"', '"+cols[3][:-1]+"')"
    cur.execute(sql)
    con.commit()
    logfile.write(output)
except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    errfile.write(output)
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()


errfile.close()
logfile.close()
