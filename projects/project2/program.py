from datastructures.array2d import Array2D
from projects.project2.grid import Grid
from projects.project2.gameController import GameController

def main():
    file = open("Testgrid.txt", "r")
    grid = Grid(file)
    print("ABCD")
    game_controller = GameController(grid)
    game_controller.run()

if __name__ == '__main__':
    main()