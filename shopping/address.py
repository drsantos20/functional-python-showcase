from dataclasses import dataclass
from typing import Optional

from returns.maybe import Maybe


@dataclass
class Address(object):
    street: Optional[str]


def get_street_address(order: 'shopping.order.Order') -> Maybe[str]:
    return Maybe.from_optional(order.user).bind_optional(
        lambda user: user.address
    ).bind_optional(
        lambda address: address.street,
    )


# without functional way
def get_address(order: 'shopping.order.Order'):
    if order.user is not None:
        user = order.user
        if user.address is not None:
            address = user.address
            if address.street is not None:
                street = address.street
                return street
