class BankAccount:

    def __init__(self, accNo, balance, accountHolderName: str) -> None:
        self.accno = accNo
        self.balance = balance
        self.accountHolderName = accountHolderName

    def deposit(self, amount) -> str:
        if isinstance(amount, int):
            self.balance += amount
            return f"{amount} is deposited within account {self.accno} from {self.accountHolderName} and balance is {self.balance}"
        else:
            return f"Please provide valid cash method."
        
    def withdraw(self, amount) -> str:
        if amount > self.balance :
            return f"{amount} withdraw unsucessfull as balance of {self.balance} present"
        else:
            self.balance -= amount
            return f'{amount} is withdrawed sucessfully, remaining balance is {self.balance}'
        

    def print_info(self):
        return f'{self.accountHolderName} : {self.accno} balance : {self.balance}'
        
    @staticmethod
    def interest(account):
        if account.balance > 1000:
            account.balance += 600
            return account.print_info()
        

alok = BankAccount('201728102912', 10000, 'Alok')
# receipt = alok.deposit(1000)
# print(receipt)
# withdraw_recipt = alok.withdraw(100)
# print(withdraw_recipt)
print(BankAccount.interest(alok))