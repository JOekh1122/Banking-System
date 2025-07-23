import random
def check_balance(name,init_balance):
    print(f"\n{name} balance is: {init_balance}")

def deposit(name,init_balance):
 try:
    amount=int(input("Enter Deposit amount: "))
    init_balance+=amount
    return init_balance
 except ValueError:
     print("Invalid input, please try again\n")
     return deposit(name,init_balance)

def create_account():
    name = input("Enter your name: ")
    try:
     init_balance = float(input("Enter your initial balance: "))
     print(f"Welcome {name} Your Balance is: {init_balance}")
     main_menu(name,init_balance)
    except ValueError:
        print("Invalid Initial Balance")
        create_account()


def withdraw(name, init_balance):
    while True:
        try:
            amount = int(input("Enter Withdraw amount: "))
            if amount <= init_balance:
                init_balance -= amount
                print(f"Withdraw successful! Your new balance = {init_balance}")
                return init_balance
            else:
                print(f"Invalid Withdraw, {name}! Your balance = {init_balance}")
        except ValueError:
            print("Please enter a valid number.")


def main_menu(name,init_balance):
 while True:
     operation=input("1]Check Balance\n2]Deposit\n3]WithDraw\n4]Exit\nEnter your choice: ")
     if operation=="1":
       check_balance(name,init_balance)
     elif operation=="2":
       init_balance=deposit(name,init_balance)
       check_balance(name,init_balance)
     elif operation=="3":
        init_balance=withdraw(name,init_balance)
        check_balance(name, init_balance)

     elif operation == "4":
        print(f"Thank you for using our bank system! {bank} Bank")
        break
     else:
         print("Invalid choice")



banks=["CIB","SAIB","HSBC","AL_AHLY"]
bank=random.choice(banks)
print(f"Welcome to {bank} Bank.")
choise=input("Enter your choice\n1]Create Account\n2]Exit\n")

if choise == "1":
    create_account()
elif choise == "2":
    quit()
else:
    print("Invalid choice")



