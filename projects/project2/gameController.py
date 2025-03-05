from time import sleep
from projects.project2.grid import Grid
from projects.project2.kbhit import KBHit

class GameController:
    def __init__(self,grid:Grid):
        self.grid = grid

    def run(self):
        self.grid.display()

        print("Press q to quit")

        kbhit = KBHit()

        while True:
            sleep(1)
            if kbhit.kbhit():
                key = kbhit.getch()

                if key == 'q':
                    print("Quitting now.")
                    return
            self.grid.next_generation()
            self.grid.display()