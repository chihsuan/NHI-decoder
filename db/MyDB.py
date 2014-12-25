# !/usr/bin/evn python
# -*- coding: utf8 -*-

import MySQLdb
import psycopg2
import sys

class MyDB:

    def __init__(self, db_type, host, db_name, user, passwd, charset, port):
        self.db_type = db_type.lower();
        self.host = host
        self.db_name = db_name
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.port = port

        self.connectdb()

    def connectdb(self):
        try:
            if self.db_type == "mysql":
                self.db = MySQLdb.connect( host = self.host,
                        db = self.db_name,
                        user = self.user,
                        passwd = self.passwd,
                        charset = self.charset )
            elif self.db_type == "postgresql":
                self.db = psycopg2.connect( host = self.host,
                        database = self.db_name,
                        user = self.user,
                        password = self.passwd,
                        port = self.port )

                self.cursor = self.db.cursor()
        except:
            print "ERROR: in connectdb"


    def exe_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e    
            self.db.rollback()
            sys.exit(1)

    def select(self, sql):
        self.exe_sql(sql)
        return self.cursor.fetchall()

    def insert_data(self, table_name, key_list, data_list):

		sql = "INSERT INTO %s (%s" % table_name, key_list[0] 

		for i in range( 1, len(key_list) ):
			sql += "," + key_list[i]
		
		sql += ") VALUES ("
		for i in range( 0, len(data_list) ):
			if data_list[i]:	
				try: 
					sql += "'"+ data_list[i] + "',"
				except TypeError:	
					sql += "'"+ str(data_list[i]) + "',"
			else:
				sql += "' ',"

		sql = sql[0: len(sql) -1 ] + ");"
		self.doc_sql(sql, data_list[0])

    def show_info(self):
        self.cursor.execute( "SELECT VERSION()")
        data = self.cursor.fetchone()
        if data:
            print "Database version", data
    
    def close(self):
        self.db.commit()
        self.cursor.close()
        self.db.close()
