from datastructures.array2d import Array2D
from projects.project2.kbhit import KBHit
from projects.project2.Project2Temporary.grid import Grid
from time import sleep
import time

class GameController():

    def __init__(self, grid:Grid) -> None:
        self.__grid = grid

    def generateOnce(self) -> None:
        # self.__grid.populate()
        for i in range(self.__grid.rowLength()):
            for j in range(self.__grid.colLength()):
                self.__grid.getNeighbors(i,j)
                self.__grid.declareLifeorDeath(i, j)
                print(f"i {i} j {j}")

        self.__grid.copyTemptoMain()
        self.__grid.display()


    def startSequence(self) -> None:
        print(f"\n _____                  _____ ___\n|   __|___ _____ ___   |     |  _|\n|  |  | .'|     | -_|  |  |  |  _|\n|_____|__,|_|_|_|___|  |_____|_|\n         __    _ ___\n        |  |  |_|  _|___\n        |  |__| |  _| -_|\n        |_____|_|_| |___|\n\n           GAME MODES\n1) Automatic mode; Runs all on its own!\n2) Manual Mode; Allows for user paced generation!")
        
        mode = int(input("To play please enter a mode! [1][2]: "))
        while(mode != 1 and mode!= 2):
            print("Oops! Thats not a real mode!")
            mode = int(input("To play please enter a mode! [1][2]: "))
        if mode == 1:
            for i in range(5):
                self.generateOnce()
        else:
            pass
            # print("To step through each iteration press key 's'! To exit, press q")

            # kb = KBHit()
            # while True():
            #     self.generateOnce()
            #     time.sleep(1)
            #     key = kb.getch()
                
            #     if key == 'q':
            #         print("Quit!")
            #         break