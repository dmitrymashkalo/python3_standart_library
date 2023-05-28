# Datetime Module
from datetime import datetime

now = datetime.now()

# Date
print(now.date()) # Get current date 'year-month-day'
print(now.year)
print(now.month)
print(now.day)

# Time
print(now.time()) # Get current time 'hour-minute-second'
print(now.hour)
print(now.minute)
print(now.second)


# Getting More Control Over Formatting
# Days
# %a - abbreviated day of week: Mon, Tues, Wed...
# %A - full name of day of week: Monday, Tuesday, Wednesday
# %d - day of month: number 10 for the 10th of month 
print(now.strftime('%a %A %d'))


# Months
# %b - avvreviated month name: Jan, Feb
# %B - full month name: January
# %m - month as number: 01 for January
print(now.strftime('%b %B %m'))


# Times
# %H - hours
# %M - minutes
# %S - seconds
# $p - p.m or a.m
print(now.strftime('%H:%M:%S %p'))


# Years
# %y - avvreviated year as two numbers: 23
# %Y - year as four numbers: 2023
print(now.strftime('%y %Y'))