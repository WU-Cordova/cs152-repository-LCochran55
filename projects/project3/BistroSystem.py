
from projects.project3.drink import Drink

class bistroSystem:
    def __init__(self,) -> None:
        self.menu = ['Mocha','Latte', 'Tea', 'Matcha Latte', 'Lemonade']
        return

    def MenuStart(self)-> None:

        options = [1,2,3,4,5,6]

        print(f"Welcome to bearcat Bistro!")
        userChoice = int(input(f"1. Display Menu\n2. Take new order\n3. View Open Orders\n4. Mark Next Order as Complete\n5. View End of Day Report\n6. Log Out and Exit"))

        while userChoice not in options:
            print(f"Please select a valid choice")
            userChoice = int(input(f"1. Display Menu\n2. Take new order\n3. View Open Orders\n4. Mark Next Order as Complete\n5. View End of Day Report\n6. Log Out and Exit"))

        if(userChoice == 1):
            self.displayMenu()
        elif(userChoice==2):
            self.takeOrder()
        elif(userChoice==3):
            self.viewOrders()
        elif(userChoice==4):
            self.completeOrder()
        elif(userChoice==5):
            self.viewDayReport()
        else:
            self.exit()
    
    def displayMenu():
        pass

    def takeOrder():
        pass

    def viewOrders():
        pass
    

    