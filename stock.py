 # Imports
import csv
from datetime import datetime
import os
from os import close
import set_date
from tempfile import NamedTemporaryFile
import shutil

#empty lists for purchase id's from stock file,purchase id's from purchase file and purchase id's which are missing in the stock file
                                                


#function that returns purchase_id which has not yet been inserted in the stockfile.
def purchase_id_check():  
    stock_list = []  
    purchase_list = []                                                                                                            
    new_rows_list = []                                              
    try:         
        #look in the stock file for every row (skip the header) add values of the 1st row, product_id to the empty stock list                                 
        with open ('stock.csv', 'r') as stock_file:         
            next(stock_file)                                        
            for row in stock_file:                                  
                row_value_stock = (row.split(';')[0])               
                stock_list.append(int(row_value_stock))  
        close                                                      
    except: stock_list.append('')            
    try:
        #look in the purchase file for every row (skip the header) add values of the 1st row, product id to the empty purchase list 
        with open ('purchase_overview.csv', 'r') as purchase_file:  
            next(purchase_file)                                     
            for row in purchase_file:                               
                row_value_purchase = (row.split(';')[0])             
                purchase_list.append(int(row_value_purchase))
        close                  
    except: stock_list.append('')    
    #purchase id's that are missing in the stock file are added to new_rows_list and returned.
    new_rows_list = ((list(set(purchase_list)-set(stock_list))))          
    new_rows_list.sort()                                        
    return new_rows_list  


#function to find the product name in the purchase file that belongs to the purchase id that will be added to the stock file.
def find_product_name(stock_purchase_id):      
    #look in every row of the purchase file and return the product name for the specific purchase id.                                      
    with open ('purchase_overview.csv', 'r') as purchase_file:     
        reader1 = csv.DictReader(purchase_file,delimiter = ';')     
        for row in reader1:                                          
                if str(stock_purchase_id) == row['purchase_id']:             
                    return(row['product_name'])                    
    close 

#function to find the purchase price in the purchase file that belongs to the purchase id that will be added to the stock file.
def find_purchase_price(stock_purchase_id):           
    #look in every row of the purchase file and return the purchase price for the specific purchase id.                                 
    with open ('purchase_overview.csv', 'r') as purchase_file:    
        reader1 = csv.DictReader(purchase_file,delimiter = ';')      
        for row in reader1:                                         
                if str(stock_purchase_id) == row['purchase_id']:            
                    return(row['unit_price'])    
    close


#function to find the purchase date in the purchase file that belongs to the purchase id that will be added to the stock file.
def find_purchase_date(stock_purchase_id):                                         
    with open ('purchase_overview.csv', 'r') as purchase_file:
        reader = csv.DictReader(purchase_file,delimiter = ';')
        for row in reader:
                if stock_purchase_id == row['purchase_id']:
                    return(row['purchase_date'])
    close


#function to find the expiration date in the purchase file that belongs to the purchase id that will be added to the stock file.
def find_expiration_date(stock_purchase_id): 
    #look in every row of the purchase file and return the purchase price for the specific purchase id.                                       
    with open ('purchase_overview.csv', 'r') as purchase_file:
        reader = csv.DictReader(purchase_file,delimiter = ';')
        for row in reader:
                if str(stock_purchase_id) == row['purchase_id']:
                    return(row['expiration_date'])
    close


#function to find if the product is expired.
def find_expired(stock_purchase_id):      
    #look in every row of the purchase file look for the specific purchase id.                                 
    with open ('purchase_overview.csv', 'r') as purchase_file:
        reader = csv.DictReader(purchase_file,delimiter = ';')
        for row in reader:
            if row['purchase_id'] == stock_purchase_id:
                #If no sales price is added check if the expriration date is before today, in that case return "Expired", is all other cases return "".
                if find_sales_price(match_sales_id(row['purchase_id'])) is None: 
                    if find_expiration_date(row['purchase_id']) < (set_date.today):
                        return ('Expired')
                    else: return ""
                else: return ""


#formule om de sales id met de purchase id te matchen en de juiste sales id terug te geven bij het ingevoerde purchase id.
def match_sales_id(new_purchase_id):  
    #empty lists to be filled in the following steps
    product = []
    sales_id_list = []
    purchase_id_list = []
    # search for the row of the purchase id and add product name to product list.
    with open('purchase_overview.csv', mode='r',encoding='utf8',newline='') as purchase_file:
        reader = csv.DictReader(purchase_file,delimiter = ';')
        for p_row in reader:
            if p_row['purchase_id'] == str(new_purchase_id):
                product.append(p_row['product_name'])
        close
    # for every row of the sales file find the sales_ids that match the product name and add them to the sales id list. 
    with open('sales_overview.csv', mode='r',encoding='utf8',newline='') as sales_file:
        for sales_row in sales_file:
            sales_id = (sales_row.split(';')[0])
            sales_product = (sales_row.split(';')[1])
            if (product) == [sales_product]:
                sales_id_list.append(sales_id)
        close
    # for every row of the purchase file find the purchase_ids that match the product name and add them to the purchase id list.     
    with open('purchase_overview.csv', mode='r',encoding='utf8',newline='') as purchase_file2:  
        for purchase_row in purchase_file2:                            
            purchase_id_column = (purchase_row.split(';')[0])
            purchase_product = (purchase_row.split(';')[1])
            if (product) == [purchase_product]:
                purchase_id_list.append(purchase_id_column)
        #connect the items from the purchase id list to the sales Id list and make it a dictionary (match dictionary).        
        zip_iterator = zip(purchase_id_list,sales_id_list)
        match_dictionary = dict(zip_iterator)   
    # if the purchase id is in match dictionary than the sales id of the purchase id will be returned.                      
    if str(new_purchase_id) in match_dictionary:
        return match_dictionary[str(new_purchase_id)]
    else: return''
close
    

#function to find the sales price in the sales file that belongs to the sales id that will be added to the stock file.
def find_sales_price(stock_sales_id):
    #look in every row of the sales file and return the sales price for the specific sales id.
    with open('sales_overview.csv', mode='r',encoding='utf8',newline='') as sales_file:
        reader_sales = csv.DictReader(sales_file,delimiter = ';',lineterminator='\n', quotechar='"')
        for sales_row in reader_sales:
            sales_id = (sales_row['sales_id'])
            if sales_id == str(stock_sales_id):
                return (sales_row['sales_unit_price'])


#function to find the sales date in the sales file that belongs to the sales id that will be added to the stock file.
def find_sales_date(stock_sales_id):
        #look in every row of the sales file and return the sales date for the specific sales id.
    with open('sales_overview.csv', mode='r',encoding='utf8',newline='') as sales_file:
        reader_sales = csv.DictReader(sales_file,delimiter = ';',lineterminator='\n', quotechar='"')
        for sales_row in reader_sales:
            sales_id = (sales_row['sales_id'])
            if sales_id == str(stock_sales_id):
                return (sales_row['sales_date'])

#function to calculate te profit for each line of the stock file. 
def line_profit(line_id):
    #don't calculate the header
    if (find_sales_price(match_sales_id(line_id))) == "line_profit":
        return ""
    #find the sales id based on the purchase id and from that the sales price. If this price does exist than return the following.       
    elif (find_sales_price(match_sales_id(line_id))) is not None:
        #return the found sales price minus (the purchase price that is found based on the purchase id).
        return float(find_sales_price(match_sales_id(line_id))) - float((find_purchase_price(line_id)))
    # this leaves the rows where the price does not exist, if this product, based on the purchase id is Expired, return 0 minus the purchase price.       
    elif find_expired(line_id) == 'Expired':
        return 0 - float((find_purchase_price(line_id)))
    #In the other cases: not expired and not sold, return no profit value.     
    else: 
        return ""

#function t ofind the week the product has been sold.
def sales_week(sales_date):
    try: 
        return datetime.strptime((sales_date), '%Y-%m-%d').isocalendar()[1]
    except: return ""

#the named tempory file function is called tempfile . 
tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

#function to check if a stock file exist, if not it creates it. It adds lines for new purchases, makes a note if a article is expired and adds sales info to the lines.
def stock_update():                                                 
    try:   
        # if file stock.csv does not exist, a new file is created with only headers of the columns.
        if not os.path.exists('stock.csv'):                  
                with open('stock.csv', mode='w',newline='') as stock_file: 
                    columns = ['stock_purchase_id','product_name','stock_purchase_price','stock_purchase_date','expiration_date','expired','stock_sales_id','stock_sales_price','stock_sales_date','line_profit','sales_week'] ###laatste 3 kolommen nog in de maak
                    writer = csv.DictWriter(stock_file, delimiter=';',lineterminator='\n', fieldnames=columns)
                    writer.writeheader()
                close
        # if file sales_overview.csv does not exist, a new file is created with only headers of the columns.
        if not os.path.exists('sales_overview.csv'):                                                                                                
            with open('sales_overview.csv', mode='w',newline='') as sales_file:                                                                  
                columns = ['sales_id','product_name','sales_unit_price','sales_date']                                      
                writer = csv.DictWriter(sales_file, delimiter=';',lineterminator='\n', fieldnames=columns)
                writer.writeheader()
                close  
        # the purchase file will be opened to read and from the stock file a temp file will be created.  
        with open('purchase_overview.csv', mode='r',encoding='utf8',newline='') as purchase_file, open('stock.csv', mode='w',encoding='utf8', newline='')\
             as tempfile,open('sales_overview.csv', mode='r',encoding='utf8',newline='') as sales_file: 
                columns = ['stock_purchase_id','product_name','stock_purchase_price','stock_purchase_date','expiration_date','expired','stock_sales_id', 'stock_sales_price','stock_sales_date','line_profit','sales_week']
                writer = csv.DictWriter(tempfile, delimiter=';',lineterminator='\n', fieldnames=columns)
                reader_a = csv.DictReader(purchase_file,delimiter = ';',lineterminator='\n', quotechar='"')
                writer.writeheader()
                #for every row of the purchase file a new row will be written in the tempfile. Every field is found by one of the functions above.
                for row_a in reader_a: 
                                writer.writerow({'stock_purchase_id':row_a['purchase_id'],'product_name':find_product_name(row_a['purchase_id']),\
                                    'stock_purchase_price':find_purchase_price(row_a['purchase_id']),'stock_purchase_date':find_purchase_date(row_a['purchase_id']),\
                                        'expiration_date':find_expiration_date(row_a['purchase_id']),'expired':find_expired(row_a['purchase_id']),\
                                            'stock_sales_id':match_sales_id(row_a['purchase_id']),'stock_sales_price':find_sales_price(match_sales_id(row_a['purchase_id'])),\
                                                'stock_sales_date':find_sales_date(match_sales_id(row_a['purchase_id'])),\
                                                'line_profit':line_profit(row_a['purchase_id']),'sales_week': sales_week(find_sales_date(match_sales_id(row_a['purchase_id'])))})        
                print('Stock.csv is updated')       
        #the tempfile will overwrite the earlier version of stock.csv.                             
        shutil.move(tempfile.name, 'stock.csv')
        close
        
        return''
    except PermissionError: print("WARNING! Stock file is not updated. Please close the file 'stock.csv' and try again or contact your network administrator.")

            

if __name__ == '__main__':
    print(stock_update())








    #het idee is nu om een purchase file te maken. 
    #er is ook een sales file, maar die moet nog checken in de stock file of het product ook beschikbaar is 
    #in de stock file moeten de lijnen komen die nog niet toegevoegd zijn uit de purchase file. Daarvoor nu een verschil check gemaakt in stock.py. ALs deze voorkomt in de purchase file dan moeten de data daarvan overgenomen worden. 
    #Daarna kan de sales file aangevuld worden met de check of het beschikbaar is. En die moet dan ook meteen de stock file updaten op de al bestaande regels
