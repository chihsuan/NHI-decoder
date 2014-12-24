# !/usr/bin/evn python
# -*- coding: utf8 -*-
import json_io
from dec_converter import dec_convert

class CD:

    def __init__(self, path):
        self.book_1997 = json_io.read_json(path + 'codebook_CD1997.json') 
        #self.book_2004 = json_io.read_json(path + 'codebook_CD2004.json')
        #self.book_2012 = json_io.read_json(path + 'codebook_CD2012.json')

    def decode(self, code, year):

        if year >= 1997 and year <= 2003:
            return dec_convert(code, self.book_1997)
        elif year >= 2004 and year <= 2011:
            return dec_convert(code, self.book_2004)
        elif year >= 2012:
            return dec_convert(code, self.book_2012)
        else:
            print 'Error: year do not found'
            exit(-1)
