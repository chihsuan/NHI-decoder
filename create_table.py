#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from modules import json_io
from db.MyDB import MyDB


if __name__=='__main__':
    
    codebook_path = 'modules/codebook/'

    config = json_io.read_json('config.json')

    db_config = config[u'database']
    mydb = MyDB( db_config[u'dbtype'], db_config[u'host'], db_config[u'dbname'], \
            db_config[u'username'], db_config[u'password'], db_config[u'encoding'], "")

    tables = config[u'table']

    for category, table_info in tables.iteritems():
        for name, years in table_info.iteritems():
            f = codebook_path + 'codebook_' + name[:6] + '.json'
            table_format = json_io.read_json(f)
            mydb.create_table(name, table_format.keys(), table_format.values())
    mydb.close()
