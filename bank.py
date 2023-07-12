
class bankaccount:
    def __init__(self) -> None:
        self.zelle=""
        self.balance=0
        self.registered_accounts={self.zelle:self.balance}
    def create_account(self):
        zelle_ID=input("please input your zelle ID, it must be 5 letters long and lowercase?")
        if len(zelle_ID)!=5:
            print("zelle_ID length not reached, make sure it is 5 letters long and lower case")
        elif zelle_ID!=zelle_ID.lower():
            print("zelle ID must be lowercase")
        elif zelle_ID in self.registered_accounts:
            print("Zelle ID currently in use, select another")
        else:
            starting_sum=float(input("Deposit a starting sum?"))
            self.registered_accounts[zelle_ID]=starting_sum
            print("Account succefully created")
    
    def view_balance(self):
        zelle=input("what is your zelle ID?")
        if zelle in self.registered_accounts:
            print("your balance is ${}".format(self.registered_accounts[zelle]))
        else:
            print("You don't have an account with use, please create one and deposit somne money")
        
    def deposit(self,amount):
        zelle=input("what is your zelle ID?")
        if amount>=1:
            self.registered_accounts[zelle]+=amount
            print("${} added to your account".format(amount))
            
    def withdraw(self,amount):
        zelle=input("What is your zelle ID?")
        if self.registered_accounts[zelle]>=amount:
            self.registered_accounts[zelle]-=amount
            print("${} deducted from your account balance".format(amount))
        else:
            print("insufficient balance")
    
    def transfer(self,amount):
        zelle=input("What is your zelle?")
        recipient=input("What is the recipient's zelle?")
        if self.registered_accounts[zelle]>=amount:
            self.registered_accounts[recipient]+=amount
            self.registered_accounts[zelle]-=amount
            print("you transfered ${} to {}".format(amount,recipient))
            
        
        
        
