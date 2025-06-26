from register import *
from bank_services import *
status = False

print("Welcome to Abhishek Banking Project")
while True:
    try:
        register = int(input("1. Sign up\n""2. SignIn\nEnter your choice = "))
        
        if register == 1 or register == 2:
            if register == 1:
                signup()
                
            if register == 2:
                user = signin()
                status = True
                break
                
        else:
            print("Please Enter Valid Input from Options")
        
    except ValueError:
        print("Enter 1 or 2 only ")
      
      
      
      
account_number = db_query(f"select account_number from customers where username = '{user}';")
      
while status:
    print(f"{user.capitalize()}, Choose your banking service..\n")  

    try:
        facilities = int(input("1. Balance enquiry\n""2. Cash deposit\n""3. Cash withdraw\n" "4. Fund transfer\n"  "Enter your choice = "))
    
        
        if facilities >= 1 or facilities <= 4:
            if facilities == 1:
                bobj =  Bank(user, account_number)
                bobj.balance_enquiry()                                 

                
                
            elif facilities == 2:
                while True:
                    try:
                        ammount_to_deposit = int(input("Enter ammount to deposit = "))
                        bobj =  Bank(user, ammount_to_deposit)
                        bobj.deposit(ammount_to_deposit)
                        mydb.commit()
                        choice = input("\nDo you want to continue (y/n) = ")
                        if choice == 'y':
                            ammount_to_deposit
                        elif choice == 'n':
                            break
                        
                    except ValueError:
                        print("Please enter a valid input..!!!")
                        

            elif facilities == 3:
                while True:
                    try:
                        ammount = int(input("Enter ammount to withdraw = "))
                        bobj =  Bank(user, ammount)
                        bobj.withdraw(ammount)
                        mydb.commit()
                        choice = input("\nDo you want to continue (y/n) = ")
                        if choice == 'y':
                            ammount
                        elif choice == 'n':
                            break
                    except ValueError:
                        print("please enter a valid input..!!!")
                        
                
                
            elif facilities == 4:
                while True:
                    try:
                        receive = int(input("enter receiver account number = "))
                        amount = int(input("enter Ammount to transfer = "))
                        bobj =  Bank(user, account_number[0][0])
                        bobj.fund_transfer(receive, amount)
                        mydb.commit()
                        break
                        
                    except ValueError:
                        print("Please enter valid input ie. number !!")
                        continue
                
                
        else:
            print("Please Enter Valid Input from Options")
            continue
        
    except ValueError:
        print("Enter 1 or 2 only ")
        