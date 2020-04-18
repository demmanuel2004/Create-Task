from datetime import datetime, date
def day_year(user_year):
  if user_year <= 1699 and user_year >= 1600:
     global year_addition 
     year_addition = 6 
  elif user_year <= 1799 and user_year >= 1700:
      year_addition = 4 
  elif user_year <= 1899 and user_year >= 1700:
      year_addition = 2
  elif user_year <= 1999 and user_year >= 1900:
      year_addition = 0
  elif user_year <= 2000 and user_year >= 2099:
      year_addition = 6   

def day_month(user_month):
  if user_month == 1 or user_month == 10:
    global month_addition
    month_addition = 0 
  elif user_month == 2 or user_month == 3:
    month_addition = 3 
  elif user_month == 4 or user_month == 7:
    month_addition = 6
  elif user_month == 5:
    month_addition = 1
  elif user_month == 6:
    month_addition = 4
  elif user_month == 7:
    month_addition = 6
  elif user_month == 8:
    month_addition = 2
  elif user_month == 9 or user_month == 12:
    month_addition = 5
  elif user_month == 11:
    month_addition = 3


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

global last_user_year 
last_user_year = int(str(user_year)[2:4])

day_calculated = user_day + month_addition + last_user_year + last_user_year / 4 + 6 

global day_number_calculated
day_number_calculated = day_calculated % 7

global fixed_last_user_year 
fixed_last_user_year = day_number_calculated
fixed_last_user_year = float(str(fixed_last_user_year)[0:2])

if fixed_last_user_year == 0:
  print ("It will be Sunday!")
elif fixed_last_user_year == 1:
  print ("It Will be Monday!")
elif fixed_last_user_year == 2:
  print ("It Will be Tuesday!")
elif fixed_last_user_year == 3:
  print ("It Will be Wedensday!")
elif fixed_last_user_year == 4:
  print ("It Will be Thursday!")
elif fixed_last_user_year == 5:
  print ("It Will be Friday!")
elif fixed_last_user_year == 6:
  print ("It Will be Saturday!")


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
