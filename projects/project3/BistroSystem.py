
from projects.project3.drink import Drink
from projects.project3.CustomerOrder import CustomerOrder
from datastructures.bag import Bag
from datastructures.linkedlist import LinkedList

import datetime

class BistroSystem:
    def __init__(self) -> None:

        self.menu = {
            'Latte' : 1.20,
            'Mocha' : 1.25,
            'Tea': 1.00,
            'Matcha': 2.00, 
            'Lemonade' : 1.00
        }

        self.add_ons = {
            'Espresso shot' : .50,
            'Syrup': .25,
            'Milk Alternative': .50
        }

        #Saves the date to input into the history file for saving end of day report
        current_time = datetime.datetime.now()
        year = current_time.year
        month = current_time.month
        day = current_time.day

        self.historyFile = "projects\\project3\\OrderHistory.txt"

        with open(self.historyFile,'a') as openfile:
                openfile.write(f"{month}/{day}/{year}\n=============================")
        openfile.close()

        #Stores the total amount of each drink made during a full day
        self.total_orders = Bag()

        #Stores the total amount of sales made during a day
        self.total_sales = 0.00

        #Keeps track of currents unmade orders
        self.currentOrders = LinkedList(CustomerOrder)

        #Stores past orders once they are made
        self.history = LinkedList(CustomerOrder)

    def MainMenu(self)-> None:
        #Opens up the options menu, and starts he bistro system

        options = [1,2,3,4,5,6]

        print(f"Welcome to bearcat Bistro!")
        userChoice = int(input(f"1. Display Menu\n2. Take new order\n3. View Open Orders\n4. Mark Next Order as Complete\n5. View End of Day Report\n6. Log Out and Exit\n"))

        while userChoice not in options:
            print(f"Please select a valid choice")
            userChoice = int(input(f"1. Display Menu\n2. Take new order\n3. View Open Orders\n4. Mark Next Order as Complete\n5. View End of Day Report\n6. Log Out and Exit\n"))

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
    
    def displayMenu(self):
        #Displays the menu
        #================== TEMP ===============================
        with open("projects\\project3\\menu.txt", 'r') as file:
                menuFile = file.read()
                print(menuFile)
        file.close()
        return
        
    def takeOrder(self) -> CustomerOrder:
        #Takes the users order, adding as many drinks as they select

        drink_list = []
        price = 0.00

        customer = str(input(f"What is the name for the order?: "))

        #Confirms that the order is still being taken, so drinks can be added until the user no longer wants more drinks (When takingOrder == False)
        takingOrder = True

        while takingOrder == True:
            drinkChoice = str(input(f"Drink Choice?: "))
            while drinkChoice not in self.menu:
                print(f"Item not on menu")
                drinkChoice = str(input(f"Drink Choice?: "))
            price += self.menu.get(drinkChoice)
                
            drinkSize = str(input(f"Size? [s,m,l]: "))
            while drinkSize != "s" and drinkSize != "m" and drinkSize != "l":
                print(f"Size not on menu")
                drinkChoice = str(input(f"Size? [s,m,l]: "))
            #Adds to price if user wants a bigger drink
            if drinkSize == 'm':
                price += .25
            elif drinkSize == 'l':
                price += 50
            
            add_on_list = []

            add = str(input(f"Any add-ons? [y or n]: "))
            while add != "y" and add != "n":
                add = str(input(f"Any add-ons? [y or n]: "))
            
            #Will ask the user for any add-ons they want until they input n 
            while add == "y":
                added = str(input(f"What would you like to add?: "))
                while added not in self.add_ons:
                    print(f"Add on not on menu")
                    added = str(input(f"What would you like to add?: "))
                
                #Appends each add on they want, so it can be read back later
                add_on_list.append(added)

                price += self.add_ons.get(added)

                #Continues to ask the user for any add-ons they want until they input n 
                #Allows user to add more than 1 syrup, espresso, etc
                add = str(input(f"Any more add-ons? [y or n]:"))
                while add != "y" and add != "n":
                    add = str(input(f"Any add-ons? [y or n]:"))

            drink = Drink(type=drinkChoice,size=drinkSize,add_on=add_on_list,price=price)
            drink_list.append(drink)

            self.total_sales += price
            self.total_orders.add(drinkChoice)
            print(self.total_orders)

            price = 0.00

            #Allows user to add multiple drinks to one order
            additionalOrder = str(input("Add additional item? [y or n]: "))
            while add != "y" and add != "n":
                additionalOrder = str(input("Add additional item? [y or n]: "))
            if additionalOrder == "n":
                takingOrder = False  

        customerOrder = CustomerOrder(name=customer,order=drink_list)

        self.currentOrders.append(customerOrder)

    def viewOrders(self):
        pass

    def completeOrder(self):
        self.history.append(self.currentOrders.pop_front())

    def viewDayReport(self):
        with open(self.historyFile,'a') as openfile:
                openfile.write(f"{str(self.total_orders)}")
        openfile.close()



    def exit(self):
        pass

    

    