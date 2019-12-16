# This is a Python script to maintain your calendar
# By default is modifies the Events.txt file in current directory, whilst also making a backup
# This script adds new days to your current Events.txt, whilst incoorporating the #repeatingEvents. Functionality for adding #oob automatically will be added later.

import shutil
import os.path
import sys
import datetime


if os.path.exists("Events.txt"):
    shutil.copy2("Events.txt", "Events.txt.backup")
else:
    print("File not found! Exiting...")
    sys.exit()

# add new days / fill them up?
now = datetime.datetime.now()

# read last date line (bruteforce)
with open("Events.txt") as myFile:
    for num, line in enumerate(myFile, 1):
        if "|" in line:
            endingYear = line[6:10]
            lastDateLine = num
            endingDate = line[:10]


nowyear = now.strftime("%Y")
nowyear = int(nowyear)
endingYear = int(endingYear)

# this writes the actual content to the file 
# snippet from https://stackoverflow.com/questions/10507230/insert-line-at-middle-of-file-with-python
def insertContent(content, linenumber):

    f = open("Events.txt", "r")
    contents = f.readlines()
    check = contents[linenumber] 
    f.close()

   # don't write if already there
    if content != check:
        contents.insert(linenumber, content)
        
    f = open("Events.txt", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()




if (endingYear - nowyear) < 3:
    print("new days are required")
    # parse last date which is read from Event.tx
    endingDate = endingDate + '18:00:00'
    now =  datetime.datetime.strptime(endingDate, '%d/%m/%Y%H:%M:%S')
    # this is from make.py except substitue printing for write to file

    ###################
    
    # settings
    genDaysAhead = 500
    WeekdaysStrings = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    # if you want the week to start on sunday, change elif statement to weekdaynumber == 6
    
    # end settings
    
    for day in range(genDaysAhead):
        # linenumber adjustment
        insertPlace = lastDateLine + day

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
            toPrint = '\n\n' + monthname + '\n' + printDate + ' ' + weekdayname + ' |\n' 
            insertContent(toPrint, insertPlace)
            lastDateLine = lastDateLine + 3

        elif weekdaynumber == 0:
            toPrint = '______\n' + printDate + ' ' + weekdayname + ' |\n' 
            insertContent(toPrint, insertPlace)
            lastDateLine = lastDateLine + 1
        else:
            toPrint = printDate + ' ' + weekdayname + ' |\n'
            insertContent(toPrint, insertPlace)

    print(genDaysAhead, ' have been added')

    ##################
else:
    print("no new days required")

# merging repeatingYearlyEvents
EventList = []
DateList = []


with open("Events.txt") as myFilex:
    for numx, linex in enumerate(myFilex, 1):
        if ' - ' in linex:
            varRepeatingEventDate = linex[:5]
            varRepeatingEventContent = linex[8:]
            varRepeatingEventDate = varRepeatingEventDate + '/'
            #print(varRepeatingEventDate)
            EventList.append(varRepeatingEventContent)
            DateList.append(varRepeatingEventDate)




def findGetLines(query):
    lineList = []
    with open("Events.txt") as myFile:
        for num, line in enumerate(myFile, 1):
            if query in line:
                lineList.append(num)
        return lineList

for xpos, x in enumerate(DateList):
    y = EventList[xpos]
    lineListInsert = findGetLines(x)
    counter = 0
    for z in lineListInsert:
        insertion = '+ ' + y 
        insertContent(insertion, (z + counter))
        counter = counter + 1
