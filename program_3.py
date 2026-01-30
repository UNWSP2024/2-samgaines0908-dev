 #Author: Sam Gaines
    #Date: 1/20/2026
    #Title: Total Purchase
def calculate_total_purchase():
    # A customer in a store is purchasing five items.
    item1= int(input("Hello, Please enter the first items cost: "))
    item2= int(input("Enter the second item cost: "))
    item3= int(input("Enter the third item cost: "))
    item4= int(input("Enter the fourth item cost: "))
    item5= int(input("Enter the fifth item cost: "))
    sub_total= item1 + item2 + item3 + item4 + item5
    sales_tax_amount= 0.07
    # the amount of sales tax, and the total.
    sales_tax_amount= sales_tax_amount*sub_total
    print("sub_total: ",sub_total)
    print("sales_tax_amount: ",sales_tax_amount)
    print("total purchase: ",sub_total + sales_tax_amount)

calculate_total_purchase()
