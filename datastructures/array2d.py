from __future__ import annotations
import os
from typing import Iterator, List, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int) -> None:
        # We are going to need the data type for items so we need to add a constructor
        # parameter for `data_type`.

            self.row_index: int = row_index
            self.array: IArray = array
            self.num_columns: int = num_columns

            self.data_type = type(self.array[0])
            

        def map_index(self, row_index: int, column_index: int) -> int:
            return row_index*self.num_columns+column_index

        def __getitem__(self, column_index: int) -> T:
            # This is the second bracket operator. At this point you have row and column!
            # 1. ⛈️ If out of bounds, raise an IndexError
            # 2. ⛈️ Translate the `row_index` and `column_index` into a 1D `index`
            # 3. Return array[index]

            index: int =  self.map_index(self.row_index, column_index)

            if column_index >= self.num_columns:
                raise IndexError
            
            return self.array[index]

            # raise NotImplementedError('Row.__getitem__ not implemented.')
        
        def __setitem__(self, column_index: int, value: T) -> None:
            #This is the second bracket operator. At this point you have row and column!
            # 1. ⛈️ If out of bounds, raise an IndexError
            # 2. ⛈️ If `value` is not an instance of the right type, raise a TypeError.
            # 3. Convert the `row_index` and `column_index` into a 1D `index`
            # 4. Set array[index] = value  

            if column_index >= self.num_columns:
                raise IndexError
            
            # if not isinstance(type(value),self.__data_type):
            #     raise TypeError
            
            py_list = []
            for row in (self.array[column_index]):
                py_list.append(row)
            py_list
        

            


        def __iter__(self) -> Iterator[T]:
            # This is your forward iterator for column data!
            # 1. Loop row_index from 0 to `num_rows`
        	# 	and yield self[row_index] ⬅ uses Array2D __getitem__!

            for row_index in range (self.num_columns):
                yield self[row_index]
        

        def __reversed__(self) -> Iterator[T]:
            # This is your backward iterator for column data!
            # 1. Loop row_index from (num_rows - 1) to 0
        	# and yield self[row_index] ⬅ uses Array2D __getitem__!
        
            for row_index in range (self.num_columns):
                row_index
                yield self[row_index]

            # raise NotImplementedError('Row.__reversed__ not implemented.')

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'

#Array2D class
    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        #  ⛈️ If `starting_sequence` is not a sequence, then raise ValueError
        # 2. ⛈️ If any of the rows in `starting_sequence` are not sequences, then 
        # 	raise ValueError
        # 3. ⛈️ If any of the data in `starting_sequence` are not an instance of 
        # 	`data_type`, then raise a ValueError
        # 4. ⛈️ If any of the rows are not the same length, then raise ValueError
        # 5. Save your instance variables (rows_len, cols_len, data_type)
        # 6. Last, instantiate your 1D Array object instance variable with the data in
        # 	`starting_sequence` using row major or column major

        if not isinstance(starting_sequence, Sequence):
            raise ValueError("Starting sequence is not a sequence type")
            
        for index in range(len(starting_sequence)):
            if not isinstance(starting_sequence[index], Sequence):
                raise ValueError
            
        for row in starting_sequence:
            for item in row:
                if not isinstance(item,data_type):
                    raise ValueError
        
        for item in starting_sequence:
            rowLen = len(starting_sequence)
            if len(item) != rowLen:
                raise ValueError
            
        self.data_type = data_type
        self.rows_len = len(starting_sequence)
        self.cols_len = len(starting_sequence[0])

        py_list = []
        for row in range(self.rows_len):
            for col in range(self.cols_len):
                py_list.append(starting_sequence[row][col])

        self.elements2d = Array(starting_sequence=py_list,data_type=data_type)

        # raise NotImplementedError('Array2D.__init__ not implemented.')

#Dont need an instance of an Array2D to use -> Array2D.empty() 
    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        #  Create a List that is row x cols size using a new instance of data_type()
        # 	so that each instance is unique (important for complex objects).
        # 2. Return an Array2D instance with your list from step 1 and data_type.

        py_list2d: List[List[T]] = []
        
        for row in range(rows):
            py_list2d.append([])
            for col in range(cols):
                py_list2d[row].append(data_type())

        return Array2D(starting_sequence=py_list2d,data_type=data_type)


    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        return Array2D.Row(row_index, self.elements2d, self.cols_len)

    def __iter__(self) -> Iterator[Sequence[T]]: 
        # This is your forward iterator for row data!
        # 1. Loop row_index from 0 to `num_rows`
        # yield self[row_index] ⬅ uses Array2Ds __getitem__!
        for row_index in range (self.rows_len):
                yield self[row_index]

    def __reversed__(self):
         for row_index in range (self.rows_len-1,-1,-1):
                yield self[row_index]
            # This is your backward iterator for row data!
            # 1. Loop from (row_index - 1) to 0
        	# 	yield self[row_index] ⬅ uses Array2Ds __getitem__!
        # raise NotImplementedError('Array2D.__reversed__ not implemented.')
    
    def __len__(self): 
        return self.rows_len
        # raise NotImplementedError('Array2D.__len__ not implemented')
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.rows_len} Rows x {self.cols_len} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')