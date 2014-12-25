# !/usr/bin/evn python
# -*- coding: utf8 -*-
import json_io
from dec_converter import dec_convert

class GD:

    def __init__(self, path):
        self.book_1996 = json_io.read_json(path + 'codebook_GD1996.json') 
        self.book_1999 = json_io.read_json(path + 'codebook_GD1999.json')
        self.book_2004 = json_io.read_json(path + 'codebook_GD2004.json')
        self.book_2010 = json_io.read_json(path + 'codebook_GD2010.json')
        self.book_2012 = json_io.read_json(path + 'codebook_GD2012.json')

    def decode(self, code, year):

        if year >= 1996 and year <= 1998:
            return dec_convert(code, self.book_1996)
        elif year >= 1999 and year <= 2008:
            return dec_convert(code, self.book_1999)
        elif year >= 2004 and year <= 2009:
            return dec_convert(code, self.book_2004)
        elif year >= 2010 and year <= 2011:
            return dec_convert(code, self.book_2010)
        elif year >= 2010:
            return dec_convert(code, self.book_2012)
        else:
            print 'Error: year do not found'
            exit(-1)
