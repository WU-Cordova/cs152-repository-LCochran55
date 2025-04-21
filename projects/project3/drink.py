from dataclasses import dataclass
from datastructures.bag import Bag
from typing import Optional


@dataclass
class Drink:
    type: str
    size: str
    add_on: list[str]
    price: float
