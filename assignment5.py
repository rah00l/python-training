Assignment 5

1. Write a Python script to display the various Date Time formats -
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week


# :: Solution ::

import datetime

# Current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

# Current year
current_year = current_datetime.year
print("Current year:", current_year)

# Month of year
current_month = current_datetime.strftime("%B")  # Full month name
print("Month of year:", current_month)

# Week number of the year
week_number = current_datetime.strftime("%U")  # Week number of the year
print("Week number of the year:", week_number)

# Weekday of the week
weekday = current_datetime.strftime("%A")  # Full weekday name
print("Weekday of the week:", weekday)

# Day of year
day_of_year = current_datetime.strftime("%j")  # Day number of the year
print("Day of the year:", day_of_year)

# Day of the month
day_of_month = current_datetime.day
print("Day of the month:", day_of_month)

# Day of week (numeric)
day_of_week_numeric = current_datetime.weekday()  # Monday is 0 and Sunday is 6
print("Day of the week (numeric):", day_of_week_numeric)


# Sample Output:

Current date and time: 2024-10-06 05:53:37.964000
Current year: 2024
Month of year: October
Week number of the year: 40
Weekday of the week: Sunday
Day of the year: 280
Day of the month: 6
Day of the week (numeric): 6


--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

2. Write a Python program to determine whether a given year is a leap year.

# :: Solution ::

def is_leap_year(year):
    # A leap year is divisible by 4
    # If it is divisible by 100, it must also be divisible by 400
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Input: ask the user for a year
year = int(input("Enter a year: "))

# Output: Check if the entered year is a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

3. Write a Python program to convert a string to datetime.
Sample String : Jul 1 2014 2:43PM
Expected Output : 2014-07-01 14:43:00

# :: Solution ::

from datetime import datetime
date_string = "Jul 1 2014 2:43PM"

date_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')

print(date_object)

#=>
2014-07-01 14:43:00

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

4. Write a Python program to get the current time in Python.
Sample Format :  13:19:49.078205

# :: Solution ::

from datetime import datetime

# Get the current time with microseconds
current_time = datetime.now()

# Print the current time including microseconds
print("Current time:", current_time.time())

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

5. Write a Python program to subtract five days from the current date.
Sample Date :
Current Date : 2015-06-22
5 days before Current Date : 2015-06-17


# :: Solution ::

from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Subtract five days from the current date
five_days_before = current_date - timedelta(days=5)

# Print the results
print("Current Date :", current_date.strftime('%Y-%m-%d'))
print("5 days before Current Date :", five_days_before.strftime('%Y-%m-%d'))

# Sample Output:
Current Date : 2023-10-06
5 days before Current Date : 2023-10-01

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 


6. Write a Python program to convert a Unix timestamp string to a readable date.
Sample Unix timestamp string : 1284105682
Expected Output : 2010-09-10 13:31:22

# :: Solution ::
from datetime import datetime

# Sample Unix timestamp string
timestamp_string = "1284105682"

# Convert the timestamp string to an integer
timestamp = int(timestamp_string)

# Convert the Unix timestamp to a readable date
readable_date = datetime.fromtimestamp(timestamp)

# Print the results
print("Readable Date:", readable_date.strftime('%Y-%m-%d %H:%M:%S'))


# Output:
Readable Date: 2010-09-10 13:31:22

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

7. Write a Python program to print yesterday, today, tomorrow.

# :: Solution ::

from datetime import datetime, timedelta

# Get today's date
today = datetime.now()

# Calculate yesterday and tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

# Print the results
print("Yesterday:", yesterday.strftime('%Y-%m-%d'))
print("Today:", today.strftime('%Y-%m-%d'))
print("Tomorrow:", tomorrow.strftime('%Y-%m-%d'))

# Output:
Yesterday: 2024-10-05
Today: 2024-10-06
Tomorrow: 2024-10-07
--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

8. Write a Python program to convert the date to datetime (midnight of the date) in Python.
Sample Output : 2015-06-22 00:00:00

# :: Solution ::

from datetime import datetime, date

# Sample date
sample_date = date(2015, 6, 22)

# Convert to datetime at midnight
# datetime.min.time(), which represents midnight (00:00:00)
midnight_datetime = datetime.combine(sample_date, datetime.min.time())

# Print the result
print("Converted datetime:", midnight_datetime)

# Output:
Converted datetime: 2015-06-22 00:00:00

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

9. Write a Python program to print the next 5 days starting today.

# :: Solution ::

from datetime import datetime, timedelta

# Get today's date
today = datetime.now()

# Print today's date
print("Today:", today.date())

# Print the next 5 days
print("Next 5 days:")
for i in range(1, 6):
    next_day = today + timedelta(days=i)
    print(next_day.date())


# Output:
Today: 2024-10-06
Next 5 days:
2024-10-07
2024-10-08
2024-10-09
2024-10-10
2024-10-11

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

10. Write a Python program to add 5 seconds to the current time.
Sample Data :
13:28:32.953088
13:28:37.953088

# :: Solution ::

from datetime import datetime, timedelta

# Get the current time
current_time = datetime.now().time()

# Print the current time
print("Current Time:", current_time)

# Create a timedelta of 5 seconds
time_to_add = timedelta(seconds=5)

# Add 5 seconds to the current time
new_time = (datetime.combine(datetime.today(), current_time) + time_to_add).time()

# Print the new time
print("New Time after adding 5 seconds:", new_time)


# Output:
Current Time: 06:34:18.961000
New Time after adding 5 seconds: 06:34:23.961000

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

11. Write a Python program to convert Year/Month/Day to Day of Year in Python.

# :: Solution ::

from datetime import datetime

# Function to convert Year/Month/Day to Day of Year
def convert_to_day_of_year(year, month, day):
    # Create a date object
    date_obj = datetime(year, month, day)
    # Get the day of the year
    day_of_year = date_obj.timetuple().tm_yday
    return day_of_year

# Sample input
year = 2023
month = 10
day = 6

# Convert and print the result
day_of_year = convert_to_day_of_year(year, month, day)
print(f"Date: {year}/{month}/{day} is the {day_of_year} day of the year.")


# Output:
Date: 2023/10/6 is the 279 day of the year.

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

12. Write a Python program to get the current time in milliseconds in Python.

# :: Solution ::

import time

# Get the current time in milliseconds
current_time_millis = int(time.time() * 1000)

# Print the current time in milliseconds
print(f"Current time in milliseconds: {current_time_millis}")

# Output:
Current time in milliseconds: 1728177247908

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

13. Write a Python program to get the week number.
Sample Date : 2015, 6, 16
Expected Output : 25

# :: Solution ::
from datetime import datetime

# Get the current date
current_date = datetime.now()

# Get the week number of the year
week_number = current_date.isocalendar()[1]

# Print the current date and the week number
print(f"Current Date: {current_date.strftime('%Y-%m-%d')}")
print(f"Week Number: {week_number}")

# Output:
Current Date: 2024-10-06
Week Number: 40

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

14. Write a Python program to find the date of the first Monday of a given week.
Sample Year and week : 2015, 50
Expected Output : Mon Dec 14 00:00:00 2015

# :: Solution ::
from datetime import datetime, timedelta

def first_monday(year, week):
    # Calculate the first day of the specified week
    # The first_monday function takes year and week as parameters and calculates 
    # the date of the first Monday of that week using the fromisocalendar() method.
    first_day_of_week = datetime.fromisocalendar(year, week, 1)  # 1 corresponds to Monday
    return first_day_of_week

# Sample Year and Week
year = 2015
week = 50

# Get the date of the first Monday of the specified week
date_of_first_monday = first_monday(year, week)

# Print the result
print(f"First Monday of week {week} in {year}: {date_of_first_monday.strftime('%a %b %d %H:%M:%S %Y')}")

# Output:
First Monday of week 50 in 2015: Mon Dec 07 00:00:00 2015
--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

15. Write a Python program to select all the Sundays in a specified year.

# :: Solution ::

from datetime import datetime, timedelta

def get_sundays(year):
    # List to store all Sundays
    sundays = []
    
    # Start from January 1 of the specified year
    date = datetime(year, 1, 1)
    
    # Loop through all days of the year
    while date.year == year:
        # Check if the day is a Sunday (0 = Monday, 6 = Sunday)
        if date.weekday() == 6:  # 6 corresponds to Sunday
            sundays.append(date)
        date += timedelta(days=1)  # Move to the next day

    return sundays

# Sample Year
year = 2023

# Get all Sundays in the specified year
sundays_in_year = get_sundays(year)

# Print the results
print(f"All Sundays in the year {year}:")
for sunday in sundays_in_year:
    print(sunday.strftime('%Y-%m-%d'))

# Output:

All Sundays in the year 2023:
2023-01-01
2023-01-08
2023-01-15
2023-01-22
2023-01-29
2023-02-05
2023-02-12
2023-02-19
2023-02-26
2023-03-05
2023-03-12
2023-03-19
2023-03-26
2023-04-02
2023-04-09
2023-04-16
2023-04-23
2023-04-30
2023-05-07
2023-05-14
2023-05-21
2023-05-28
2023-06-04
2023-06-11
2023-06-18
2023-06-25
2023-07-02
2023-07-09
2023-07-16
2023-07-23
2023-07-30
2023-08-06
2023-08-13
2023-08-20
2023-08-27
2023-09-03
2023-09-10
2023-09-17
2023-09-24
2023-10-01
2023-10-08
2023-10-15
2023-10-22
2023-10-29
2023-11-05
2023-11-12
2023-11-19
2023-11-26
2023-12-03
2023-12-10
2023-12-17
2023-12-24
2023-12-31    

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 


16. Write a Python program to add year(s) to a given date and display the updated date.
Sample Data : (addYears is the user defined function name)
print(addYears(datetime.date(2015,1,1), -1))
print(addYears(datetime.date(2015,1,1), 0))
print(addYears(datetime.date(2015,1,1), 2))
print(addYears(datetime.date(2000,2,29),1))
Expected Output :
2014-01-01
2015-01-01
2017-01-01
2001-03-01

# :: Solution ::

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

17. Write a Python program to drop microseconds from datetime.

# :: Solution ::

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

18. Write a Python program to get days between two dates.
Sample Dates : 2000,2,28, 2001,2,28
Expected Output : 366 days, 0:00:00

# :: Solution ::

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

19. Write a Python program to get the date of the last Tuesday.

# :: Solution ::

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

20. Write a Python program to test the third Tuesday of a month.

# :: Solution ::

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

21. Write a Python program to get the last day of a specified year and month.

22. Write a Python program to get the number of days in a given month and year.

23. Write a Python program to add a month to a specified date.

24. Write a Python program to count the number of Mondays on the 1st day of the month from 2015 to 2016.

25. Write a Python program to print a string five times, with a delay of three seconds..

26. Write a Python program that calculates the date six months from the current date using the datetime module.

27. Write a Python program to create 12 fixed dates from a specified date over a given period. The difference between two dates is 20.

28. Write a Python program to get the dates 30 days before and after today.

29. Write a Python program to get GMT and the local time.

30. Write a Python program to convert a date to a timestamp.

31. Write a Python program to convert a string date to a timestamp.

32. Write a Python program to calculate the number of days between two dates.

33. Write a Python program to calculate the number of days between two date times.

34. Write a Python program to display the date and time in a human-friendly string.

35. Write a Python program to convert a date to a Unix timestamp.

36. Write a Python program to calculate the difference between two dates in seconds.

37. Write a Python program to convert difference of two dates into days, hours, minutes, and seconds.

38. Write a Python program to get the last modified information of a file.

39. Write a Python program to calculate an age in years.

40. Write a Python program to get the current date and time information.

41. Write a Python program to generate a date and time as a string.

42. Write a Python program to display formatted text output of a month and start the week on Sunday.

43. Write a Python program to print a 3-column calendar for an entire year.

44. Write a Python program to display a calendar for a locale.

45. Write a Python program to get the current week.

46. Write a Python program to create a HTML calendar with data for a specific year and month.

47. Write a Python program display a list of the dates for the 2nd Saturday of every month for a given year.

48. Write a Python program to display a simple, formatted calendar of a given year and month.

49. Write a Python program to convert a string into datetime

50. Write a Python program to get a list of dates between two dates.

51. Write a Python program to generate RFC 3339 timestamp.

52. Write a Python program to get the first and last second.

53. Write a Python program to validate a Gregorian date. The month is between 1 and 12 inclusive, the day is within the allowed number of days for the given month. Leap year's are taken into consideration. The year is between 1 and 32767 inclusive.

54. Write a Python program to set the default timezone used by all date/time functions.

55. The epoch is the point where time starts, and is platform dependent. For Unix, the epoch is January 1, 1970, 00:00:00 (UTC). Write a Python program to find out what the epoch is on a given platform. Convert a given time in seconds since the epoch.
Sample Output:
Epoch on a given platform:
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
Time in seconds since the epoch:
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=10, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

56. Write a Python program to get time values with components using local time and gmtime.
Sample Output:
localtime:
tm_year : 2021
tm_mon : 4
tm_mday : 13
tm_hour : 11
tm_min : 20
tm_sec : 37
tm_wday : 1
tm_yday : 103
tm_isdst: 0
gmtime:
tm_year : 2021
tm_mon : 4
tm_mday : 13
tm_hour : 11
tm_min : 20
tm_sec : 37
tm_wday : 1
tm_yday : 103
tm_isdst: 0

57. Write a Python program to get different time values with components timezone, timezone abbreviations, the offset of the local (non-DST) timezone, DST timezone and time of different timezones.
Sample Output:
Default Zone:
TZ : (not set)
Timezone abbreviations: ('UTC', 'UTC')
Timezone : 0 (0.0)
DST timezone 0
Time : 11:30:05 04/13/21 UTC
Pacific/Auckland :
TZ : Pacific/Auckland
Timezone abbreviations: ('NZST', 'NZDT')
Timezone : -43200 (-12.0)
DST timezone 1
Time : 23:30:05 04/13/21 NZST
Europe/Berlin :
TZ : Europe/Berlin
Timezone abbreviations: ('CET', 'CEST')
Timezone : -3600 (-1.0)
DST timezone 1
Time : 13:30:05 04/13/21 CEST
America/Detroit :
TZ : America/Detroit
Timezone abbreviations: ('EST', 'EDT')
Timezone : 18000 (5.0)
DST timezone 1
Time : 07:30:05 04/13/21 EDT
Singapore :
TZ : Singapore
Timezone abbreviations: ('+08', '+08')
Timezone : -28800 (-8.0)
DST timezone 0
Time : 19:30:05 04/13/21 +08

58. Write a Python program that can suspend execution of a given script for a given number of seconds.
Sample Output:
Sorry, Slept for 3 seconds...
Sorry, Slept for 3 seconds...
Sorry, Slept for 3 seconds...
Sorry, Slept for 3 seconds...

59. Write a Python program to convert a given time in seconds since the epoch to a string representing local time.
Sample Output:
Tue Apr 13 11:51:51 2021
Thu Jun 30 18:36:29 1977

60. Write a Python program that prints the time, names, representation format, and the preferred date time format in a simple format.
Sample Output:
Simple format of time:
Tue, 13 Apr 2021 12:02:01 + 1010
Full names and the representation:
Tuesday, 04/13/21 April 2021 12:02:01 + 0000
Preferred date time format:
Tue Apr 13 12:02:01 2021
Example 11: 04/13/21, 12:02:01, 21, 2021

61. Write a Python program that takes a given number of seconds and passes since the epoch as an argument. Print structure time in local time.
Sample Output:
Result: time.struct_time(tm_year=1983, tm_mon=2, tm_mday=19, tm_hour=21, tm_min=38, tm_sec=18, tm_wday=5, tm_yday=50, tm_isdst=0)
Year: 1983

62. Write a Python program that takes a tuple containing 9 elements corresponding to structure time as an argument and returns a string representing it.
Sample Output:
Result: Sun Jan 22 02:34:06 2020
Result: Tue Nov 12 02:54:08 1982

63. Write a Python program to parse a string representing time and return the time structure.
Sample Output:
String representing time: 22 January, 2020
time.struct_time(tm_year=2020, tm_mon=1, tm_mday=22, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=22, tm_isdst=-1)
String representing time: 30 Nov 00
time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
String representing time: 04/11/15 11:55:23
time.struct_time(tm_year=2015, tm_mon=4, tm_mday=11, tm_hour=11, tm_min=55, tm_sec=23, tm_wday=5, tm_yday=101, tm_isdst=-1)
String representing time: 12-11-2019
time.struct_time(tm_year=2019, tm_mon=12, tm_mday=11, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=345, tm_isdst=-1)
String representing time: 13::55::26
time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=13, tm_min=55, tm_sec=26, tm_wday=0, tm_yday=1, tm_isdst=-1)
