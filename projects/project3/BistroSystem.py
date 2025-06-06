
from projects.project3.drink import Drink
from projects.project3.CustomerOrder import CustomerOrder
from datastructures.bag import Bag
from datastructures.linkedlist import LinkedList

import datetime

class BistroSystem:
    def __init__(self) -> None:

        self.menu = {
            'Latte'.casefold()  : 1.20,
            'Mocha'.casefold()  : 1.25,
            'Tea'.casefold() : 1.00,
            'Matcha'.casefold() : 2.00, 
            'Lemonade'.casefold()  : 1.00
        }

        self.add_ons = {
            'Espresso shot'.casefold()  : 0.50,
            'Syrup'.casefold() : 0.25,
            'Alt. Milk'.casefold() : 0.50
        }

        #Stores the total amount of each drink made during a full day
        self.total_orders = Bag()
        self.total_add_ons = Bag()

        #Stores the total amount of sales made during a day
        self.total_sales = 0.00

        #Keeps track of currents unmade orders
        self.currentOrders = LinkedList(CustomerOrder)


    def MainMenu(self)-> None:
        """
        Opens up the options menu, and starts the bistro system
        Each option will return back to the menu after it is completed
        """

        options = [1,2,3,4,5,6]

        print(f"\nWelcome to bearcat Bistro!")
        userChoice = int(input(f"1. Display Menu\n2. Take new order\n3. View Open Orders\n4. Mark Next Order as Complete\n5. View End of Day Report\n6. Log Out and Exit\n\n"))

        while userChoice not in options:
            print(f"Please select a valid choice")
            userChoice = int(input(f"1. Display Menu\n2. Take new order\n3. View Open Orders\n4. Mark Next Order as Complete\n5. View End of Day Report\n6. Log Out and Exit\n\n"))

        if(userChoice == 1):
            self.displayMenu()
            self.MainMenu()
        elif(userChoice==2):
            self.takeOrder()
            self.MainMenu()
        elif(userChoice==3):
            self.viewOrders()
            self.MainMenu()
        elif(userChoice==4):
            self.completeOrder()
            self.MainMenu()
        elif(userChoice==5):
            self.viewDayReport()
            self.MainMenu()
        else:
            self.exit()



    def displayMenu(self) -> None:
        """
        Prints a text file containing the menu
        """
        #================== TEMP ===============================
        with open("projects\\project3\\menu.txt", 'r') as file:
                menuFile = file.read()
                print(menuFile)
        file.close()
        return

    def takeOrder(self) -> None:
        """
        Asks for users name, drink order, size, add ons, and any additional drinks.
        Calulates price and adds to total list of orders
        """

        totalPrice = 0

        drink_list = []
        price = 0.00

        customer = str(input(f"What is the name for the order?: "))

        #Confirms that the order is still being taken, so drinks can be added until the user no longer wants more drinks (When takingOrder == False)
        takingOrder = True

        while takingOrder == True:
            drinkChoice = str(input(f"\nDrink Choice?: ")).casefold()
            while drinkChoice not in self.menu:
                print(f"Item not on menu")
                drinkChoice = str(input(f"\nDrink Choice?: ")).casefold()
            price += self.menu.get(drinkChoice)
                
            drinkSize = str(input(f"\nSize? [s,m,l]: ")).casefold()
            while drinkSize  != "s".casefold() and drinkSize != "m".casefold()  and drinkSize  != "l".casefold() :
                print(f"Size not on menu")
                drinkSize = str(input(f"\nSize? [s,m,l]: ")).casefold()
            #Adds to price if user wants a bigger drink
            if drinkSize == 'm'.casefold() :
                price += .25
            elif drinkSize == 'l'.casefold() :
                price += 0.50
            
            add_on_list = []

            add = str(input(f"\nAny add-ons? [y or n]: ")).casefold()
            while add  != "y".casefold()  and add  != "n".casefold() :
                add = str(input(f"\nAny add-ons? [y or n]: ")).casefold()
            
            #Will ask the user for any add-ons they want until they input n 
            while add  == "y".casefold() :
                added = str(input(f"What would you like to add?: ")).casefold()
                while added not in self.add_ons:
                    print(f"Add on not on menu")
                    added = str(input(f"What would you like to add?: ")).casefold()
                
                #Appends each add on they want, so it can be read back later
                add_on_list.append(added)
                self.total_add_ons.add(added)

                price += self.add_ons.get(added.casefold())

                #Continues to ask the user for any add-ons they want until they input n 
                #Allows user to add more than 1 syrup, espresso, etc
                add = str(input(f"\nAny more add-ons? [y or n]: ")).casefold()
                while add  != "y".casefold()  and add  != "n".casefold() :
                    add = str(input(f"\nAny add-ons? [y or n]: ")).casefold()

            drink = Drink(type=drinkChoice,size=drinkSize,add_on=add_on_list,price=price)
            drink_list.append(drink)
    

            self.total_sales += price
            self.total_orders.add(drinkChoice)

            totalPrice += price
            price = 0.00

            #Allows user to add multiple drinks to one order
            print(f"\nYour current order is")
            for drink in drink_list:
                print(f"\n--{drink.type} ({drink.size}), {drink.add_on} ; {drink.price}")
                print(f"\nTotal price: {totalPrice}")
            additionalOrder = str(input("\nAdd additional item? [y or n]: ")).casefold()
            while additionalOrder != "y".casefold() and additionalOrder != "n".casefold():
                additionalOrder = str(input("\nAdd additional item? [y or n]: ")).casefold()
            if additionalOrder == "n".casefold():
                takingOrder = False  


        customerOrder = CustomerOrder(name=customer,order=drink_list)
        self.currentOrders.append(customerOrder)


    def viewOrders(self) -> None:
        """
        Prints out the current Linked List of unfullfilled orders
        """
        totalPrice = 0
        print(f"CURRENT UNFULFILLED ORDERS\n===============")
        for order in self.currentOrders:
            print(f"{order.name}'s order")
            for drink in order.order:
                totalPrice += drink.price
                print(f"--{drink.type} ({drink.size}), {drink.add_on} ; {drink.price}")
            print(f"Total price: {totalPrice}")

        print(f"===============")

    def completeOrder(self) -> None:
        """
        Asks for the customer whos order is done, and removes their order from the Linked List of total orders
        """
        completed_order = str(input("Enter customer's name to complete: ")).casefold()

        for order in self.currentOrders:
            name = order.name
            if completed_order == name.casefold():
                self.currentOrders.remove(order)
                print(f"{name}'s order is completed!")
                return
            
        print("Order not in list")

    def viewDayReport(self) -> None:
        """
        Adds the date, what drinks were made, what add ons were used, and total sales of the day to a text file to print
        """

        current_time = datetime.datetime.now()
        year = current_time.year
        month = current_time.month
        day = current_time.day

        current_day = f"{month}/{day}/{year}"

        historyFile = "projects\\project3\\OrderHistory.txt"

        with open(historyFile,'r+') as file:
            # file.seek(0)
            # date = file.readline().rstrip()
            # if date != current_day:
            #     lines = file.readlines() # read old content
            #     file.seek(0) # go back to the beginning of the file
            #     file.write(f"{current_day}\n=============================\nDRINKS ORDERS:{str(self.total_orders)}\nADD-ONS USED:{str(self.total_add_ons)}\nTOTAL SALES: {self.total_sales}\n") # write new content at the beginning
            #     file.write(date)
            #     file.write("\n")
            #     for line in lines: # write old content after new
            #         file.write(line)
            #     file.close
            # else:
            file.seek(0)
            file.truncate()
            file.write(f"{current_day}\n=============================\nDRINKS ORDERS:{str(self.total_orders)}\nADD-ONS USED:{str(self.total_add_ons)}\nTOTAL SALES: {self.total_sales}\n") # write new content at the beginning
            file.close
        
        with open(historyFile,'r') as openfile:
            report = openfile.read()
            print(report)

    def exit(self) -> None:
        """
        Ends the program
        """
        exit = str(input("Log out? [y/n]:")).casefold()
        while exit  != "y".casefold()  and exit != "n".casefold() :
            exit = str(input("Log out? [y/n]: ")).casefold()
        if exit == "y".casefold():
            print("Logging out...")
            exit
        else:
            self.MainMenu()



    

    