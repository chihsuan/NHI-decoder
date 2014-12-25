NHI-decoder
===========
全民健保資料解碼程式 /  National Health Insurance data decoder

[codebook reference] (http://nhird.nhri.org.tw/date_02.htm)

## Description

This is a program to convert the NHI data from .dat format to json format and insert to database.

這是一個程式用來轉換健保資料從.dat格式成json格式，並儲存到資料庫中。

## Required

    pip install psycopg2


## Usage

+ fill up the `config_sample.json` and rename as `config.json`.

+ you can use `create_table.py` to create tables.



