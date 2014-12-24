# !/usr/bin/evn python
# -*- coding: utf8 -*-
from dec_converter import dec_convert

class DD:

    def __init__(self, path):
        pass
        #self.book_1996 = json_io.read_json(path + 'codebook_CD1996.json') 
        #self.book_2004 = json_io.read_json(path + 'codebook_CD2004.json')
        #self.book_2007 = json_io.read_json(path + 'codebook_CD2007.json')

    def decode(self, code, year):

        if year >= 1996 and year <= 2003:
            return dec_convert(code, self.book_1996)
        elif year >= 2004 and year <= 2006:
            return dec_convert(code, self.book_2004)
        elif year >= 2007:
            return dec_convert(code, self.book_2007)
        else:
            print 'Error: year do not found'
            exit(-1)
