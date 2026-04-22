class Bank:
    owners = ""
    balance = 0
    def __init__(self,owners,balance):
        self.owners = owners
        self.balance = balance

    def Deposite(self, amount):
        self.balance += amount
        print(self.owners,"Deposited Successfully PKR:", amount, "| " "New Balance:", self.balance,"PKR")

    def Withdraw(self, amount):
        if self.balance >= amount:        
            self.balance -= amount
            print(self.owners,"Withdrawn Successfully PKR:", amount, "| " "New Balance:", self.balance,"PKR")
        else:
            print()


account1 = Bank("Fahad", 10000)     
account1.Deposite(5000)
account1.Withdraw(2000)
print()
account2 = Bank("Ali", 20000)
account2.Deposite(10000)  
account2.Withdraw(15000)