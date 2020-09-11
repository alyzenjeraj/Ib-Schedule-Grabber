from datetime import date

today = date.today()


# Month abbreviation, day and year	
day = today.strftime("%b-%d-%Y")
print(day)