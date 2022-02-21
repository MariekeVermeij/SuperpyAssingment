import argparse
from datetime import datetime, timedelta,date
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import set_date
from matplotlib.backends.backend_pdf import PdfPages

#Create a parser for dasboard update.
parser = argparse.ArgumentParser(description='Create a new dashbaord, based on input period')                                 
#Parser arguments for dashboard period.
parser.add_argument("period", type=str, help='Insert the first day of the period or click the chosen period')    #all arguments that should be entered in a commandline are listed and explained
parser.add_argument("period2", type=str, help='Insert the last day of the period or click the chosen period')    #all arguments that should be entered in a commandline are listed and explained

args = parser.parse_args()

#This function uses the entry information about start date and end date to return all dates in the period.
def period_to_use(period, period2):
    #start_date is used for the date of today
    start_date = datetime.strptime((set_date.today),"%Y-%m-%d")
    if period == 'last_week':
        # For last week: the first day of the current week minus a timedelta of one week is used to find the first day of last week. 
        weekday =  (start_date).weekday()
        start_days = timedelta(days=int(weekday), weeks=1)
        start_of_week = start_date - start_days
        #returned wil be the start date and the 6 days after that.
        return  [(start_of_week + timedelta(0)).strftime("%Y-%m-%d"),(start_of_week + timedelta(1)).strftime("%Y-%m-%d"),\
            (start_of_week + timedelta(2)).strftime("%Y-%m-%d"),(start_of_week + timedelta(3)).strftime("%Y-%m-%d"),(start_of_week + timedelta(4)).strftime("%Y-%m-%d"),\
                (start_of_week + timedelta(5)).strftime("%Y-%m-%d"),(start_of_week + timedelta(6)).strftime("%Y-%m-%d")]             
    elif period == 'current_week':
        # For current week: the first day of the current week is used, returned wil be the start date and the 6 days after that.
        return [(start_date + timedelta(0)).strftime("%Y-%m-%d"),(start_date + timedelta(1)).strftime("%Y-%m-%d"),\
            (start_date + timedelta(2)).strftime("%Y-%m-%d"),(start_date + timedelta(3)).strftime("%Y-%m-%d"),(start_date + timedelta(4)).strftime("%Y-%m-%d"),\
                (start_date + timedelta(5)).strftime("%Y-%m-%d"),(start_date + timedelta(6)).strftime("%Y-%m-%d")] 
    elif period == 'last_month':
        month_dates = []
        # For last month: subtracting the days of day number of today from today to get last date of last Month.
        last_day_last_month = start_date - timedelta(days=start_date.day)
        #replace the last day of the month with 1 for the first day of the month. 
        first_day = (last_day_last_month.replace(day=1)).strftime("%Y-%m-%d")
        next_day = datetime.strptime((first_day),"%Y-%m-%d")
        #add the dates of the period to the empty list. every time adds 1 to the date that is added, stops when the end date is the same as the added date.
        while next_day <= last_day_last_month:
            month_dates.append(next_day.strftime("%Y-%m-%d"))
            next_day = next_day + timedelta(1)
        #return the list with dates.
        return month_dates
    elif period == 'current_month':
        # find first day next month by using today, replace day number with 28 + four days to be sure to reach a next month.
        #than replace that day number with one and this date minus 1 for last day this month.
        month_dates = []
        next_month = start_date.replace(day=28) + timedelta(days=4)
        last_day_current_month = next_month.replace(day=1) - timedelta(days=1)
        #replace the last day of the month with 1 for the first day of the month. 
        first_day = (last_day_current_month.replace(day=1)).strftime("%Y-%m-%d")
        next_day = datetime.strptime((first_day),"%Y-%m-%d")
         #add the dates of the period to the empty list. every time adds 1 to the date that is added, stops when the end date is the same as the added date.
        while next_day <= last_day_current_month:
            month_dates.append(next_day.strftime("%Y-%m-%d"))
            next_day = next_day + timedelta(1)
        #return the list with dates.
        return month_dates
    elif period == 'last_year':
        year_dates = []
        #find first day of de current year by replacing day and month with number 1. Minus 1 is the last day of last year. 
        first_month = start_date.replace(day=1,month=1) 
        last_day_last_year = first_month - timedelta(days=1)
        #replace the last day of the day and month with 1 for the first day of the year. 
        first_day_last_year = (last_day_last_year.replace(day=1,month=1)).strftime("%Y-%m-%d")
        next_day_last_year = datetime.strptime((first_day_last_year),"%Y-%m-%d")
         #add the dates of the period to the empty list. every time adds 1 to the date that is added, stops when the end date is the same as the added date.
        while next_day_last_year <= last_day_last_year:
            year_dates.append(next_day_last_year.strftime("%Y-%m-%d"))
            next_day_last_year = next_day_last_year + timedelta(1)
        #return the list with dates.
        return year_dates
    elif period == 'current_year':
        year_dates = []
          #replace the last day of the day and month with 1 for the first day of the year, and month 12 and day 31 for the last day of the current year.
        first_day_current_year = start_date.replace(day=1,month=1).strftime("%Y-%m-%d")        
        last_day_current_year = start_date.replace(day=31,month=12) 
        next_day_current_year = datetime.strptime((first_day_current_year),"%Y-%m-%d")
         #add the dates of the period to the empty list. every time adds 1 to the date that is added, stops when the end date is the same as the added date.
        while next_day_current_year <= last_day_current_year:
            year_dates.append(next_day_current_year.strftime("%Y-%m-%d"))
            next_day_current_year = next_day_current_year + timedelta(1) 
        #return the list with dates.
        return year_dates    
    elif period == 'today':
        #use function to find date
        return [set_date.today]
    elif period == 'yesterday':  
         #use function to find date  
        return [set_date.yesterday]
    elif isinstance((datetime.strptime((period),"%Y-%m-%d")),date):
        manual_dates = []
        #use the dates that are entered in entry boxes as fisrt and last date. 
        start_period = datetime.strptime((period),"%Y-%m-%d")
        end_period = datetime.strptime((period2),"%Y-%m-%d")
        next_manual_day = (start_period)
         #add the dates of the period to the empty list. every time adds 1 to the date that is added, stops when the end date is the same as the added date.
        while next_manual_day <= end_period:
            manual_dates.append(next_manual_day.strftime("%Y-%m-%d"))
            next_manual_day = next_manual_day + timedelta(1)
        #return the list with dates.
        return manual_dates
    else: print ('input error') 
  

#Function to create pdf file with information graphs.
def dashboard(p1,p2):
    df = pd.read_csv (r'stock.csv', sep=';')
    #make a data frame of only the rows that have sales dates that belong to the period to use. 
    stock_period = df[df["stock_sales_date"].isin(period_to_use(p1,p2))]
    plt.style.use('dark_background')
    #create a figure that groups by product and shows the sum of the profit and the mean profit. 
    fig1 = plt.figure(constrained_layout=True)
    stock_period.groupby('product_name')['line_profit'].sum().plot(kind='barh',width=0.4,x='product_name',y='sum',color = '#d252e3',legend='Total profit')        
    stock_period.groupby('product_name')['line_profit'].mean().plot(kind='barh',width=0.2,x='product_name',y='mean',color = "#71c571",legend='Mean profit') 
    #create titel, ticks, legend and label.
    plt.title('Total and mean profit for: '+p1+" - "+p2, fontdict=None, loc='center', pad=None)
    plt.yticks(fontsize=6, ha='right', va='top') 
    plt.xticks(fontsize=6)
    plt.legend().get_texts()[0].set_text('Total profit')
    plt.legend().get_texts()[1].set_text('Mean profit')
    plt.ylabel("Products",fontsize=6)
    plt.xlabel("Profit in Euro",fontsize=6)
    #create a figure that groups by product and counts how many times the product is sold. 
    fig2 = plt.figure(constrained_layout=True)
    stock_period.groupby('product_name')['stock_sales_id'].count().plot(kind='barh', width=0.1, color = "#ff3791",legend='Sold products')   #number of sold products deze 2 gaan samen in 1 grafiek. 
    #create titel, ticks, legend and label.
    plt.title('Number of sold products for: '+p1+" - "+p2, fontdict=None, loc='center', pad=None)
    plt.legend().get_texts()[0].set_text('Sold products')
    plt.ylabel("Products",fontsize=6)
    plt.xlabel("Count",fontsize=6)
    plt.xticks(fontsize=6, ha='right', va='top')
    plt.yticks(fontsize=6)
    #create a figure that groups sales week and shows the revenue and profit of that week.
    fig3 = plt.figure(constrained_layout=True)
    stock_period.groupby("sales_week")['stock_sales_price'].sum().plot(kind='bar', width=0.1, color = "#ff3791",legend='Revenue1')  
    stock_period.groupby("sales_week")['line_profit'].sum().plot(kind='bar', width=0.05, color = "#51dee5",legend='Profit') 
    #create titel, ticks, legend and label.
    plt.title('Revenue and profit per week for: '+p1+" - "+p2, fontdict=None, loc='center', pad=None)
    plt.legend().get_texts()[0].set_text('Revenu')
    plt.legend().get_texts()[1].set_text('Profit')
    plt.ylabel("Euro",fontsize=6)
    plt.xlabel("Week",fontsize=6)
    plt.yticks(fontsize=6, ha='right', va='top') 
    plt.xticks(fontsize=6)
    #create or use pdf file,save the figures in it and close the pdf. 
    pp = PdfPages('Superpy_dashboard.pdf')
    pp.savefig(fig1)
    pp.savefig(fig2)
    pp.savefig(fig3)
    pp.close()
    return""
    

#run dashboard function with arguments from the commandline.  
dashboard(args.period, args.period2)
   
