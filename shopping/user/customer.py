from shopping.user.user import User


class Customer(User):
    def __init__(self, joined_at=None, **kwargs):
        super(Customer, self).__init__(**kwargs)
        self.joined_at = joined_at

