print("-----------SHOPPING BILL FOR STATIONERY ITEMS-----------")
print("Here are the items for you select which of the items you want, how many you want ? just go for it") 
print("1.Pen:-      10Rs")
print("2.Paper:-     2Rs")
print("3.Pencil:-    5Rs")
print("4.Eraser:-    7Rs")
print("5.Book:-     25Rs")
a=1
price1,price2,price3,price4,price5=0,0,0,0,0
while a>0:
     choice=int(input("Enter the choice no."))
     if choice==1:
         num1=int(input("Enter how many pens do you want?:-"))
         price1+=num1*10
         print("Total price for pens is:-",price1)
     elif choice==2:
         num2=int(input("Enter how many papers do you want?:-"))
         price2+=num2*2
         print("Total price for papers is:-",price2)
     elif choice==3:
         num3=int(input("Enter how many pencils do you want?:-"))
         price3+=num3*5
         print("Total price for pencils is:-",price3)
     elif choice==4:
         num4=int(input("Enter how many erasers do you want?:-"))
         price4+=num4*7
         print("Total price for erasers is:-",price4)
     elif choice==5:
         num5=int(input("Enter how many books do you want?:-"))
         price5+=num5*25
         print("Total price for books is:-",price5)
     else:
         print("Invalid Choice no.")
     x=input("Do you wish to continue(y/n)")
     if x=="y":
         continue
     else:
         print("------THANK YOU-------")
         a=-1
total_price= price1+price2+price3+price4+price5
print("Total price for the stationery items is:-",total_price)
gst=(12*total_price)/100
sgst=gst/2
cgst=gst/2
print("CGST:-",cgst,"Rs")
print("SGST:-",sgst,"Rs")
Total_price=total_price+cgst+sgst
print("Total Price of items is:- ",Total_price)
delivery_charge=100
if Total_price<500:
    print("Total Price of items after delivery charge is:- ",Total_price+delivery_charge)
else:
    print("Total Price of items is:- ",Total_price)
# This program is written by Pratham Jindal.