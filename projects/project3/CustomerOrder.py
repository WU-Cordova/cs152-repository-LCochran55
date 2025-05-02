
from dataclasses import dataclass
from projects.project3.drink import Drink


@dataclass
class CustomerOrder:
    name: str
    order: list[Drink]
