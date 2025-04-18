from datastructures.array2d import Array2D
from projects.project2.Project2Temporary.grid import Grid
from projects.project2.Project2Temporary.gameController import GameController
import numpy as np
from numpy.typing import NDArray


def main():
    grid = Grid(3,4)
    controller = GameController(grid)
    controller.startSequence()


if __name__ == '__main__':
    main()
