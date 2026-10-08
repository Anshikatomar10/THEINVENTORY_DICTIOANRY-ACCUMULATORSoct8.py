# THE INVENTORY DICTIONARY & ACCUMULATORS .
# this program needs to sell snacks , keep trak of limited stock (inventory),handle purchases , and
#automaticaly apply a discount if the user is a vip member .
#the inventory dictionary : "popcorn":$6.00 , stock:10, "soda":$4.50,stock:15, "candy":$3.50 ,stock:5
#Give discount to the VIP members and calculate the grand_total at the end of the loop .

#step1 set up the dictionary for the items price and stock availablity.
inventory = {
         "popcorn":{"price":6.00, "stock":10},
         "soda":{"price":4.50,"stock":15},
         "candy":{"price":3.50,"stock":5}
     }                       
# set sccumulators set to false and 0.0
vip_status = False
grand_total = 0.0

while True:#set a while loop so the program keep repeating until you want it to end .
    #ask for snack prefrence and give the word to end the loop if want to .
    snack = str(input("enter the snack you want to buy (or 'done' to checkout : )")).lower().strip()
    if snack == "done":# end the loop if that word is typed by the user .
        break
    if snack not in inventory :# check if item is in inventory or not.
        print("sorry we do not sell this item .") # if not available print a message conveing the problem.     
        continue # continue to ask for other item .
    elif inventory[snack]["stock"]== 0 :# check if the item is available in number (in stock).
        # if not available then convey the message using the print receipt.
        print("sorry the item is sold out .")
        continue
    # if the item is available in stock then calculate the price 
    price = inventory[snack]["price"]
    #step 3 set up a loop for asking quantity the customer wanna buy of that particular snack they choose.
    while True:
        try:
            quantity = int(input("enter the quantity of your choosen item in whole number :"))
            break # if the user enters a valid number .break from the loop
        except ValueError:
            print("please enter a valid whole number")# if the number is not valid ,ask them to reenter .
    # step 4 ask for membership status and apply the discount accordingly .        
    vip_status = str(input("are you a VIP member enter ye/no : ")).lower().strip()        
    if vip_status == "yes": #if the customer is a vip member give 10% disscount .
           your_total = (price*quantity)*0.90
    elif vip_status == "no": # if not calculate the price without any discount .
           your_total = (price*quantity)*1
    else:
          your_total = (price*quantity)*1 
    # step 5 decrease the number of stock availablity with each purchase.      
    inventory[snack]["stock"] -= quantity
    print(your_total) # print the total for each user . 
#step 5 after the loop ends calculate the grand_total(full day revenue).by adding each purchase all together.
    grand_total += your_total 
#print the grand total as final output .    
print("your today's revenue is :$",grand_total)                         
