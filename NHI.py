#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os

from modules.CodeBook import CodeBook
from db.MyDB import MyDB

if __name__=='__main__':

    config = json_io.read_json('config.json')
    codebook = CodeBook(config[u'codebook'][u'path'])
    
    db_config = config[u'database']
    mydb = DataDB( db_config[u'dbtype'], db_config[u'host'], db_config[u'dbname'], \
            db_config[u'username'], db_config[u'password'], db_config[u'encoding'], "")
    
    for root, _, files in os.walk(config[u'data'][u'folder_path']):
        for f in files:
            encoding = f[5:7]
            year = int(f[7:11])
            data = codebook.decode_file(root+f, encoding, year)
            
