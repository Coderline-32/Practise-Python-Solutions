class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount} acoount balance: {self.__balance}")
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew: {amount} account balance: {self.__balance}")
        else:
            print("Insufficient funds!")
    def check_balance(self):
        print(f"Your account balance: {self.__balance}")

name_query = input("Enter your first name: ")
b1 = BankAccount(name_query, 0)
while True:
   
    
    Query = input("'d' for deposit, 'w' for withdraw and 'b' for balance: ").lower()

    if Query == "d":
        deposit_amount = int(input("Enter amount you want to deposit: "))
        b1.deposit(deposit_amount)
    elif Query == "w":
        withdraw_amount = int(input("Enter amount you want to withdraw: "))
        b1.withdraw(withdraw_amount)
    elif Query == "b":
        b1.check_balance()
    else:
        print("Invalid input")