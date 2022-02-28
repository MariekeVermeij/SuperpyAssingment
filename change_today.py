import  datetime
import argparse 
import os
import csv
import datetime 
from os import close


#Create a parser for set date today.
parser = argparse.ArgumentParser(description='Create a new dashboard, based on input period')                                 
#Parser arguments for set date today.
parser.add_argument('-d', '--days', type=str,default=0, help='Insert the day you would like to be considered today, (yyyy-dd-mm')   

args = parser.parse_args()

#this function is used to store a date to use as today
def set_date(use_days):
     #tries to update the file, if there is no permission it skips the writing of a new line. 
    try:     
        #checks if file today does exist, if not it writes the header and creates a new file.                                                                                                                                  
        if not os.path.exists('today.csv'):                                                                                                
            with open('today.csv', mode='w',newline='') as today_file:                                                                   
                columns = ['today_date']                                      
                writer = csv.DictWriter(today_file, delimiter=';',lineterminator='\n', fieldnames=columns)
                writer.writeheader()
                close       
    except PermissionError: print("WARNING! Today is not updated. Please close the file 'today.csv' and try again or contact your network administrator.")
    #if the parsed amount of days is not equal to 0, the day from the pdf file is used as a base date
    if use_days != str(0):
        with open('today.csv', mode='r',newline='') as read_today_file:
            reader = csv.DictReader(read_today_file,delimiter = ';',lineterminator='\n', quotechar='"')
            today_list = []
            for row in reader:
                today_list.append(row['today_date'])
            base_date = today_list[0]
        close
        #to the base date is the amount of days added, this overwrites the previous date.
        with open('today.csv', mode='w',newline='') as today_file:                                                                                                                                                     
            columns = ['today_date']                         
            writer = csv.DictWriter(today_file, delimiter=';',lineterminator='\n', fieldnames=columns)   
            #new line is created with the arguments from the command line, which are typed in by the user in the entry fields of the program.                                    
            writer.writeheader()
            writer.writerow({'today_date': (datetime.datetime.strptime(base_date, '%Y-%m-%d') + datetime.timedelta(days=(int(use_days)))).strftime("%Y-%m-%d")})             
        close
    else:     
        #if the parsed amount of days is equal to 0, the current date is used. 
        today_date = datetime.datetime.today().strftime("%Y-%m-%d")
        with open('today.csv', mode='w',newline='') as today_file:                                                                                                                                                     
            columns = ['today_date']                         
            writer = csv.DictWriter(today_file, delimiter=';',lineterminator='\n', fieldnames=columns)   
            #with today as base date and the amount of days added to this the previous date is overwritten.                                    
            writer.writeheader()
            writer.writerow({'today_date': (datetime.datetime.strptime(today_date, '%Y-%m-%d') + datetime.timedelta(days=(int(use_days)))).strftime("%Y-%m-%d")})
        close
                                

set_date(args.days)


