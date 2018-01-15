"""
Emergency Retail POS
Quick fix to add totals with tax
Tracks purchases and totals
"""

tax = float(input("What is tax: ")) #Sets amount of tax applied to each purchase
total_sales = 0 #Total $ value of purchase
sales = [] #List of individual items
sales_with_tax = [] #List of items plus tax
sales_tax = 0 #Cost of item plus tax
item = 1

while True:
    sale = float((input("Price of item number {} before taxes: ".format(item))))
    if sale == 0: #Exits loop and displays total
        print("="*40)
        item -= 1 #Ensure item count is correct
        print ("Total sales with tax: {}".format(total_sales)) #Total cost of purchase
        print("Total number of items: {}".format(item)) #How many items in cart
        break
    elif sale > 0:
        taxes = sale * tax
        sale_with_tax = round(sale + taxes, 2) #Rounds to two decimals places
        sales.append(sale)
        sales_with_tax.append(sale_with_tax)
        total_sales += sale_with_tax
        item += 1
        print("_" * 40)
        print("There are {} items".format(item - 1))
        print("Items without tax: $ {}".format(sales))
        print ("Items with tax: ${}".format((sales_with_tax)))
        print("Total purchase with tax: {}".format(round(total_sales, 2)))
        pass
