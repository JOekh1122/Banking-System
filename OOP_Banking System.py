import random
from operator import truediv


class Account:
    def __init__(self,Name,balance):
        self.Name = Name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount


    def check_Balance(self):
        return self.balance

    def withdraw(self,amount):
        if(self.balance >= amount):
         self.balance -= amount
        else :
         print("Insufficient balance, please try again\n")

def main_menu(account,bank):
 while True:
     operation=input("1]Check Balance\n2]Deposit\n3]WithDraw\n4]Exit\nEnter your choice: ")
     if operation=="1":
       balance=account.check_Balance()
       print(f"{account.Name} your account balance is: {balance}")
     elif operation=="2":
      try:
          deposit_amount=float(input("Enter your deposit amount: "))
          account.deposit(deposit_amount)
          print(f"Your deposit amount is: {deposit_amount} is now deposited")
          print(f"{account.Name} your account balance is: {account.check_Balance()}")
      except ValueError:
          print("Invalid Ammount, please try again\n")

     elif operation=="3":
         try:
             withdraw_amount = float(input("Enter your withdraw amount: "))
             account.withdraw(withdraw_amount)
             print(f"Your withdraw amount is: {withdraw_amount} is now withdrawn")
             print(f"{account.Name} your account balance is: {account.check_Balance()}")
         except ValueError:
             print("Invalid Ammount, please try again\n")


     elif operation == "4":
        print(f"Thank you for using our bank system! {bank} Bank")
        break
     else:
         print("Invalid choice")







def create_account(bank):
    name = input("Enter your name: ")
    try:
     init_balance = float(input("Enter your initial balance: "))
     print(f"Welcome {name} Your Balance is: {init_balance}")
     account = Account(name,init_balance)
     main_menu(account,bank)
    except ValueError:
        print("Invalid Initial Balance")
        create_account(bank)





banks=["CIB","SAIB","HSBC","AL_AHLY"]
bank=random.choice(banks)
print(f"Welcome to {bank} Bank.")
choise=input("Enter your choice\n1]Create Account\n2]Exit\n")

if choise == "1":
   create_account(bank)

elif choise == "2":
    quit()
else:
    print("Invalid choice")