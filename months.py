#Program to print all months of the year 
from calendar import*
year = int(input("Enter year: "))
print(calendar(year, 2, 1, 8, 4))

#2 = 2 characters for days(mo,tu,etc)
#1 = 1 line (row) for each week
#8 = 8 rows for each month
#4 = 4 columns for all months of the year