# settings
genDaysAhead = 400 #4380
WeekdaysStrings = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# end settings

print("# Calendar\n")

import datetime

now = datetime.datetime.now()

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
    else:
        toPrint = printDate + ' ' + weekdayname + ' |'
        print(toPrint)



