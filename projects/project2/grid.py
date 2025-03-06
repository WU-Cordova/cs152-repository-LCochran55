from __future__ import annotations
from datastructures.array2d import Array2D
from projects.project2.cell import Cell
import copy
import random
from typing import List


class Grid:
    def __init__(self,file=None, rows: int=10,cols:int=10):

        self.file = file
        self.history: List[Grid] = []

        #IF the user inputs a file, will populate the grid with the values found in the file
        if(self.file is not None):
            with open(self.file,'r') as openfile:
                self.rows = int(openfile.readline())
                self.cols = int(openfile.readline())
                self.grid: Array2D[Cell] = Array2D.empty(self.rows,self.cols,data_type=Cell)
                self.tempGrid: Array2D[Cell] = Array2D.empty(self.rows,self.cols,data_type=Cell)
                self.readFile(openfile)
                return
        else:  
            self.grid: Array2D[Cell] = Array2D.empty(rows,cols,data_type=Cell)
            self.rows = rows
            self.cols = cols
            #Temporary grid used to store generations
            self.tempGrid: Array2D[Cell] = Array2D.empty(rows,cols,data_type=Cell)
            #Populates the Array2D with randomly selected dead or alive cells
            for row in range(self.rows):
                for col in range(self.cols):
                    self.grid[row][col].is_alive = random.choice([True,False])


    def columns(self) -> int:
        return self.cols
    
    def rows(self) -> int:
        return self.rows

    def readFile(self,file: str) -> None:
            rowIndex = 0
            colIndex = 0

            for line in file:
                if(rowIndex >= self.rows):
                    rowIndex = 0
                for l in line.strip():
                    if(colIndex >= self.cols):
                        colIndex = 0
                    if l == "X":
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
        print("━━《》━《》━《》━━")
        print()
        num+=1


    def get_Neighbors(self,row:int,col:int) -> int:
        count = 0
        for r in range(row-1,row+2):
                for c in range(col-1,col+2):

                    if((r==row and c==col) or not(0<=r<self.rows and 0<=c<self.cols)):
                        continue
                    else:
                            # print(f"row-1: {row-1} row {row} row+1: {row+1}\ncol-1: {col-1} col {col} row+1: {col+1}\nself.grid[r][c] {self.grid[r][c]}")
                        if(self.grid[r][c].is_alive == True):
                            count+=1
                        # print(f"{count} r: {r} c: {c} grid[r][c] = {self.grid[r][c]}")
        return count


    def declareLifeorDeath(self, row: int, col: int) -> None:
        print(f"r {row} c {col}")
        print(f"GRID ALIVE: {self.grid[row][col].is_alive == True} NUM NEIGHBORS: {self.get_Neighbors(row,col)}")
        if(self.grid[row][col].is_alive == True):
            if(self.get_Neighbors(row,col) == 2 or self.get_Neighbors(row,col) == 3):
                self.tempGrid[row][col].is_alive = True 
            else:
                self.tempGrid[row][col].is_alive = False
        else:
            if(self.get_Neighbors(row,col) == 3):
                self.tempGrid[row][col].is_alive = True
            else:
                self.tempGrid[row][col].is_alive = False


    def copyTemptoMain(self) -> None:
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c] = copy.deepcopy((self.tempGrid[r][c]))


    def next_generation(self) -> Grid:
        for r in range(self.rows):
            for c in range(self.cols):
                self.declareLifeorDeath(r, c)
                # print(f"r {r} c {c}")
        
        self.history.append(self.grid)
        print(f"HISTORY: {self.history}")
        self.copyTemptoMain()
        return self.grid


    def checkHistory(self) -> None:
        pass

    def __eq__(self,value):
        if(isinstance(value,Grid)) and self.rows == value.rows and self.cols == value.cols:
            return self.grid == value.grid
        return False
    