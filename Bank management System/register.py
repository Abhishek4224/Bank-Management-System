# USER REGISTRATION SIGNIN SIGNUP
from database import *
import random
from customer import *
from bank_services import Bank

def signup():
    username =  input("Create Username: ")
    temp = db_query(f"SELECT username from customers where username = '{username}';")
    if temp:
        print("Entered Username is already exist..!!!")
        signup()
    else:
        print("You may Proceed..")
        password = input("Enter your password = ")
        name = input("Enter your name = ")
        age = int(input("Enter your age = "))
        city = input("Enter your city = ")
        while True:
            account_number = random.randint(10000000,99999999)
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            
            if temp:
                continue
            else:
                print(f"Your Account Number is = '{account_number}'")   
                break

    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()
    
    
def signin():
    username = input("\nenter username = ")
    temp = db_query(f"select username from customers where username = '{username}';")
    if temp:
        while True:
            password = input(f"\nWelcome {username.upper()}\nEnter your password = ")
            temp = db_query(f"select password from customers where username = '{username}'")
            if temp[0][0] == password:
                print("Signin Successfully..")
                return username
                
                
            else:
                print("enter correct password !!!! \n")
                continue
                
        
    else:
        print("Please.. Enter correct username !!")
        signin()