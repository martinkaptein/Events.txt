genYearStart = 2019
generateYearsAhead = 12
monthsAbreviation = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"]
diff = genYearStart + (generateYearsAhead + 1)
for year in range(genYearStart, diff):
    for month in range(0, 12):
        monthname = monthsAbreviation[month]
        print(":", year, ".", monthname, ":", sep='')
