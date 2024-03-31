class BankAccount():
    def __init__(self, number, balance, date, name):
        self.number = number
        self.balance = balance
        self.date = date
        self.name = name

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def check_balance(self):
        return self.balance



def main():
    account = BankAccount(123456, 1000000, "12/12/2020", "Nguyen Van A")
    account.withdraw(100000)
    account.deposit(500000)
    print(account.check_balance())
    print(account.name)


if __name__ == "__main__":
    main()
