class Account:
    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.filepath = filepath
            balance = file.read()
            self.balance = float(balance)

    def withdraw(self, amount):
        self.balance -= float(amount)

    def submit(self, amount):
        self.balance += float(amount)

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))



class Checking(Account):
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


checking = Checking("balance.txt", 1)
checking.transfer(100)
print(checking.balance)
checking.commit()

# account= Account('balance.txt')
# account.withdraw(100)
# account.commit()
# account.submit(200)
# account.commit()
