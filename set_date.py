import  datetime 
import csv

# Current date,  yesterday's date in variables
def get_date():
    with open ('today.csv', mode='r',encoding='utf8',newline='') as today_file:
            reader_today = csv.DictReader(today_file,delimiter = ';',lineterminator='\n', quotechar='"')
            for row in reader_today:
                date_to_use = (row['today_date'])
                return date_to_use

today = get_date()
yesterday = (datetime.datetime.strptime(today, '%Y-%m-%d') - datetime.timedelta(days=1)).strftime("%Y-%m-%d")




