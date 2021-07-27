from datetime import date
def NumberOfDays(date1, date2):
    return (date2 - date1).days
date1 = date(2020, 10, 13)
date2 = date(2021, 5, 6)
print("The difference betweent these two given dates is:\n")
print(NumberOfDays(date1, date2), "days")
