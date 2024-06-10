import time

print("Please insert your CARD")

time.sleep(5)

password = 123456

pin = int(input("Enter yout card pin"))

balance = 5000

if pin == password:
    while True:
                
        print("""
              1. Balance
              2. Withdraw Balance
              3. Deposite Balance
              4. Exit
              """)
        
        try:
            option = int(input("Please Enter given choice"))
        except:
            print("Please Enter valid choice")   

        if option == 1:
            print(f"Your current balance is {balance}")
            print("\n")

        if option == 2:
            withdraw_amount = int(input("Please enter withdraw amount"))
            print("\n ")
            balance = balance - withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print("\n")
            print(f"Your current balance is {balance}")
            print("\n")

        if option == 3:
            deposite_amount = int(input("Please enter deposite amount"))
            balance = balance + deposite_amount
            print("\n")
            print(f"{deposite_amount} is credited to your account")
            print("\n")
            print(f"Your updated balance is {balance}")
            print("\n")

        if option == 4:
            break    
            
else:
    print("Wrong Pin .... Please try again")
