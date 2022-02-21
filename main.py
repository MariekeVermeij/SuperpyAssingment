# Imports
import argparse
import csv
import datetime 
import os
from os import close
import set_date
import stock

# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'


#A parse for new purchase and sales lines
parser = argparse.ArgumentParser(description='Creates a new line in purchase_overview.csv based on new purchases')                                 
subparser = parser.add_subparsers(dest='command')
#sub parser with arguments for purchase overview
purchase = subparser.add_parser('purchase')
purchase.add_argument("product_name", type=str, help='Enter the standard name of the product')    #all arguments that should be entered in a commandline are listed and explained
purchase.add_argument("unit_price", type= float, help = 'Enter the amount paid in Euro\'s, rounded to 2 decimal places,e.g.2.50')
purchase.add_argument("expiration_date", type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'),help = "Enter the expiration date of the product(s) in the following format: ['yyyy-mm-dd']" )
#sub parser with for sales overview
sales = subparser.add_parser('sales')
sales.add_argument("product_name", type=str, help='Enter the standard name of the sold product')   #all arguments that should be entered in a commandline are listed and explained
sales.add_argument("sales_unit_price", type= float, help = 'Enter the amount paid in Euro\'s, rounded to 2 decimal places,e.g.2.50')
args = parser.parse_args()


# backend message to inform which product is typed in the purchase/sales entry field. 
if args.command == 'purchase':
  print('Buying:', args.product_name)
if args.command == 'sales':
  print('Trying to sell:', args.product_name)


#function returns the new id no to use in purchase file 
def purchase_id_count():       
#try if the following is possible, if the file does not exist it will skip this and return 1
    try:          
        #look in every row of the purchase file and if its a number add it to the list. the last number in the list is the current max id                                                         
        with open('purchase_overview.csv', 'r') as purchase_file:           
            list = []
            for row in purchase_file:                                    
                id = (row.split(';')[0])
                if id.isnumeric() == True:
                    list.append(id)
                else: list.append(0)
        max_id = list[-1]   
        # return value of the last row + 1   
        return (int(max_id)+1)                                                                                                                
    except FileNotFoundError:
        #if the file does not exist return 1      
        return 1                                                         


# funtion to create new line in the purchase overview with the following information: product_name,unit_price and expiration_date).
def purchase_lines(product_name,unit_price,expiration_date):    
    #tries to update the file, if there is no permission it skips the writing of a new line.                                                                         
    try: 
        #checks if file stock_update does exist, if not it writes the header and creates a new file.                                                                                                                                                    
        if not os.path.exists('purchase_overview.csv'):                                                                                                     
            with open('purchase_overview.csv', mode='w',newline='') as purchase_file:                                                                       
                columns = ['purchase_id','product_name','unit_price','expiration_date','purchase_date']
                writer = csv.DictWriter(purchase_file, delimiter=';',lineterminator='\n', fieldnames=columns)
                writer.writeheader()
                close
        #if the file already existed or is created the file is opened.
        with open('purchase_overview.csv', mode='a',newline='') as purchase_file:                                                                                                                                                     
                    columns = ['purchase_id','product_name','unit_price','expiration_date','purchase_date']                       
                    writer = csv.DictWriter(purchase_file, delimiter=';',lineterminator='\n', fieldnames=columns)       
                    #new line is created with the arguments from the command line, which are typed in by the user in the entry fields of the program.                                    
                    writer.writerow({'purchase_id':purchase_id_count(),'product_name': (args.product_name).lower(),'unit_price':  args.unit_price,\
                        'expiration_date': (args.expiration_date).strftime("%Y-%m-%d"),'purchase_date':set_date.today})
                    print("New row added to purchase_overview.csv")
        close
    except PermissionError: print("WARNING! Purchased Product not added to the file. Please close the file 'purchase_overview.csv' and try again or contact your network administrator.")

 
#function returns the new id no to use in sales file 
def sales_id_count():   
    #try if the following is possible, if the file does not exist it will skip this and return 1                                                  
    try: 
        #look in every row of the sales file and if its a number add it to the list. the last number in the list is the current max id                                                                 
        with open('sales_overview.csv', 'r') as sales_file:           
            list = []
            for row in sales_file:                                     
                id = (row.split(';')[0])
                if id.isnumeric() == True:
                    list.append(id)
                else: list.append(0)
        max_id = list[-1]    
        # return value of the last row + 1   
        return (int(max_id)+1)                                                                                                                
    except FileNotFoundError:     
        #if the file does not exist return 1 
        return 1                                                    


#function to check if the product entered in the sales entry line is available in stock
def check_inventory(product_to_sell):
    #look in every row of the stock file. if there is a product with a expiration date of today of higher and without the line reveure line already filled(than the product is sold or expired)
    with open ('stock.csv', 'r') as stock_file: 
        reader = csv.DictReader(stock_file,delimiter = ';',lineterminator='\n', quotechar='"')                                        
        for row in reader: 
               if product_to_sell == (row['product_name']):
                    if(row['expiration_date']) >= set_date.today:
                        if (row['line_profit']) == "":
                            print ('product available') 
                            #if the product is available for sale a 1 will be returned
                            return 1 


 
# funtion to create new line in the sales overview with the following information: product_name,sales_unit_price).
def sales_lines(product_name,sales_unit_price): 
     #tries to update the file, if there is no permission it skips the writing of a new line. 
    try:     
        #checks if file stock_update does exist, if not it writes the header and creates a new file.                                                                                                                                        #try if the following is permitted, if not a warning wil be printed
        if not os.path.exists('sales_overview.csv'):                                                                                                
            with open('sales_overview.csv', mode='w',newline='') as sales_file:                                                                   
                columns = ['sales_id','product_name','sales_unit_price','sales_date']                                      
                writer = csv.DictWriter(sales_file, delimiter=';',lineterminator='\n', fieldnames=columns)
                writer.writeheader()
                close
        #if the product is availabe (fuction check_inventory returns 1) the file is opened.
        if check_inventory((args.product_name).lower()) == 1:                    
                    with open('sales_overview.csv', mode='a',newline='') as sales_file:                                                                      
                        columns = ['sales_id','product_name','sales_unit_price','sales_date']                                  
                        writer = csv.DictWriter(sales_file, delimiter=';',lineterminator='\n', fieldnames=columns)  
                        #new line is created with the arguments from the command line, which are typed in by the user in the entry fields of the program.                                    
                        writer.writerow({'sales_id':sales_id_count(),'product_name': (args.product_name).lower(),'sales_unit_price':  args.sales_unit_price,'sales_date':set_date.today})
                        close
                        print("New row added to sales_overview.csv")
        else: print('product not in stock')
    except PermissionError: print("WARNING! Sold Product not added to the file. Please close the file 'sales_overview.csv' and try again or contact your network administrator.")


#function to execute the update functions with the commands on the line - which are derived from the user entry boxes.
def main():
    #for subparser purchase.
    if args.command == 'purchase':
        purchase_lines(args.product_name,args.unit_price,args.expiration_date)
    #for subparser sales.
    elif args.command == 'sales':
        #before check if porduct can be sold it first updates the stock file.
        stock.stock_update()
        sales_lines(args.product_name,args.sales_unit_price)



if __name__ == '__main__':
    main()
