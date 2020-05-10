import calendar

def findday(date):
    day , month , year = (int(i) for i in date.split(' '))
    daynumber = calendar.weekday(day , month , year )
    days = ['Monday' , 'Tuesday' , 'Wednesday' , 'Thursay' , 'Friday' , 'Saturday' , 'Sunday']
    return (days[daynumber])

    date1 = ' 03 02 2019 '
    print(findday(date1))

 #from datetime import datetime, date

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
while user_year > 3000 or user_year < 1599:
 user_year = int(input("Invalid Year! Please enter a year that is between 1600 and 2099. \n"))
user_month = int(input("Now " + name + ", Enter the number of the month your day is located in. Please format it in numbers only <for example, June will be 6>: \n"))

def leap_year_addition(user_year):
  if user_year % 4 == 0:
    global subtract_year
    subtract_year = 1 
  elif user_year % 4 != 0:
    subtract_year = 0 

while user_month > 13 or user_year < 0:
 user_month = int(input("Invalid Month! Please enter a month that is between 1 and 12. \n"))
user_day = int(input("Finally " + name + ", Enter the number day of the month in numbers please <1, 3, etc>: \n"))

while user_day > 31 or user_year < 0:
 user_day = int(input("Invalid Day! Please enter a day that is between 31 and 1. \n"))
day_month(user_month)

def main_calculation(user_year, user_month, user_day, month_addition):
  day_year(user_year)
  leap_year_addition(user_year)
  if user_year <= 1699 and user_year >= 1600:
    century_addition = 6 
  elif user_year <= 1799 and user_year >= 1700:
    century_addition = 4 
  elif user_year <= 1899 and user_year >= 1800:
    century_addition = 2
  elif user_year <= 1999 and user_year >= 1900:
    century_addition = 0
  elif user_year <= 2099 and user_year >= 2000:
    century_addition = 6  
  last_user_year = int(str(user_year)[2:4])

  if subtract_year == 1 and user_month != 2:
    counter_subtract = 1
  elif subtract_year == 0:
    counter_subtract = 0
  elif subtract_year == 1 and user_month == 2:
    counter_subtract = 0 
  day_calculated = user_day +  month_addition + century_addition + last_user_year - subtract_year + counter_subtract + last_user_year / 4  
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
main_calculation(user_year, user_month, user_day, month_addition)

from datetime import datetime, date
# to calculate no of days between two given dates 

def no_of_days(start,end):
    if start > end :
        diff = start - end 
    else:
        diff = end - start 
    print("You have %d days of time left" % diff.days)
#Print no of days between two different dates entered by user , stored in diff 

#Asking the user to whether to count no of days or not 
answer = input("Continue? Enter yes to find the number of days between two dates: ")
if answer == "yes":
   print("\n Welcome back " + name +". Calculate number of days between two given dates <year>-<month>-<date> :\n")
   fdate = input("Enter the Start date :- ")
   start = datetime.strptime(fdate, "%Y-%m-%d")
   # %m will check month no should be from 1-12
   # %d will check that date should be from 1-31
   ldate = input("Enter the last date :- ")
   end = datetime.strptime(ldate, "%Y-%m-%d")
   no_of_days(start , end)
   print("\n Thank you " + name +" for using this program")
else:
    print("\n Thank you " + name +" for using this program")


''' Algorithm :
Step 1 : Input name of user.
Step 2 : Call day of week 
Step 3 : Input answer(yes/no)
Step 4 : If  answer is yes , then goto step 6.
Step 5 : If answer is no , them goto step 10
Step 6 : Print name of user .
Step 7 : Input start date in format defined in strptime , predefined function in datetime module .
Step 8 : Input end date in format defined in strptime , predefined  function in datetime module 
Step 9 : Call no_of_days(start , end)
Step 10 : Exit.
Algorithm to calculate no of days between two dates
no_of_days(start , end)
Step 1 : If start > end , then
	diff = start - end
Step 2 : If start <= end , then
	diff = end - start 
Step 3 : Print no of days between two different dates entered by user , stored in diff '''
