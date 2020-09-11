import requests
from datetime import date
import tabula 

today = date.today()

# url = 'http://ibs.diefib.ca/IBS.pdf'
# r = requests.get(url, allow_redirects=True)

# Month abbreviation, day and year	
day = today.strftime("%b-%d-%Y")

# open(day + '.pdf', 'wb').write(r.content)

file = 'http://ibs.diefib.ca/IBS.pdf'

tables = tabula.read_pdf(file, pages = 3)

tabula.convert_into(file, day+'-Schedule.csv', pages = 3)







