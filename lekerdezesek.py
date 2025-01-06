#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import MySQLdb
from time import gmtime, strftime

def szulinap():
 most = strftime("%m-%d")
 db = MySQLdb.connect("localhost","db_user","db_password","db_name",charset="utf8",use_unicode=True)
 cursor = db.cursor()
 cursor.execute("""SELECT nev FROM szulinap WHERE szulinap=%s""", (most,) )
 results = cursor.fetchall()
 rc = cursor.rowcount
 if str(rc) == "0":
    visszateresiertek = "0"
    return str(visszateresiertek)
 else:
    for row in results:
     visszateresiertek = row[0]
     return str(visszateresiertek)

def lefutottmost():
 most = strftime("%Y-%m-%d %H:%M:%S")
 db1 = MySQLdb.connect("localhost","db_user","db_password","db_name",charset="utf8",use_unicode=True)
 cursor1 = db1.cursor()
 cursor1.execute("""UPDATE run_dates SET szulinap=%s""", (most,) )
 data1=cursor1.fetchall()
 db1.commit()