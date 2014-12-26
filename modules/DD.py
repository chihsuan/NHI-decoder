# !/usr/bin/evn python
# -*- coding: utf-8 -*-
import json_io
from dec_converter import dec_convert

class DD:

    def __init__(self, path):
        self.book_1996 = json_io.read_json(path + 'codebook_DD1996.json') 
        self.book_2004 = json_io.read_json(path + 'codebook_DD2004.json')
        self.book_2007 = json_io.read_json(path + 'codebook_DD2007.json')
        self.book_2012 = json_io.read_json(path + 'codebook_DD2012.json')

    def decode(self, code, year):

        if year >= 1996 and year <= 2003:
            return dec_convert(code, self.book_1996)
        elif year >= 2004 and year <= 2006:
            return dec_convert(code, self.book_2004)
        elif year >= 2007 and year <= 2011:
            return dec_convert(code, self.book_2007)
        elif year >= 2012:
            return dec_convert(code, self.book_2012)
        else:
            print 'Error: year do not found'
            exit(-1)
