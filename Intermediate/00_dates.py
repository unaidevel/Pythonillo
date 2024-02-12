### Dates ###

from datetime import datetime

now = datetime.now()

# Datetime que es capaz de aglutinar los dos tipos de datos.
#Date es capaz de agrupar la parte de fecha
#Time capaz de agrupar la parte de hora

def print_name(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)   
    print(date.timestamp())


timestamp = now.timestamp()
print (timestamp)


year_2024 = datetime(2024, 1, 1)
print_name(year_2024)

from datetime import time

current_time = time(21, 5, 1)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)


diff = year_2024 - now
print(diff)


diff = year_2024.date() - current_date
print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta + start_timedelta)
print(end_timedelta - start_timedelta)

