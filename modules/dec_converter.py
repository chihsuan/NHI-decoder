# !/usr/bin/evn python
# -*- coding: utf8 -*-

def dec_convert(code, codebook):
    data = {}
    for col, attrs in codebook.iteritems():
        if attrs['type'] != 'I':
            start = attrs['start']
            end = attrs['end']
            if attrs['type'] == 'C':
                data[col] = code[start-1:end]
            elif attrs['type'] == 'N':
                data[col] = int(code[start-1:end])
    return data

