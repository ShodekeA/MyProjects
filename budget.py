class Category():
    def __init__(self, name):
        self.name = name
        self.total_bal = 0.0

    def __repr__(self):
        return f"The remaining balance on {self.name} is : {self.total_bal}"

    def deposit(self, dep_amnt):
        self.total_bal += dep_amnt
        return self.total_bal

    def withdrawal(self, withdraw_amnt):
        self.total_bal -= withdraw_amnt
        return self.total_bal

    def getBalance(self):
        return self.total_bal

    def transfer(self, amount, budget_group):
        #if self.name != budget_group.name:
        self.withdrawal(amount)
        budget_group.deposit(amount)


def test_category():
    testbudget = Category(100)
    assert testbudget.total_bal == 100