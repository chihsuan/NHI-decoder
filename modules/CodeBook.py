# !/usr/bin/evn python
# -*- coding: utf8 -*-

from CD import CD
from DD import DD
from DO import DO
from GD import GD
from GO import GO
from ID import ID
from OO import OO

class CodeBook:

    def __init__(self, path):
        self.CD = CD(path)
        self.DD = DD(path)
        self.DO = DO(path)
        self.GD = GD(path)
        self.GO = GO(path)
        self.ID = ID(path)
        self.OO = OO(path)

    def decode(self, code, encoding, year):

        if encoding == 'CD':
            return self.CD.decode(code, year)
        elif encoding == 'DD':
            return self.CD.decode(code, year)
        elif encoding == 'DO':
            return self.CD.decode(code, year)
        elif encoding == 'GD':
            return self.CD.decode(code, year)
        elif encoding == 'GO':
            return self.CD.decode(code, year)
        elif encoding == 'ID':
            return self.CD.decode(code, year)
        elif encoding == 'OO':
            return self.CD.decode(code, year)
        else:
            print 'Error: encoding do not found'
            exit(-1)

    def decode_file(self, filename, encoding, year):
        data = []
        f = open(filename)
        for line in f.readlines():
            code = self.decode(line[:-1], encoding, year)
            data.append(code)
        f.close()
        return data

