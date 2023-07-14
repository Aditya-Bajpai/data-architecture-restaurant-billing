import mysql.connector


from tabulate import tabulate



mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "adidata",
        database = "hhw_project",
        auth_plugin='mysql_native_password'
    )


mycursor = mydb.cursor()
menu_type = input("Would you like to see the Veg Menu, Non-Veg menu, or both?: ")
if menu_type == "both":
    for i in range(1):
        '''print("item", end = "\t")
        print("price per item", end = "\t")
        print("stock", end = "\t")'''
    
        mycursor.execute(f"select * from menu")
        data = []
        for x in mycursor:
        
            data.append([x[0],x[1],x[2],x[3],x[4]])
    print (tabulate(data, headers=["Sno"," Item name", "Price", "Stock", "Vgetarian"]))
elif menu_type == "veg":
    for i in range(1):
        '''print("item", end = "\t")
        print("price per item", end = "\t")
        print("stock", end = "\t")'''
    
        mycursor.execute(f"select * from menu where Vegetarian = 'Yes'")
        data = []
        for x in mycursor:
        
            data.append([x[1],x[2],x[3]])
    print (tabulate(data, headers=["Item name", "Price", "Stock"]))
elif menu_type == "non-veg":
    for i in range(1):
        '''print("item", end = "\t")
        print("price per item", end = "\t")
        print("stock", end = "\t")'''
    
        mycursor.execute(f"select * from menu where Vegetarian = 'No'")
        data = []
        for x in mycursor:
        
            data.append([x[1],x[2],x[3]])
        
    print (tabulate(data, headers=["Item name", "Price", "Stock"]))

n = int(input("how many items would you like to purchase?: "))
order = []
quant = []
price = []
for i in range(n):
    name = input("enter item name: ")
    quantity = int(input("enter the number of servings of the above inputted item: "))
    mycursor.execute(f"select * from menu where item_name = '{name}'")
    for x in mycursor:
        if x[3] < quantity:
            print(f"There is not enough stock of the inputted item. Stock of {name}: {x[3]}")
            break
        else:
            print("Ordered registered.")
        new_stock = x[3] - quantity
        mycursor.execute(f"update menu set stock = {new_stock} where item_name = '{name}'")
        order.append(name)
        quant.append(quantity)
        price.append(x[2])
        mydb.commit()
    total = 0
    tot_price = 0
    
    for i in range(len(quant)):
        tot_price += quant[i]*price[i]
    
print(tot_price)
gst_price = tot_price*1.18

print("BILL")
print("===========")

for i in range(len(order)):
    print(order[i], end = "\t")
    print(price[i], end="\t")
    print(quant[i], end = "\t")
    print(quant[i]*price[i])

print(f"Total Bill: {tot_price}")
print(f"price GST included: {gst_price}")
        


'''for x in mycursor:
  print(x)'''



