

1) Data structure choices for each component (Menu, Customer Order, Order Confirmation, Open Orders Queue, Completed Orders), and justifications for your choices. Your justifications should include complexity analysis and trade-offs.

    Menu:
    for the menu I chose a dictioary because I believed it would be an efficent way to store an item's name and price in one. 
    The complexity for grabbing the item's name/price would then be linear, so it would not be complex to do things such as compare
    a user's input to the keys in the dictionary, or update the price to the value of ths key.
    Displaying the menu, I chose to display a text file so I can make it look fancier without using a bunch of print statements. 

    CustomerOrder:
    My customer order is a dataclass that contains a string for the cutomers name, and a list which contains drinks. 
    Having a list with drinks allows for a cutomer's order to contain multiple drinks in one order, which makes it easier
    to repeat back the customer's total order. A trade off for this, is that it does not look very nice when printing out. I would implement some
    sort of str function to make it look nicer.

    Order Confirmation:
    My "takeOrder" function uses both the CustomerOrder class and the Drink class to create a customer's order. I use user input to grab the customers name, drink, size, and add-ons. I make sure that the customer is only able to input items that are on the menu. I also 
    allow the user to continously adding as many add-ons as they like using a while loop. This is all encapsulated inside a while loop which the user can leave once they are done with their drink order by inputting y or n, each time the user orders a new drink it is added to a list inside a function.
    After the user is done ordering the list and the customers name is then added to a customerOrder, which is then appened to the linkedlist of all current customer orders.
    An additional implmentation, I created a variable for the total sales and total drinks/add-ons used during the day, which are saved in a TXT file when checking the day report. 
    The variable for total drinks and add_ons are bags, so when a customer orders a drink/add on the value of the key increases. This allows for easy printing so that there is not a long list of repeating items and only up to 4 items with values that indicate how many times they have been ordered.
    I believe all my functions in this are o(1).

    Open Order Queue/completed orders;
    For this I originally considered a circular queue, since this is what my mind thinks of when taking orders, however I did not want to set a max size for the queue, and allow the user/barista to complete orders as they like.
    So, I implemeted a complete order function which allows the user to look through the current orders and remove the order they have completed. 
    The limitation of this, is that when two orders have the same name the order that came first will always be removed.
    This should be an o(1) time complexity.


2) Instructions to run the program.
    To start, simply choose which option you would like to use from the main menu.
    Option one displays the menu
    Option 2 allows the user to take a customers order. Input the customers name, drink, size, add-ons, and additional drinks with each prompt
    Option 3 prints out the current unfulfilled orders
    Option 4 allows the user to fulfill an order by entering the name of the completed order when prompted
    Option 5 reports the days total drinks, add-ons used, and sales.
    Option 6 allows the user to log out and quit the program.


3) Sample run(s) as screenshot(s) or pasted output.



4) Any known bugs or limitations.
    The end of day report does not keep track of history past the current session. 




5) What you’d add next if you had more time.
    If I had more time, Id like to have made a log in function that accepts a password to log in. Additionally, my end of day report was supposed to keep track of history for past days/past sessions, however the report does not. With more time I would like to improve this
