#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Test
"""
import datetime

index_format = "%Y.%m.%d"
earliest_to_keep = datetime.date.today() - datetime.timedelta(
    days=int('2'))
earliest_to_keep = earliest_to_keep.strftime(index_format)
earliest_to_keep = datetime.datetime.strptime(earliest_to_keep, index_format)
index_date = "2018.12.8"
index_date = datetime.datetime.strptime(index_date, index_format)
print(earliest_to_keep)
print(index_date)
diff = earliest_to_keep-index_date
if earliest_to_keep-index_date:
    print("good")
else:
    print("bad")
