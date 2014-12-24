# !/usr/bin/evn python
# -*- coding: utf8 -*-
from dec_converter import dec_convert

class GD:

    def __init__(self, path):
        pass
        #self.book_1996 = json_io.read_json(path + 'codebook_CD1996.json') 
        #self.book_1999 = json_io.read_json(path + 'codebook_CD1999.json')
        #self.book_2004 = json_io.read_json(path + 'codebook_CD2004.json')
        #self.book_2010 = json_io.read_json(path + 'codebook_CD2010.json')

    def decode(self, code, year):

        if year >= 1996 and year <= 1998:
            return dec_convert(code, self.book_1996)
        elif year >= 1999 and year <= 2008:
            return dec_convert(code, self.book_1999)
        elif year >= 2004 and year <= 2009:
            return dec_convert(code, self.book_2004)
        elif year >= 2010:
            return dec_convert(code, self.book_2010)
        else:
            print 'Error: year do not found'
            exit(-1)
