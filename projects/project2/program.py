from datastructures.array2d import Array2D
from projects.project2.grid import Grid
from projects.project2.gameController import GameController


def main():
    file = "projects\\project2\\Testgrid.txt"
    grid = Grid(file)
    game_controller = GameController(grid)
    game_controller.run()

if __name__ == '__main__':
    main()