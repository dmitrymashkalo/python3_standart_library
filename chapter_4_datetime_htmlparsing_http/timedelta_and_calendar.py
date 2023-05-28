# Time Delta and Calendar
from datetime import datetime, timedelta
import calendar

now = datetime.now()

# Time Delta
testDate = now + timedelta(days=1) # Get now + 1 day date
myFirstCourse = now - timedelta(weeks=3) # Get now - 3 weeks date

print(testDate.date())
print(myFirstCourse.date())


# Comparison
if testDate > myFirstCourse:
    print('Comparison works!')


# Calendar
print(calendar.month(1997, 12)) # Get month calendar

print(calendar.weekday(1997, 12, 22)) # Get weekday, 0 - Mon, 1 - Tues ...

print(calendar.isleap(1997)) # Not a Leap Year
print(calendar.isleap(2000)) # Leap Year