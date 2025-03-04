from __future__ import annotations
from datastructures.array2d import Array2D
from projects.project2.cell import Cell
import copy
import random


class Grid:
    def __init__(self, rows: int=10,cols:int=10, file:str=None):

        self.file = file

        self.history = []

        #IF the user inputs a file, will populate the grid with the values found in the file
        if(self.file != None):
            openFile = open(file, "r")
            self.rows = openFile.readline()
            self.cols = openFile.readline()
            self.readFile(self.file)

        else:  
            self.grid: Array2D = Array2D.empty(rows,cols,data_type=Cell)

            self.rows = rows
            self.cols = cols

            #Temporary grid used to store generations
            self.tempGrid: Array2D = Array2D.empty(rows,cols,data_type=Cell)

            #Populates the Array2D with randomly selected dead or alive cells
            for row in range(self.rows):
                for col in range(self.cols):
                    self.grid[row][col].is_alive = random.choice([True,False])


    def columns(self) -> int:
        return self.cols
    
    def rows(self) -> int:
        return self.rows


    def readFile(self,file: str) -> None:
            openFile = open(file, "r")

            rowIndex = 0
            colIndex = 0
            for line in openFile.readlines():
                for l in line:
                    if l.equals("X"):
                        self.grid[rowIndex][colIndex].is_alive = True
                    else:
                        self.grid[rowIndex][colIndex].is_alive = False
                    colIndex+=1
                rowIndex+=1


    def display(self) -> None:
        num = 0
        print(f"━━《》Generation {num}《》━━")
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col],end=" ")
            print()
        num+=1
        print("━━《》━《》━《》━━")
        print()



    def get_Neighbors(self,row:int,col:int) -> int:
        count = 0
        for i in range(row-1,row+1):
            if(i<self.rows and i>=0):
                for j in range(col-1,col+1):
                    if(j<self.cols and j>=0):
                            # print(f"GetNeighbors i [{i}] j [{j}] array2d[i][j] {self.grid[i][j]}")
                            if(self.grid[i][j].is_alive == True):
                                count+=1
        return count


    def declareLifeorDeath(self, row: int, col: int) -> None:
        if(self.grid[row][col].is_alive == True):
            if(self.get_Neighbors(row,col)>=2):
                self.tempGrid[row][col].is_alive = True
            else:
                self.tempGrid[row][col].is_alive = False
        else:
            if(self.get_Neighbors(row,col)>= 3):
                self.tempGrid[row][col].is_alive = True
            else:
                self.tempGrid[row][col].is_alive = False


    def copyTemptoMain(self) -> None:
        self.history.append(copy.copy(self.grid))
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c] = copy.deepcopy((self.tempGrid[r][c]))

        # print(f"HISTORY: {self.history}")


    def next_generation(self) -> Grid:


        for r in range(self.rows):
            for c in range(self.cols):
                self.declareLifeorDeath(r, c)

        self.copyTemptoMain()
        return self.grid


    def checkHistory(self) -> None:
        pass

    def __eq__(self,value):
        if(isinstance(value,Grid)) and self.rows == value.rows and self.cols == value.cols:
            return self.grid == value.grid
        return False
    