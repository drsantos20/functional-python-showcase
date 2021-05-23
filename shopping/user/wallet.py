from shopping.user.user import User


class Wallet(User):
    def __init__(self, funds=None, **kwargs):
        super(Wallet, self).__init__(**kwargs)
        self.funds = funds

    def add_funds(self, amount):
        if amount > 0:
            self.funds += amount

    def total_funds(self):
        return self.funds
