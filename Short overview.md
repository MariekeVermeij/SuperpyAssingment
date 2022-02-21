In this Superpy program there are five python files. 

Set_dte.py with the dates of today and yesterday.

In main.py you can find the sub parsers for the sales and purchasing data. 
For purchasing it will create new lines in a csv file with the entered data, a purchase id from purchase_id_count() and the entered date. 
Stock.py is also imported in main.py because before sales a check is done if the product is available and not expired.

In stock.py the stock file will be created with information of purchase and sales files and other calculated data. 
It's put in an new file to have also two more simple documents for a quick view on purchase or sales data. 
Stock.py searches with different functions in the two files and matches the right part that is sold to the part that was in stock. 
A lot of different functions are created because otherwise it would be unreadable what the writer in stock_update() is doing. 

In dashboard_creation.py the function for the period to use for the dashboard and the creation of the dashboard itself are stored. 
The period function contains a lot of option, because buttons are used for the most common periods to use. 
This makes it a lot easier for the user to create a dashboard for a specific period, there is also an option to add other dates. 
Mathplolib is used to make graphs and send these to a pdf file. 

In superpy.py the interface is build up. There are buttons and entry fields, information messages appear after certain operations have been performed. 
The different sections have different colors to make it clear which information is needed and which information the user don’t have to pay attention to. 
The buttons will activate subprocess.run to use the command line to start the functions on the python file that has to be executed. 
