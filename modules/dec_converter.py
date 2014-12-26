# !/usr/bin/evn python
# -*- coding: utf-8 -*-

def dec_convert(code, codebook):
    data = {}
    for col, attrs in codebook.iteritems():
        if attrs['type'] != 'I':
            col = col.encode('utf-8')
            start = attrs['start']
            end = attrs['end']
            data[col] = code[start-1:end].replace(' ', '').replace("'", '"')
    return data

