from bank import bankaccount

def main():
    customer=bankaccount()
    while True:
        print("""
        ====== GOLDMAN SAMS =======
        1. Create account
        2. Check balance
        3. Withdraw funds
        4. Deposit funds
        5. Transfer funds
        6.Exit
        """)
        choice = input("Enter choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        if choice==1:
            customer.create_account()
        elif choice==2:
            customer.view_balance()
        elif choice==3:
            amount=int(input("How much would you like to withdraw today?"))
            customer.withdraw(amount)
            print("You've succefully withdrawn ${}".format(amount))
        elif choice==4:
            amount=int(input("How much would you like to Deposit today?"))
            customer.deposit(amount)
            print("You've succefully deposited ${}".format(amount))
        elif choice==5:
            amount=int(input("How much would you like to tranfer?"))
            customer.transfer(amount)
            print("You've succefully transferred ${}".format(amount))
        elif choice==6:
            break
        else:
            ("Error, input a number between 1-5")
        
            
            
if __name__=='__main__':
    main()