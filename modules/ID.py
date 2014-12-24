# !/usr/bin/evn python
# -*- coding: utf8 -*-
import json_io
from dec_converter import dec_convert

class ID:

    def __init__(self, path):
        pass
        #self.book_1996 = json_io.read_json(path + 'codebook_CD1997.json') 
        #self.book_2010 = json_io.read_json(path + 'codebook_CD2004.json')

    def decode(self, code, year):

        if year <= 2009:
            return dec_convert(code, self.book_1996)
        elif year >= 2010:
            return dec_convert(code, self.book_2010)
        else:
            print 'Error: year do not found'
            exit(-1)

