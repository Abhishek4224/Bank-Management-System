# BANK SERVICES 
from database import *
import datetime
class Bank():
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number
        self.create_transaction_table
        
        
    def create_transaction_table(self):
        db_query(f"""CREATE TABLE IF NOT EXISTS {self.__username}_TRANSACTIONS (
            timedate varchar(30),
            account_number INTEGER,
            remarks varchar(30),
            amount INTEGER)""")
    
    def balance_enquiry(self):
        temp = db_query(f"select balance from customers where username = '{self.__username}'")
        print(f"\n{self.__username} your balance is Rs. {temp[0][0]}\n")
    
        
    def deposit(self,ammount_to_deposit):
        acc = db_query(f"""select account_number from customers where username = '{self.__username}'""")
        temp = db_query(f"""select balance from customers where username = '{self.__username}'  """)
        test = temp[0][0] + ammount_to_deposit
        db_query(f"update customers set balance = '{test}' where username = '{self.__username}'")
        self.balance_enquiry()
        db_query(f"""INSERT INTO {self.__username}_transactions VALUES
                 ('{datetime.datetime.now()}',
                 '{acc[0][0]}',
                 'Deposited',
                 '{ammount_to_deposit}')""")
        print(f"{self.__username} Ammount has deposited successfully.. to your account {acc[0][0]}")
        
        
        
    def withdraw(self,ammount):
        acc = db_query(f"""select account_number from customers where username = '{self.__username}'""")
        temp = db_query(f"""select balance from customers where username = '{self.__username}'  """)
        if ammount > temp[0][0]:
            print("Insufficient balance")
        else:
            test = temp[0][0] - ammount
            db_query(f"update customers set balance = '{test}' where username = '{self.__username}'")
            self.balance_enquiry()
            db_query(f"""insert into {self.__username}_transactions values
                      ('{datetime.datetime.now()}',
                      '{acc[0][0]}',
                      'Withdraw',
                      '{ammount}')""")
        print(f"{self.__username} Ammount has successfully withdrawn from your account {acc[0][0]}")
        
    
    def fund_transfer(self, receive ,amount):
        temp = db_query(f"""select balance from customers where username = '{self.__username}'  """)
        if amount > temp[0][0]:
            print("Insufficient Balance..!!")
        else:
            temp2 = db_query(f"""select balance from customers where account_number = '{receive}' """)
            test1 = temp[0][0] - amount
            test2 = amount + temp2[0][0]
            db_query(f"update customers set balance = '{test1}' where username = '{self.__username}';")
            db_query(f"update customers set balance = '{test2}' where account_number = '{receive}';")
            
            receiver_username = db_query(f"""select username from customers where account_number = '{receive}';""")
            self.balance_enquiry()
            db_query(f"""insert into {receiver_username[0][0]}_transactions values
                    ('{datetime.datetime.now()}',
                    '{receive}',
                    'from {self.__account_number}',
                    '{amount}')""")
            
            db_query(f"""insert into {self.__username}_transactions values
                    ('{datetime.datetime.now()}',
                    '{self.__account_number}',
                    'to {receive}',
                    '{amount}')""")
            print(f"{self.__username} Ammount has transferred successfully.. to '{receive}'")