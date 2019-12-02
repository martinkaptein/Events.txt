# settings
genDaysAhead = 800 #4380
startFromYear = 2019
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

    toPrint = 
    print(future)



