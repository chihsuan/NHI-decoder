#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os

from modules.CodeBook import CodeBook

if __name__=='__main__':

    if len(sys.argv) != 2:
        print 'Error argv1 should be data folder'
        eixt(-1)

    codebook = CodeBook('modules/codebook/')
    
    for root, _, files in os.walk(sys.argv[1]):
        for f in files:
            encoding = f[5:7]
            year = int(f[7:11])
            data = codebook.decode_file(root+f, encoding, year)

