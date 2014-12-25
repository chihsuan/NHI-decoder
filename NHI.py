#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os

from modules import json_io
from modules.CodeBook import CodeBook
from db.MyDB import MyDB

def get_table_name(table_dic, encoding, year):
    category = table_dic[encoding.decode('utf-8')]
    for table_name, years in category.iteritems():
        if year >= years[0] and year <= years[1]:
            return table_name

if __name__=='__main__':
    '''
    Read NHI .dat fromat data, decode and insert to db 
    '''

    config = json_io.read_json('config.json')
    codebook = CodeBook(config[u'codebook'][u'path'])
    
    db_config = config[u'database']
    mydb = MyDB( db_config[u'dbtype'], db_config[u'host'], db_config[u'dbname'], \
            db_config[u'username'], db_config[u'password'], db_config[u'encoding'], None)
    
    table_dic = config[u'table']

    for root, _, files in os.walk(config[u'data'][u'folder_path']):
        for f in files:
            encoding = f[5:7]
            year = int(f[7:11])
            data = codebook.decode_file(root+f, encoding, year)
            table_name = get_table_name(table_dic, encoding, year)
            for row in data:
                mydb.insert(table_name, row.keys(), row.values())
