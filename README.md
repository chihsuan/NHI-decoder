NHI-decoder
===========
全民健保資料解碼程式 /  National Health Insurance data decoder

[codebook reference] (http://nhird.nhri.org.tw/date_02.htm)

## Description

This is a program which convert the NHI data from `.dat` format to `json` format and insert to the database.

這是一個用來將健保資料從`.dat`格式轉換成`json`格式並儲存到資料庫中的程式。

## Required

    sudo pip install psycopg2


## Usage

### config

fill out the `config_sample.json` and rename as `config.json`.

### create tables

    python create_table.py

### convert and insert

    python NHI.py





