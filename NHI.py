#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os

from modules.CodeBook import CodeBook


if __name__=='__main__':

    code_book = CodeBook('modules/codebook/')
    code = '1997011f7fbd30c87e1a2701619ac271fa01788351997020401000437        0019970114        193102  699e30e5ba39d9c696f5d19faebfa370B2 4D10A432               02001d3db99b8dae387a4a62b7718d3821b                                000000700000000001004C      0000022005204D      00000010  000003000000005000000250M'
    print code_book.decode(code, 'CD', 1997)
