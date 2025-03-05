
import random as radm 
from datastructures.array2d import Array2D
from datastructures.array import Array
import copy
import numpy as np
from numpy.typing import NDArray


class Grid():

    def __init__(self, row_len:int, col_len: int, file:str=None) -> None:
        self.__row_len = row_len
        self.__col_len = col_len
        self.__array2d = Array2D.empty(rows=row_len, cols=col_len,data_type=int)
        self.__tempArray = Array2D.empty(rows=row_len, cols=col_len,data_type=int)
        self.__history = []
        self.__file = file

    def colLength(self) -> int:
        return self.__col_len
    
    def rowLength(self) -> int:
        return self.__row_len

    def populate(self) -> None:
        if(self.__file is not None):
            self.readFile(self.__file)
        else:   
            numBacteria = radm.randint(1,self.__row_len*self.__col_len)

            rowList = (i for i in range(self.__row_len-1))
            colList = (i for i in range(self.__col_len-1))

            while numBacteria!= 0:
                rowIndex = radm.choice(rowList)
                colIndex = radm.choice(colList)

                self.__array2d[rowIndex][colIndex] = 1
                rowList.pop(rowIndex)
                colList.pop(colIndex)
            

    def readFile(self,file: str) -> None:
            openFile = open(file, "r")
            row = openFile.readline()
            col = openFile.readline()
            rowIndex = 0
            colIndex = 0
            for line in openFile.readlines():
                for l in line:
                    if l.equals("X"):
                        self.__array2d[rowIndex][colIndex] = 1
                    else:
                        self.__array2d[rowIndex][colIndex] = 0
                    colIndex+=1
                rowIndex+=1

    def getNeighbors(self, row: int, col: int) -> int:
        count = 0
        for i in range(row-1,row+1):
            if(i<self.__row_len and i>=0):
                for j in range(col-1,col+1):
                    if(j<self.__col_len and j>=0):
                            print(f"GetNeighbors i [{i}] j [{j}] array2d[i][j] {self.__array2d[i][j]}")
                            if(self.__array2d[i][j] == 1):
                                count+=1
        return count

    def declareLifeorDeath(self, row: int, col: int) -> None:
        if(self.__array2d[row][col]==1):
            if(self.getNeighbors(row,col)>=2):
                self.__tempArray[row][col] = 0
            else:
                self.__tempArray[row][col] = 0
        else:
            if(self.getNeighbors(row,col)>= 3):
                self.__tempArray[row][col] = 1
            else:
                self.__tempArray[row][col] = 0

    def copyTemptoMain(self) -> None:
        for r in self.__array2d:
            for c in r:
                self.__array2d[r][c] = copy.deepcopy((self.__tempArray[r][c]))

        self.__history.append(copy(self.__tempArray))
        for r in range(self.__row_len):
            self.__tempArray[r].clear()

    def display(self) -> None:
        for r in self.__array2d:
            for c in r:
                print(f"||{self.__array2d[r][c]}||")
            print()

    def checkHistory(self) -> None:
        pass

            


                
                
        
