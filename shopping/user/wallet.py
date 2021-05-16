

class Wallet:
    def __init__(self, customer, funds):
        self.customer = customer()
        self.funds = funds

    def total_funds(self) -> int:
        return self.funds
