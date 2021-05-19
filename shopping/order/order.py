from typing import Optional

from returns.maybe import Maybe, maybe

from shopping.user.wallet import Wallet


class Order:
    def __init__(self, total_value, discount=0):
        self.total_value = total_value
        self.discount = discount

    # Normally this is the checks that we normally do
    # def pay_order(self, wallet: Wallet) -> int:
    #     if wallet is not None:
    #         user_wallet = wallet
    #         if user_wallet is not None:
    #             user_wallet_total_funds = user_wallet.total_funds()
    #             if user_wallet_total_funds is not None and user_wallet_total_funds > 0:
    #                 if self.discount > 0:
    #                     discount = self.discount
    #                     self.total_value -= discount
    #                 else:
    #                     user_wallet_total_funds -= self.total_value
    #                 return user_wallet_total_funds

    def pay_order(self, wallet: Wallet) -> Maybe[int]:
        return Maybe.from_optional(wallet).bind_optional(
            lambda user_wallet_total_funds: wallet.total_funds(),
        ).bind_optional(
            lambda order_discount: self.apply_discount(discount=self.discount)
        ).bind_optional(
            lambda credit: self.total_value - wallet.total_funds() if wallet.total_funds() > 0 else None,
        )

    @maybe
    def apply_discount(self, discount: int) -> Optional[int]:
        if discount > 0:
            return discount - self.total_value
        return None
