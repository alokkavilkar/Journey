# Bank Account Management System:

# Design a Python class for a bank account with methods to deposit, withdraw, and check balance.
# Implement inheritance to create specialized account types such as SavingsAccount and CurrentAccount with additional features like interest calculation or overdraft protection.


class BOMACCOUNT:

    @staticmethod
    def format_currency(amount):
        float(amount)
        return f"${amount:,.2f}"

    def __init__(self, bankname, branch, code, minimum_balance) -> None:
        self.bankName = bankname
        self.branch = branch
        self.code = code
        self.balance = minimum_balance

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            print(f'{self.balance} after adding {amount}')
        else:
            print(f'{amount} is not valid, current balance : {self.balance}')

    def with_draw(self, amount):

        if self.balance < amount:
            print(f'{amount} is not valid, please review the amount because current balance is {self.balance}')

        else:
            self.balance -= amount
            print(f"{amount} deducted from the account, balance : {self.balance}")


    def display_details(self):
        print(f"Bank : {self.bankName} Branch: {self.branch} balance: {BOMACCOUNT.format_currency(self.balance)}")


        
class SavingAccount(BOMACCOUNT):

    __interest_rate = 0.05

    @staticmethod
    def calculate_interest(balance, interest_rate):
        return balance * interest_rate
    
    def __init__(self, bankname, branch, code, minimum_balance) -> None:
        super().__init__(bankname, branch, code, minimum_balance)

        print(f"{self.bankName} is ready with your saving account")
        

    def deposit(self, amount):
        self.add_interest()
        return super().deposit(amount)

    def add_interest(self):
        interest_amount = self.calculate_interest(self.get_balance(), SavingAccount.__interest_rate)
        self.balance += interest_amount
        print(f"Interest of {self.format_currency(interest_amount)} added, New balance is {self.format_currency(self.balance)}")





myaccount = SavingAccount("BOM", "PANVEL", "#9012", 4000)
myaccount.deposit(5000)
myaccount.display_details()