1.
This function checks if the product to sell is available to sell, because otherwise it could be noted down as sold while it is already sold or expired. 
It checks in the stock file if the expiration date is today of higher and if the profit field is empty, because that field will be full when a product is sold or it its expired. 

def check_inventory(product_to_sell):
    with open ('stock.csv', 'r') as stock_file: 
        reader = csv.DictReader(stock_file,delimiter = ';',lineterminator='\n', quotechar='"')                                        
        for row in reader: 
               if product_to_sell == (row['product_name']):
                    if(row['expiration_date']) >= set_date.today:
                        if (row['line_profit']) == "":
                            return 1 

2.
This is  the writer of the function to create lines in the stock file. 
It reads the lines of the purchase file and for every line it creates a line in the stock file. 
It contains a function for every field of the file. so it's easier to track what data is used, by looking at the different functions. 

for row_a in reader_a: 
                                writer.writerow({'stock_purchase_id':row_a['purchase_id'],'product_name':find_product_name(row_a['purchase_id']),\
                                    'stock_purchase_price':find_purchase_price(row_a['purchase_id']),'stock_purchase_date':find_purchase_date(row_a['purchase_id']),\
                                        'expiration_date':find_expiration_date(row_a['purchase_id']),'expired':find_expired(row_a['purchase_id']),\
                                            'stock_sales_id':match_sales_id(row_a['purchase_id']),'stock_sales_price':find_sales_price(match_sales_id(row_a['purchase_id'])),\
                                                'stock_sales_date':find_sales_date(match_sales_id(row_a['purchase_id'])),\
                                                'line_profit':line_profit(row_a['purchase_id']),'sales_week': sales_week(find_sales_date(match_sales_id(row_a['purchase_id'])))})        
      


3.
This is the function that is called when you press the sales button. It uses the command line with sales sub parser to activate main.py to create lines. 
It checks if the supposed new line number is higher than the max line id number that the file has. 
If no new line is created a warning message will appear, this will vanish after a little while. 
If the correct id is found the message will be shown that a new line is created.  

def insert_purchase(): 
    line_number = purchase_id_count() +1
    subprocess.run("python main.py purchase " + product_entry_box.get() + " " + price_entry_box.get() + " " + expiration_entry_box.get())
    if line_number > purchase_id_count():
        MessageLabel = Label(root,text= 'Warning: no new row added to purchase_overview.csv',width=97, height=3,relief=RAISED ,background="#ff3791",font=('Ubuntu', 10,"bold"))
        MessageLabel.place(x=30, y=640)
        root.after(8000,MessageLabel.destroy)
    elif line_number == purchase_id_count():
        MessageLabel = Label(root,text= 'New product: row added to purchase_overview.csv',width=97, height=3,relief=RAISED ,background="#ff3791",font=('Ubuntu', 10,"bold"))
        MessageLabel.place(x=30, y=640)
        root.after(8000,MessageLabel.destroy)

