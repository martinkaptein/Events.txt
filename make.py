import datetime
print("___Events (dot) txt___\n__@username__\n")


now = datetime.datetime.now()

##############################

# settings
genDaysAhead = 2000 #4380
WeekdaysStrings = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# if you want the week to start on sunday, change elif statement to weekdaynumber == 6

# end settings

for day in range(genDaysAhead):
    diff = datetime.timedelta(days=day)
    future = now + diff
    year = future.strftime("%Y")
    month = future.strftime("%m")
    day = future.strftime("%d")
    printDate = future.strftime("%d/%m/%Y")
   
    monthname = months[int(month) - 1]
    weekdaynumber = future.weekday()
    weekdayname = WeekdaysStrings[weekdaynumber] 
    if day == '01':
        toPrint = '\n\n' + monthname + '\n' + printDate + ' ' + weekdayname + ' |' 
        print(toPrint)
    elif weekdaynumber == 0:
        toPrint = '______\n' + printDate + ' ' + weekdayname + ' |' 
        print(toPrint)
    else:
        toPrint = printDate + ' ' + weekdayname + ' |'
        print(toPrint)

###############################

print("\n\n#repeatingYearly")
print("\n\n#oob")
