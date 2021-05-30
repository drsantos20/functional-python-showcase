from dataclasses import dataclass
from typing import Optional

from shopping.user import User


@dataclass
class Order(object):
    user: Optional[User]
