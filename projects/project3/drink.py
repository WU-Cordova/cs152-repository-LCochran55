from dataclasses import dataclass
from datastructures.bag import Bag
from enum import Enum

@dataclass
class Drink:
    name: str
    size: str
    add_on: Bag
    price: float
