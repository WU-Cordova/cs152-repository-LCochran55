from dataclasses import dataclass
from datastructures.bag import Bag
from typing import Optional


@dataclass
class Drink:
    name: Optional[str] = None
    size: Optional[str] = None
    add_on: Optional[Bag] = None
    price: Optional[float] = None
