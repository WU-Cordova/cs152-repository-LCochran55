from time import sleep
from projects.project2.grid import Grid
from projects.project2.kbhit import KBHit
from time import sleep
import time

class GameController:
    def __init__(self,grid:Grid):
        self.grid = grid

    def run(self):
        #Decorative header
        print(f"\n _____                  _____ ___\n|   __|___ _____ ___   |     |  _|\n|  |  | .'|     | -_|  |  |  |  _|\n|_____|__,|_|_|_|___|  |_____|_|\n         __    _ ___\n        |  |  |_|  _|___\n        |  |__| |  _| -_|\n        |_____|_|_| |___|\n\n           GAME MODES\n1) Automatic mode; Runs all on its own!\n2) Manual Mode; Allows for user paced generation!")
        
        #Deciding game mode the player wants to play
        mode = int(input("To play please enter a mode! [1][2]: "))
        #Repeats until player inputs a correct gamemode
        while(mode != 1 and mode!= 2):
            print("Oops! Thats not a real mode!")
            mode = int(input("To play please enter a mode! [1][2]: "))

        kb = KBHit()

        #Automatic mode
        if mode == 1:
            self.grid.display()
            while(self.grid.checkHistory() == False):
                time.sleep(1)
                self.grid.next_generation() #Generates next generation
                self.grid.display() #Displays the grid
            print("Pattern is repeating. To generate once more press any key, if not, press q to quit")
            key = kb.getch()

            while key is not 'q': #Runs until q is entered, allowing users to continue generation if they want
                self.grid.next_generation()
                self.grid.display()
                time.sleep(1)
                key = kb.getch()
        
            print("Quitting!")
            return
            
        #manual mode
        else:
            print("To step through each iteration press any key! To exit, press q")
            self.grid.display() #Displays initial grid

            while True:
                self.grid.next_generation()
                self.grid.display()
                key = kb.getch()
                    
                if key == 'q':
                    print("Quitting!")
                    break