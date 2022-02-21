from tkinter import *
from os import close
import subprocess
from main import sales_id_count, purchase_id_count


root = Tk()
root.geometry("850x710")
root.title('SuperPy')
root.configure(background='black')
c=Canvas(root,width=850,height=710,background='black')
header = Label(root,text='SuperPy',width=52, height=2,relief=RAISED ,background="#ff3791",font=('Ubuntu', 18, 'bold')).place(x=30, y=10)
#header = Label(root,text='',width=52, height=0.02,relief=RAISED ,background="#ff3791",font=('Ubuntu', 18, 'bold')).place(x=30, y=380)
c.pack()
c.create_line(425, 85, 425, 703, fill= "#ff3791")
c.create_line(7, 393, 843, 393, fill= "#ff3791")

#The purpose of the purchase button is to start this function:
def insert_purchase(): 
    # old line number +1 to check if a new line is created afterwards. 
    line_number = purchase_id_count() +1
    #start the function in the main.py page, with the information from the purchase entry boxes.
    subprocess.run("python main.py purchase " + product_entry_box.get() + " " + price_entry_box.get() + " " + expiration_entry_box.get())
    #If the line number is higher than the line number after the funtion, something went wrong and a warning message will appear in the screen. 
    if line_number > purchase_id_count():
        MessageLabel = Label(root,text= 'Warning: no new row added to purchase_overview.csv',width=97, height=3,relief=RAISED ,background="#ff3791",font=('Ubuntu', 10,"bold"))
        MessageLabel.place(x=30, y=640)
        root.after(8000,MessageLabel.destroy)
    #If the line number is equal to the line number after the funtion, a message will appear in the screen that the new line is created. 
    elif line_number == purchase_id_count():
        MessageLabel = Label(root,text= 'New product: row added to purchase_overview.csv',width=97, height=3,relief=RAISED ,background="#ff3791",font=('Ubuntu', 10,"bold"))
        MessageLabel.place(x=30, y=640)
        root.after(8000,MessageLabel.destroy)

#The purpose of the (purchase) refresh button is to start this function: 
#this wil clear the three entry boxes.
def refresh():
        product_entry_box.delete(0, 'end')
        price_entry_box.delete(0, 'end')
        expiration_entry_box.delete(0, 'end')

#The purpose of the (purchase) help button is to start this function: 
#this wil show you help lines.
def purchase_input_help():
    Label(root,text='Enter standard product name (single word or separated by underscore, "_").',font=('Ubuntu', 8),background='black',fg='#d252e3').place(x=30, y=250)
    Label(root,text='Enter the amount in Euro\'s, use only numbers,',font=('Ubuntu', 8),background='black',fg='#d252e3').place(x=30, y=270)
    Label(root,text='rounded to 2 decimal places separated by a decimal point (2.50).',font=('Ubuntu', 8),background='black',fg='#d252e3').place(x=40, y=290)
    Label(root,text='Enter the expiration date, format: year-month-day (2024-08-14).',background='black',font=('Ubuntu', 8),fg='#d252e3').place(x=30, y=310)
    Label(root,text='Purchase_overview.csv will be updated with new purchase info.',background='black',font=('Ubuntu', 8),fg='#d252e3').place(x=30, y=330)
    Label(root,text='Always close puchase_overview.csv before adding new sales, otherwise.',background='black',font=('Ubuntu', 8),fg='#d252e3').place(x=30, y=350)
    Label(root,text='it will not registrate new rows.',background='black',font=('Ubuntu', 8),fg='#d252e3').place(x=40, y=370)



#The purpose of the sales button is to start this function:
def insert_sales(): 
    # old line number +1 to check if a new line is created afterwards.
    line_number = sales_id_count() +1
    #start the function in the main.py page, with the information from the purchase entry boxes.
    subprocess.run("python main.py sales " + s_product_entry_box.get() + " " + s_price_entry_box.get())
    #If the line number is higher than the line number after the funtion, something went wrong and a warning message will appear in the screen. 
    if line_number > sales_id_count():
        MessageLabel = Label(root,text= 'Warning: no new row added to sales_overview.csv, check if this product is available!',width=97, height=3,relief=RAISED ,background="#ff3791",font=('Ubuntu', 10,"bold"))
        MessageLabel.place(x=30, y=640)
        root.after(8000,MessageLabel.destroy)
    #If the line number is equal to the line number after the funtion, a message will appear in the screen that the new line is created. 
    elif line_number == sales_id_count():
        MessageLabel = Label(root,text= 'Product availabe: row added to sales_overview.csv',width=97, height=3,relief=RAISED ,background="#ff3791",font=('Ubuntu', 10,"bold"))
        MessageLabel.place(x=30, y=640)
        root.after(8000,MessageLabel.destroy)

#The purpose of the (sales) refresh button is to start this function: 
#this wil clear the two entry boxes.    
def s_refresh():
        s_product_entry_box.delete(0, 'end')
        s_price_entry_box.delete(0, 'end')

#The purpose of the (sales) help button is to start this function: 
#This wil show you help lines.
def sales_input_help():
    Label(root,text='Enter standard product name (single word or separated by underscore, "_").',background='black',font=('Ubuntu', 8),fg="#71c571").place(x=460, y=250)
    Label(root,text='Enter the amount in Euro\'s, use only numbers,',background='black',font=('Ubuntu', 8),fg="#71c571").place(x=460, y=270)
    Label(root,text='rounded to 2 decimal places separated by a decimal point (2.50).',font=('Ubuntu', 8),background='black',fg="#71c571").place(x=470, y=290)
    Label(root,text='The stock will be checked to see if selling is possible.',background='black',font=('Ubuntu', 8),fg="#71c571").place(x=460, y=310)
    Label(root,text='Sales_overview.csv will be updated with new sales information.',background='black',font=('Ubuntu', 8),fg="#71c571").place(x=460, y=330)
    Label(root,text='Always close sales_overview.csv before adding new sales, otherwise',background='black',font=('Ubuntu', 8),fg="#71c571").place(x=460, y=350)
    Label(root,text='it will not registrate new rows.',background='black',font=('Ubuntu', 8),fg="#71c571").place(x=470, y=370)



#The purpose of the dashboard buttons is to start this function:
def return_period(p1,p2):
    #Start the function on the dashboard.py page, with the information of the chosen button and if needed of the the entry boxes. 
    subprocess.run("python dashboard_creation.py " + p1 + " " +p2)
    #A message will appear to tell the dashboard is created
    MessageLabel = Label(root,text='Dashboard information can be found in Superpy_dashboard.pdf',width=97, height=3,relief=RAISED ,background="#ff3791",font=('Ubuntu', 10,"bold"))
    MessageLabel.place(x=30, y=640)
    root.after(8000,MessageLabel.destroy)  

#The purpose of the (dashboard) help button is to start this function: 
#This wil show you help lines.
def profit_help():
    Label(root,text='Superpy_dashboard.pdf will be created or updated.',background='black',font=('Ubuntu', 8),fg="#51dee5").place(x=30, y=600)
    Label(root,text='Save this file under a new name if you would like to keep it.',background='black',font=('Ubuntu', 8),fg="#51dee5").place(x=30, y=620)
    Label(root,text='Enter the dates in format: year-month-day (2024-08-14).',background='black',font=('Ubuntu', 8),fg="#51dee5").place(x=30, y=640)
    Label(root,text='If you choose a period for which no information exist, the dashboard',background='black',font=('Ubuntu', 8),fg="#51dee5").place(x=30, y=660)
    Label(root,text='will not update and shows the information of your previous request.',background='black',font=('Ubuntu', 8),fg="#51dee5").place(x=40, y=680)

#The purpose of the (dashboard) refresh button is to start this function: 
#this wil clear the two entry boxes.   

def period_refresh():
        period_entry_box.delete(0, 'end')
        period2_entry_box.delete(0, 'end')



#The purpose of the stock update button is to start this function:
#This will update the stock file with purchase and sales information, for if you corrected something manually in one of these files. 
def stock_update():
    subprocess.run("python stock.py")    
    MessageLabel = Label(root,text= 'Stock_update.csv will the show last info of the sales and purchase files',width=97, height=3,relief=RAISED ,background="#ff3791",font=('Ubuntu', 10,"bold"))
    MessageLabel.place(x=30, y=640)
    root.after(8000,MessageLabel.destroy)  

#The purpose of the (stock update) help button is to start this function: 
#This wil show you a help line.
def stock_input_help():
    Label(root,text='The file Stock.csv will be updated with latest purchase and sales info.',font=('Ubuntu', 8),background='black',fg="#ff7a37").place(x=460, y=460)


#Below lines tell the location of the purchase texts entry boxes.
purchase_text = Label(root,text='Enter the details of your new purchase',font=('Ubuntu', 10),background='black',fg="#d252e3")
purchase_text.place(x=30, y=100)
product_text = Label(root,text='Product name:',background='black',font=('Ubuntu', 8),fg="#d252e3")
product_text.place(x=30, y=130)
product_entry_box = Entry(root,width=26,borderwidth=2)
product_entry_box.place(x=220,y=130)
price_text = Label(root,text='Unit price:',font=('Ubuntu', 8),background='black',fg="#d252e3")
price_text.place(x=30, y=160)
price_entry_box = Entry(root,width=26,borderwidth=2)
price_entry_box.place( x=220,y=160)    
expiration_text = Label(root,text='Expiration date (yyyy-mm-dd):',font=('Ubuntu', 8),background='black',fg="#d252e3")
expiration_text.place(x=30, y=190)
expiration_entry_box = Entry(root,width=26,borderwidth=2)
expiration_entry_box.place(x=220,y=190)

#Below lines tell where the location of the purchase buttons and which funtion to run.
purchase_button = Button(root,text='Purchase',font=('Ubuntu', 8),command=insert_purchase,background="#d252e3",borderwidth=4)
purchase_button.place(x=32, y=220)
refresh_button = Button(root,text='Refresh',font=('Ubuntu', 8),command=refresh,background="#d252e3",borderwidth=4)
refresh_button.place(x=142, y=220)
help_purchase_button = Button(root,text='Help',font=('Ubuntu', 8),command=purchase_input_help,background="#d252e3",borderwidth=4)
help_purchase_button.place(x=346, y=220)



#Below lines tell the location of the sales texts entry boxes.
sales_text = Label(root,text='Enter the details of your new sales',font=('Ubuntu', 10),background='black',fg="#71c571")
sales_text.place(x=462, y=105)
s_product_text = Label(root,text='Product name:',font=('Ubuntu', 8),background='black',fg="#71c571")
s_product_text.place(x=462, y=130)
s_product_entry_box = Entry(root,width=26,borderwidth=2)
s_product_entry_box.place(y=130, x=650)
s_price_text = Label(root,text='Unit price:',font=('Ubuntu', 8),background='black',fg="#71c571")
s_price_text.place(x=462, y=160)
s_price_entry_box = Entry(root,width=26,borderwidth=2)
s_price_entry_box.place(y=160, x=650)    

#Below lines tell where the location of the sales buttons and which funtion to run.
sales_button = Button(root,text='Sales',font=('Ubuntu', 8),command=insert_sales,background="#71c571",borderwidth=4)
sales_button.place(x=462, y=220)
s_refresh_button = Button(root,text='Refresh',font=('Ubuntu', 8),command=s_refresh,background="#71c571",borderwidth=4)
s_refresh_button.place(x=580, y=220)
help_sales_button = Button(root,text='Help',font=('Ubuntu', 8),command=sales_input_help,background="#71c571",borderwidth=4)
help_sales_button.place(x=776, y=220)



#Below lines tell the location of the dashboard text.
profit_text = Label(root,text='Create a new dashboard for the chosen period',font=('Ubuntu', 10),background='black',fg="#51dee5")
profit_text.place(x=30, y=400)

#Below lines tell where the location of the dashboard buttons and which funtion to run.
profit_button = Button(root,text='Today',font=('Ubuntu', 8),command=lambda: return_period('today','today'),background="#51dee5",borderwidth=4)
profit_button.place(x=32, y=430)
profit_button = Button(root,text='Yesterday',font=('Ubuntu', 8),command=lambda: return_period('yesterday','yesterday'),background="#51dee5",borderwidth=4)
profit_button.place(x=120, y=430)
profit_button = Button(root,text='Current week',font=('Ubuntu', 8),command=lambda: return_period('current_week','current_week'),background="#51dee5",borderwidth=4)
profit_button.place(x=220, y=430)
profit_button = Button(root,text='Last week',font=('Ubuntu', 8),command=lambda: return_period('last_week','last_week'),background="#51dee5",borderwidth=4)
profit_button.place(x=32, y=470)
profit_button = Button(root,text='Current month',font=('Ubuntu', 8),command=lambda: return_period('current_month','current_month'),background="#51dee5",borderwidth=4)
profit_button.place(x=120, y=470)
profit_button = Button(root,text='Last month',font=('Ubuntu', 8),command=lambda: return_period('last_month','last_month'),background="#51dee5",borderwidth=4)
profit_button.place(x=220, y=470)
profit_button = Button(root,text='Current year',font=('Ubuntu', 8),command=lambda: return_period('current_year','current_year'),background="#51dee5",borderwidth=4)
profit_button.place(x=32, y=510)
profit_button = Button(root,text='Last year',font=('Ubuntu', 8),command=lambda: return_period('last_year','last_year'),background="#51dee5",borderwidth=4)
profit_button.place(x=120, y=510)
profit_button = Button(root,text='Help',font=('Ubuntu', 8),command=profit_help,background="#51dee5",borderwidth=4)
profit_button.place(x=346, y=430)
refresh_button = Button(root,text='Refresh',font=('Ubuntu', 8),command=period_refresh,background="#51dee5",borderwidth=4)
refresh_button.place(x=330, y=470)

#Below lines tell the location of the manual period dashboard text, entry boxes and button.
period_text = Label(root,text='For manual period (yyyy-mm-dd)',font=('Ubuntu', 10),background='black',fg="#51dee5")
period_text.place(x=30, y=540)
period_text = Label(root,text='Enter the start date:',font=('Ubuntu', 8),background='black',fg="#51dee5")
period_text.place(x=30, y=560)
period_entry_box = Entry(root,width=17,borderwidth=2)
period_entry_box.place(x=32,y=580)
price_text = Label(root,text='Enter the end date:',font=('Ubuntu', 8),background='black',fg="#51dee5")
price_text.place(x=160, y=560)
period2_entry_box = Entry(root,width=17,borderwidth=2)
period2_entry_box.place( x=162,y=580)    
manual_button = Button(root,text='Manual period',font=('Ubuntu', 8),command=lambda: return_period(period_entry_box.get(),period2_entry_box.get()) ,background="#51dee5",borderwidth=4)
manual_button.place(x=220, y=510)



#Below lines tell the location of the stock update button.
stock_text = Label(root,text='Stock update',font=('Ubuntu', 10),background='black',fg="#ff7a37")
stock_text.place(x=460, y=400)
stock_button = Button(root,text='Stock update',command=stock_update,background="#ff7a37",borderwidth=4)
stock_button.place(x=462, y=430)
help_stock_button = Button(root,text='Help',font=('Ubuntu', 8),command=stock_input_help,background="#ff7a37",borderwidth=4)
help_stock_button.place(x=776, y=430)


 

root.mainloop()
