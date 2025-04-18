from projects.project3.drink import Drink
from datastructures.bag import Bag

class orderItem:
    def __init__(self, drink: Drink) -> None:
        self.drink = Drink()
        self.menu = ['Mocha','Latte', 'Tea', 'Matcha Latte', 'Lemonade']

    def orderDrink(self) -> Drink:
        drinkChoice = str(input(f"Drink Choice?: "))
        while drinkChoice not in self.menu:
            print(f"Item not on menu")
            drinkChoice = str(input(f"Drink Choice?: "))
        size = str(input(f"Size? [s,m,l]:"))
        while size != "s" or size != "m" or size != "l":
            print(f"Size not on menu")
            drinkChoice = str(input(f"Size? [s,m,l]: "))
        
    
    def _str_(self) -> str:
        return f'Drink: {self.drink.name}, Size: {self.drink.size}, Add-ons: {self.drink.add_on}, Price: {self.drink.price}'