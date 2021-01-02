# PRACTICE PROJECT "Date Detection" of Chapter7
# BY JITHIN JOHN
import re
date_exp = re.compile(r'\d{2}/\d{2}/\d{4}')
date = input("Please enter the date to be validated: ")
mo = date_exp.search(date)
if mo != None:
    day, month, year = date.split("/")
    day, month, year = int(day), int(month), int(year) 
    apr = 30
    jun = 30
    sep = 30
    nov = 30
    jan = 31
    mar = 31
    may = 31
    jul = 31
    aug = 31
    oct = 31
    dec = 31
    if year%4==0:
        feb = 29
    elif year%100 == 0:
        pass
    else:
        feb = 28
    month_days = [jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec]
    if month >= 12:
        print("No such Month")
    elif day > month_days[month-1]:
        print("No such day")
    else:
        print("The Date exist")
else:
    print("Not in DD/MM/YYYY format")