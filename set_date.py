import  datetime 
# Current date,  yesterday's date in variables
today = datetime.datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")




