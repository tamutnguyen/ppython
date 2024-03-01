print('-----------------------------------------')
print('***Wellcome to Stock value Calculator Program! ***')
print('-----------------------------------------')
stock_name=input("Enter stock's name:")
total_purchased=int(input("Enter the total number of purchased shares:"))
if(total_purchased <0):
    print('Error: Number of purchased shared should be >=0')
    exit()
amount_paid=float(input("Enter the dollar amount paid per a purchased share:"))
if(amount_paid <0):
    print('Error: The purchased amount should be >0')
    exit()
total_sold=int(input("Enter the total number of sold shares:"))
####1111111

if(total_sold <0 or total_sold > total_purchased):
    print('Error: Number of sold share should be >=0 and must be <=number of purchased shares')
    exit()
amount_sold=float(input("Enter the dollar amount paid per a sold share:"))
if(amount_sold <0):
    print('The sold amount should be >0')
    exit()
if(total_purchased < 1000):
    purchase_comission=100 
else:
    purchase_comission=0
sold_comission=0
if(total_sold < 1000):
    sold_comission=100
elif(total_sold>=1000 and total_sold <2000):
    sold_comission=50
else:
    sold_comission=0

total_purchased_amount=total_purchased * amount_paid
total_sold_amount=total_sold * amount_sold
profit=total_sold_amount - total_purchased_amount - purchase_comission - sold_comission
print('*****************************************')
print("\t \t Purchasing Report \t \t")
print('*****************************************')
print("Stock name:",stock_name)
print("Total purchased amount:$"+str(total_purchased_amount))
print("Purchase commitment:$"+str(purchase_comission))
print('*****************************************')
print("\t \t Selling Report \t \t")
print('*****************************************')
print("Total sold amount:$"+str(total_sold_amount))
print("Sold commitment:$"+str(sold_comission))
print('*****************************************')
if profit >0:
    print("Congraduation, Total Profit:$"+str(profit))
elif profit<0:
    print("Good Luck Next Time, Total Profit:$"+str(profit))
else:
    print("No profit or loss, Total Profit:$"+str(profit))
print('*****************************************')










