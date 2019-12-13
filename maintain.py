# This is a Python script to maintain your calendar
# By default is modifies the Events.txt file in current directory, whilst also making a backup
# This script adds new days to your current Events.txt, whilst incoorporating the #repeatingEvents. Functionality for adding #oob automatically will be added later.

# TEMP comments for myself
# 1. make backup of Events.txt, if not found exit with error message
# 2. read last "normal" day date (parse in reverse direction of optimization)
# 3. insert x new dates
# 4. for each repeating Event parse and insert at all correct locations (=years)
# whilst maintaining syntax
