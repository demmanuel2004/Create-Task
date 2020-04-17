from datetime import datetime, date

"""JANUARY = 31
FEBRUARY = 28
MARCH = 31
APRIL = 30
MAY = 31 
JUNE = 30 
JULY = 31
AUGUST = 31 
SEPTEMBER = 30
OCTOBER = 31
NOVEMBER = 30
DECEMBER = 31""" 

"""def day_year(user_year):
  if user_year <= 1699 and user_year >= 1600:
     global a 
     a = 6 
  print (a)

  elif user_year <= 1799 and user_year >= 1700:
      global year_addition_18th
      year_addition_18th = 4 
  print (year_addition_18th)"""

def day_month(user_month):
  if user_month == 1 or user_month == 10:
    global month_addition
    month_addition = 0 
    print (month_addition)
  elif user_month == 2 or user_month == 3:
    month_addition = 3 
    print (month_addition)
  elif user_month == 4 or user_month == 7:
    month_addition = 6
    print (month_addition)
  elif user_month == 5:
    month_addition = 1
    print (month_addition)
  elif user_month == 6:
    month_addition = 4
    print (month_addition)
  elif user_month == 7:
    month_addition = 6
    print (month_addition)
  elif user_month == 8:
    month_addition = 2
    print (month_addition)
  elif user_month == 9 or user_month == 12:
    month_addition = 5
    print (month_addition)
  elif user_month == 11:
    month_addition = 3
    print (month_addition)


name = input("Welcome user, what is your name? \n"); 

user_year = int(input("Welcome " + name +" \n" "Enter the year between the years 1600 and 2099. Please format it in numbers only <1999, etc>: \n"));

"day(user_year)"

if user_year % 4 == 0:
  FEBRUARY = 29

while user_year > 3000 or user_year < 1599:
 user_year = int(input("Please enter a year that is between 1600 and 2099 \n"))

user_month = int(input("Now " + name + " Enter the number of the month your day is located in. Please format it in numbers only <for June it will be 6> \n"))
day_month(user_month)

while user_month > 13 or user_year < 0:
 user_month = int(input("Please enter a month that is between 1 and 12\n"))


user_day = int(input("Finally " + name + " Enter the number day of the month in numbers please <1, 3, etc> \n"))

while user_day > 31 or user_year < 0:
 user_day = int(input("Please enter a day that is between 31 and 1 \n"))


# To find out the no of days between two given dates
print("\n Calculate number of days between two given dates <year>-<month>-<date> :\n")

fdate = input("Enter the Start date :- ")
start = datetime.strptime(fdate, "%Y-%m-%d")
# %m will check month no should be from 1-12
# %d will check that date should be from 1-31

ldate = input("Enter the last date :- ")
end = datetime.strptime(ldate, "%Y-%m-%d")

diff = end - start
diff1 = abs(diff)

print("You have %d days of time left" % diff1.days)
print("\n Thank you " + name +" for using this program")
