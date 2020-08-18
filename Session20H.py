# import datetime
import datetime as dt

today = dt.datetime.today()
print(today)
print(type(today))

today = str(today)
print(today)
print(type(today))

date_time_stamp = today.split(" ")
print(date_time_stamp[0])   # Date
print(date_time_stamp[1])   # Time

today = dt.datetime.today()
tomorrow = dt.datetime(2020, 8, 19, 13, 00, 50, 0)
print(today)
print(tomorrow)

print(tomorrow - today)