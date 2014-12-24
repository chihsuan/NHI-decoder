# !/usr/bin/evn python
# -*- coding: utf8 -*-
from dec_converter import dec_convert

class GO:

    def __init__(self, path):
        pass
        #self.book_1996 = json_io.read_json(path + 'codebook_CD1996.json') 
        #self.book_2007 = json_io.read_json(path + 'codebook_CD2004.json')
        #self.book_2012 = json_io.read_json(path + 'codebook_CD2010.json')

    def decode(self, code, year):

        if year >= 1996 and year <= 2006:
            return dec_convert(code, self.book_1996)
        elif year >= 2007 and year <= 2011:
            return dec_convert(code, self.book_2007)
        elif year >= 2012:
            return dec_convert(code, self.book_2012)
        else:
            print 'Error: year do not found'
            exit(-1)
