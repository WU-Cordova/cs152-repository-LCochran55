from __future__ import annotations
from datastructures.array2d import Array2D
from projects.project2.cell import Cell
import copy
import random
from typing import List


class Grid:
    def __init__(self,file:str=None, rows: int=10,cols:int=10): #Sets initial parameters, if none are input then file is None and row and col are set to 10

        self.file:str = file 
        self.history: List[Grid] = []
        self.numGeneration = 0 #Keeps track of how many generations have passed

        #IF the user inputs a file, will populate the grid with the values found in the file
        if(self.file is not None):
            with open(self.file,'r') as openfile:
                self.rows = int(openfile.readline()) #First line in the file is the row #
                self.cols = int(openfile.readline()) #Second line in file is col #
                self.grid: Array2D[Cell] = Array2D.empty(self.rows,self.cols,data_type=Cell) #Sets grid to the amount of rows and cols inside the file
                self.tempGrid: Array2D[Cell] = Array2D.empty(self.rows,self.cols,data_type=Cell) #Sets the temporary array to the same values as the grid
                self.readFile(openfile) #calls the read file function to populate the grid according to the file
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
            """ Reads the user inputted file and populates the grid based on it """
            rowIndex = 0
            colIndex = 0

            for line in file:
                if(rowIndex >= self.rows): #makes sure the row index never exceeds bounds
                    rowIndex = 0
                for l in line.strip():
                    if(colIndex >= self.cols): #Makes sure col index never exceeds bounds
                        colIndex = 0
                    if l == "X":
                        self.grid[rowIndex][colIndex].is_alive = True
                    else:
                        self.grid[rowIndex][colIndex].is_alive = False
                    colIndex+=1
                rowIndex+=1


    def display(self) -> None:
        """ Displays the grid """

        print(f"━━《》Generation {self.numGeneration}《》━━")
        for row in range(self.rows):
            for col in range(self.cols): 
                print(f"  {self.grid[row][col]}",end=" ")
            print()
        print("━━《》━《》━《》━《》━━")
        print()
        self.numGeneration+=1


    def get_Neighbors(self,row:int,col:int) -> int:
        """ Counts the number of neighbors that are alive surrounding a cell, avoiding the position of the cell itself, and 
            cells that are out of bounds"""
        count = 0
        for r in range(row-1,row+2):
                for c in range(col-1,col+2):
                    if((r==row and c==col) or not(0<=r<self.rows and 0<=c<self.cols)):
                        continue
                    else:
                        if(self.grid[r][c].is_alive == True):
                            count+=1
        return count


    def declareLifeorDeath(self, row: int, col: int) -> None:
        """Loops through every cell in the grid, calulating the neighbors for each cell and deciding if it will die or live """
        #If the Cell at this point in the grid is alive it will enter and decide the correct state for the Cell to be in based on its neighbors
        if(self.grid[row][col].is_alive == True):
            if(self.get_Neighbors(row,col) == 2 or self.get_Neighbors(row,col) == 3):
                self.tempGrid[row][col].is_alive = True 
            else:
                self.tempGrid[row][col].is_alive = False
        #Same thing, but for if the cell is dead
        else:
            if(self.get_Neighbors(row,col) == 3):
                self.tempGrid[row][col].is_alive = True
            else:
                self.tempGrid[row][col].is_alive = False


    def copyTemptoMain(self) -> None:
        #Copies the updated temporary grid into the main grid
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c] = copy.deepcopy(self.tempGrid[r][c])


    def next_generation(self) -> Grid:
        
        self.history.append(copy.deepcopy(self.grid)) #Adds the grid to the history

        for r in range(self.rows):
            for c in range(self.cols): #loops through rows and cols
                self.declareLifeorDeath(r, c) #Decides if the current cell is alive or dead
        
        self.copyTemptoMain()
        return self.grid


    def checkHistory(self) -> bool:
        if(len(self.history) > 3): #Pops oldest grid if the history becomes larger than 3
            self.history.pop(0)
        if(len(self.history) > 2):
            currentArray = self.history[2] #Newest grid in history
            previousArray = self.history[1] #Second newest grid in history
            prevPreviousArray = self.history[0] #Oldest grid in history
            for r in range(self.rows):
                for c in range(self.cols):
                    if(not(currentArray[r][c] == previousArray[r][c]) and not(currentArray[r][c] == prevPreviousArray[r][c])):
                        return False #Will return false if grid history is unique
            return True
        else:
            return False

    def __eq__(self,value):
        if(isinstance(value,Grid)) and self.rows == value.rows and self.cols == value.cols:
            return self.grid == value.grid
        return False
    