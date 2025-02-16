# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray
import copy


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        self.__logical_size: int = len(starting_sequence)
        self.__physical_size: int = self.__logical_size
        self.__data_type: type = data_type

        self.__elements = np.empty(self.__logical_size, dtype=self.__data_type)

        for index in range(self.__logical_size):
            self.__elements[index] = copy.deepcopy(starting_sequence[index])

        if not isinstance(starting_sequence,Sequence):
            raise ValueError("starting_sequence must be a valid sequence type")
        
        for index in range(self.__logical_size):
            if not isinstance(starting_sequence[index],self.__data_type):
                raise TypeError("items in starting_sequence must be the same data type")
            
        for item in starting_sequence:
            if not isinstance(item,self.__data_type):
                raise TypeError(f"Item{repr(item)} is not of type {str(data_type)}")



    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
            #make sure item exists 
            if isinstance(index,slice):
                start = slice.start
                stop = slice.stop
                step = slice.step

                if start<self.__logical_size-1 or start>-(self.__logical_size-1) and stop <= self.__logical_size-1 or stop >= -(self.__logical_size-1):
                    return Array(starting_sequence=self.__elements[index].tolist(),data_type=self.__data_type) # item if its a slice
                else:
                    raise IndexError("Your start or stop if out of range of your list")
                #check if start abd sto[ are in nobund]
                #if nto raise an exception  
            
            elif isinstance(index,int):
                if(index<=self.__logical_size-1):
                    return self.__elements[index] #item if index is an int
                else:
                    raise IndexError("Index is out of range")
                #check if index in bounds
                #if not raise an exceptio

            # raise NotImplementedError('Indexing not implemented.')
    
    def __setitem__(self, index: int, item: T) -> None:
        #check if index if out of bounds or iem is right type
        self.__elements[index] = item
        # raise NotImplementedError('Indexing not implemented.')

    def append(self, data: T) -> None:
        self.__elements.append(data)

        # raise NotImplementedError('Append not implemented.')
    
    def __grow(self,new_size:int) -> None:

        if(self.__elements):
        #for append methods

        #If array doesnt need to grow, exit
        #Create a new numpy array with new size
        #copy over the elementsfrom the crrent numpy array to the new one
        #set the current numpy array to the new one
            pass

    def append_front(self, data: T) -> None:
        #append item tofront of list
        #Groaw as needed
        raise NotImplementedError('Append front not implemented.')

    def pop(self) -> None:
        #self.__delitem__(self.__logical_size+-count-1)
        #or
        #         #del self[]
        raise NotImplementedError('Pop not implemented.')
    
    def pop_front(self) -> None:
        raise NotImplementedError('Pop front not implemented.')

    def __len__(self) -> int: 
        return self.__logical_size
        # raise NotImplementedError('Length not implemented.')

    def __eq__(self, other: object) -> bool:
        # for loop thru logical size
        #if not Other[index] == Self[index] etc
        index = 0
        for index in range(self.__logical_size):
            if self.__elements[index] != other[index]:
                return False
        return True
        # raise NotImplementedError('Equality not implemented.')
    
    def __iter__(self) -> Iterator[T]:
        raise NotImplementedError('Iteration not implemented.')

    def __reversed__(self) -> Iterator[T]:
        #Slicing 
        raise

    def __delitem__(self, index: int) -> None:
       #deletes item at the index\
       # .// capacity (floor)
       raise NotImplementedError('Delete not implemented.')

    def __contains__(self, item: Any) -> bool:
        return np.isin(item, self.__elements)
        #Numpy supports contain
        #Any function
        # raise NotImplementedError('Contains not implemented.')

    def clear(self) -> None:
        #make new empty array  and reassign
        raise NotImplementedError('Clear not implemented.')

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__item_count}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')