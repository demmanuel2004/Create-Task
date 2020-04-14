name = input("Welcome user, what is your name? \n");

from datetime import datetime, date
print("\n Welcome " + name +" \n" "Enter the Date in the format: <Year-Month-Date>")

#To find day of week on Given date
x = input("Enter the Date to find the day of the week :-")

#strptime converts the given object to a string in the specified format which wrks opposite of strftime
dd = datetime.strptime(x,"%Y-%m-%d")


print(dd.strftime("%A"))



# To find out the no of days between two given dates
print("\n Calculate number of days between two given dates :\n")

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
