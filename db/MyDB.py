# !/usr/bin/evn python
# -*- coding: utf-8 -*-

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
                self.cursor = self.db.cursor()
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
        #print sql
        self.cursor.execute(sql)

    def commit(self):
        try:
            self.db.commit()
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e    
            self.db.rollback()
            sys.exit(1)
    
    def select(self, sql):
        self.exe_sql(sql)
        return self.cursor.fetchall()

    def insert(self, table_name, key_list, data_list):

		sql = "INSERT INTO %s (%s" % (table_name, key_list[0])

		for i in range(1, len(key_list)):
			sql += "," + key_list[i]
		
		sql += ") VALUES ("
		for i in range(0, len(data_list)):
			try: 
				sql += "'"+ data_list[i].encode('utf-8') + "',"
			except TypeError:	
				sql += "'"+ str(data_list[i]) + "',"

		sql = sql[0:len(sql)-1] + ");"
		self.exe_sql(sql)

    def create_table(self, table_name, key_list, len_list):
        sql = ("CREATE TABLE IF NOT EXISTS %s ( " % table_name)
        for i in range(0, len(key_list)-1):
            sql += key_list[i].encode('utf-8') 
            sql += ' varchar(' + str(len_list[i][u'length']) + '),'

        sql += key_list[-1].encode('utf-8') 
        sql += ' varchar(' + str(len_list[-1][u'length']) + ") );"
        self.exe_sql(sql)

    def show_info(self):
        self.cursor.execute( "SELECT VERSION()")
        data = self.cursor.fetchone()
        if data:
            print "Database version", data
    
    def close(self):
        self.db.commit()
        self.cursor.close()
        self.db.close()
