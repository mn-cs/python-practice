# Exercise 6. Magic Dates (15 points)

# The date June 10, 1960, is special because when it is written in the following format,
# the month times the day equals the year: 6/10/60
# Design a program that asks the user to enter a month (in numeric form), a day, and a 
# four-digit year. The program should then determine whether the month times the day 
# equals the year. If so, it should display a message saying the date is magic. 
# Otherwise, it should display a message saying the date is not magic.

# Must check for valid month and month. (3 points)

# For e.g. if month is 4 then day can not be 31. (3 points)

# If it is a leap year,  day can be 29 for month of February.  (3 points)

# Allow the user to enter a year between 1900 and 2030. Verify it is in this range only.

# Use the last 2 digits of the year entered for determining if it is a magic date or
# not, Use the 4 digit year to determine leap or not. 

# Hint: You can you use the '%' operator to find the right two digits of the year.
# See Table 2-3.

# Prints an appropriate response. (3 points)


arr = ["January", "February", "March", "April", "May", "June", "July",
       "August", "September", "October", "November", "December"]


def check_leap(y):
    return bool((y % 400 == 0) or (y % 100 != 0) and (y % 4 == 0))


month = int()
day = int()
year = int()

while True:
  try:
    month = int(input('Enter a month (in numeric form): '))
    day = int(input('Enter a day: '))
    year = int(input('Enter a four-digit year: '))

    if month < 1 or month > 12:
        print("* Enter a month between 1 and 12")
        continue

    if month == 2 and check_leap(year) and not (1 <= day <= 29):
        print(f"* Enter a day between 1 and 29 for {arr[month - 1]}")
        continue

    if month == 2 and not check_leap(year) and not (1 <= day <= 28):
        print(f"* Enter a day between 1 and 28 for {arr[month - 1]}")
        continue

    if (month in [4, 6, 9, 11]) and not (1 <= day <= 30):
        print(f"* Enter a day between 1 and 30 for {arr[month - 1]}")
        continue

    if (month in [1, 3, 5, 7, 8, 10, 12]) and not (1 <= day <= 31):
        print(f"* Enter Day between 1 and 31 for {arr[month - 1]}")
        continue

    if year > 2030 or year < 1900:
        print("* Enter a year between 1900 and 2030")
        continue

  except ValueError:
    print("* Enter a Valid Integer")
    continue

  break

print(f"Entered Date {month}/{day}/{year}")

if (year % 100) == (month * day):
    print("The date is magic")
else:
    print("The date is not magic")

if check_leap(year):
    print("It is a Leap Year")
else:
    print("It is not a Leap Year")


# Test 1:
#        Input:  Enter a month (in numeric form): 1
#                Enter a day: 1
#                Enter a four-digit year: 2000
#        Output: Entered Date 1/1/2000
#                The date is not magic
#                It is a Leap Year

# Test 2:
#        Input:  Enter a month (in numeric form): 2
#                Enter a day: 2
#                Enter a four-digit year: 1980
#        Output: Entered Date 2/2/1980
#                The date is not magic
#                It is a Leap Year

# Test 3:
#        Input:  Enter a month (in numeric form): 6
#                Enter a day: 10
#                Enter a four-digit year: 1980
#        Output: Entered Date 6/10/1960
#                The date is magic
#                It is a Leap Year

# Test 4:
#        Input:  Enter a month (in numeric form): 5
#                Enter a day: 5
#                Enter a four-digit year: 2015
#        Output: Entered Date 5/15/2015
#                The date is not magic
#                It is not a Leap Year