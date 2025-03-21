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

        if not isinstance(starting_sequence,Sequence):
            raise ValueError("starting_sequence must be a valid sequence type")
        
        self.__logical_size: int = len(starting_sequence)
        self.__physical_size: int = self.__logical_size
        self.__data_type = data_type
        
        for index in range(self.__logical_size):
            if not isinstance(starting_sequence[index],self.__data_type):
                raise TypeError("items in starting_sequence must be the same data type")
            
        for item in starting_sequence:
            if not isinstance(item,self.__data_type):
                raise TypeError(f"Item{repr(item)} is not of type {str(data_type)}")
        
        self.__elements = np.empty(self.__logical_size, dtype=self.__data_type)
            
        for index in range(self.__logical_size):
            self.__elements[index] = copy.deepcopy(starting_sequence[index])

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
            #make sure item exists 
        if isinstance(index, int):
            data = self.__elements[index]
            return data.item() if isinstance(data, np.generic) else data

        elif isinstance(index, slice):
            data_list = []
            for data in self.__elements[index]:
                data_list.append(data.item() if isinstance(data, np.generic) else data)
            return Array(starting_sequence=data_list, data_type=self.__data_type)

        else:
            raise TypeError("Was not an int or a slice")

            # raise NotImplementedError('Indexing not implemented.')
    
    def __setitem__(self, index: int, item: T) -> None:
        #check if index if out of bounds or iem is right type
        if(isinstance(item,self.__data_type)):
            self.__elements[index] = item
        else:
            raise TypeError("Item does not contain same type as Array")
        # raise NotImplementedError('Indexing not implemented.')

    def append(self, data: T) -> None:
        listElements = self.__elements.tolist()
        listElements.append(data)
        self.__elements = np.array(listElements)
        self.__logical_size += 1
        self.grow()

        # raise NotImplementedError('Append not implemented.')
    
    def grow(self) -> None:
        if(self.__logical_size is self.__physical_size):
            self.__physical_size *= 2
            self.__newElements= np.empty(self.__physical_size,dtype=self.__data_type)
            for index in range(self.__logical_size):
                self.__newElements[index] = copy.deepcopy(self.__elements)
            self.__elements = self.__newElements
        else:
            exit
        #for append methods

        #If array doesnt need to grow, exit
        #Create a new numpy array with new size
        #copy over the elementsfrom the crrent numpy array to the new one
        #set the current numpy array to the new one
    def __shrink(self):
        if(self.__logical_size == self.__physical_size//2):
            self.__physical_size//2
            self.__newElements= np.empty(self.__physical_size,dtype=self.__data_type)
            # for index in range(self.__physical_size):
            self.__newElements = copy.deepcopy(self.__elements)
            self.__elements = self.__newElements
        else:
            exit

    def append_front(self, data: T) -> None:
        listElements = self.__elements.tolist()
        listElements.insert(0,data)
        self.__elements = np.array(listElements)
        self.__logical_size += 1
        self.grow()

        #append item tofront of list
        #Groaw as needed
        # raise NotImplementedError('Append front not implemented.')

    def pop(self) -> None:
        listElements = self.__elements.tolist()
        popped = listElements[self.__logical_size-1]
        self.__delitem__(self.__logical_size-1)
        self.__logical_size -= 1
        self.__shrink()
        return popped

        # raise NotImplementedError('Pop not implemented.')
    
    def pop_front(self) -> None:
        listElements = self.__elements.tolist()
        popped = listElements[0]
        self.__delitem__(0)
        self.__logical_size -= 1
        self.__shrink()
        return popped
        # raise NotImplementedError('Pop front not implemented.')

    def remove(self, index: int) -> None:
        if index > self.__logical_size-1:
            raise IndexError
        listElements = self.__elements.tolist()
        popped = listElements[index]
        self.__delitem__(index)
        self.__logical_size -= 1
        self.__shrink()
        return popped
    

    def __len__(self) -> int: 
        return self.__logical_size
        # raise NotImplementedError('Length not implemented.')

    def __eq__(self, other: object) -> bool:
        # for loop thru logical size
        #if not Other[index] == Self[index] etc
        if isinstance(other, Array) and len(self) == len(other):
            for i in range(len(self)):
                if self[i] != other[i]: 
                    return False
            return True
        # raise NotImplementedError('Equality not implemented.')
    
    def __iter__(self) -> Iterator[T]:
        for element in self.__elements:
            yield element
        # raise NotImplementedError('Iteration not implemented.')

    def __reversed__(self) -> Iterator[T]:
        reversedArray = self.__elements[::-1]
        return iter(reversedArray)

        # self.__elements = np.array(reversedList)
        #Slicing 

    def __delitem__(self, index: int) -> None:
       #deletes item at the index\
       # .// capacity (floor)
       self.__elements = np.delete(self.__elements,index)

    def __contains__(self, item: Any) -> bool:
        return np.isin(item, self.__elements)
        #Numpy supports contain
        #Any function
        # raise NotImplementedError('Contains not implemented.')

    def clear(self) -> None:
        #make new empty array  and reassign
        self.__logical_size: int = 0
        self.__physical_size: int = 0

        self.__elements = np.empty(self.__logical_size)
        # raise NotImplementedError('Clear not implemented.')

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__logical_size}, Physical: {len(self.__elements)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')