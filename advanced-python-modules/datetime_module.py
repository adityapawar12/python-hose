"""
    DATETIME MODULE
"""

import datetime

my_time = datetime.time(1,20,34,26)
my_date = datetime.date(2021,10,12)
my_datetime = datetime.datetime(2021,10,12,1,20,35,12)
today = datetime.date.today()

print(today)
print(my_time)
print(my_date)
print(my_datetime)
print(my_datetime.day)
print(my_datetime.year)
print(my_datetime.hour)
print(my_datetime.ctime())

my_datetime = my_datetime.replace(year=2020)
print(my_datetime)

date1 = datetime.date(2001, 1, 1)
date2 = datetime.date(2003, 1, 1)
date_rslt = date2 - date1
type(date_rslt)
print(date_rslt)
print(date_rslt.days)

datetime1 = datetime.datetime(2001, 1, 1, 12, 0, 0, 0)
datetime2 = datetime.datetime(2005, 1, 1, 5, 0, 0, 0)
datetime_rslt = datetime2 - datetime1
type(datetime_rslt)
print(datetime_rslt)
print(datetime_rslt.days)
print(datetime_rslt.seconds)
print(datetime_rslt.total_seconds())
