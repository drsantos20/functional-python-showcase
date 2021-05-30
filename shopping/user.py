from dataclasses import dataclass
from typing import Optional

from shopping.address import Address


@dataclass
class User(object):
    address: Optional[Address]


