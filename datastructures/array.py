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


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        self.__logical_size: int = len(starting_sequence)
        self.__physics_size: int = self.__logical_size
        self.__data_type: type = data_type

        if not isinstance(starting_sequence,Sequence):
            raise ValueError("starting_sequence must be a valid sequence type")
        
        for index in range(self.__logical_size):
            if not isinstance(starting_sequence[index],self.__data_type):
                raise TypeError("items in starting_sequence must be the same data type")
            
        for item in starting_sequence
            if not isinstance(item,self.__data_type):
                raise TypeError(f"Item{repr(item)} is not of type {str(data_type)}")

        self.__items: NDArray = np.empty(self.__logical_size,dtype:self.__data_type)

        for index in range(self.__logical_size):
            self.__items[index] = starting_sequence[index]



    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
            raise NotImplementedError('Indexing not implemented.')
    
    def __setitem__(self, index: int, item: T) -> None:
        raise NotImplementedError('Indexing not implemented.')

    def append(self, data: T) -> None:
        raise NotImplementedError('Append not implemented.')

    def append_front(self, data: T) -> None:
        raise NotImplementedError('Append front not implemented.')

    def pop(self) -> None:
        raise NotImplementedError('Pop not implemented.')
    
    def pop_front(self) -> None:
        raise NotImplementedError('Pop front not implemented.')

    def __len__(self) -> int: 
        raise NotImplementedError('Length not implemented.')

    def __eq__(self, other: object) -> bool:
        # for loop thru logical size
        #if not Other[index] == Self[index] etc
        raise NotImplementedError('Equality not implemented.')
    
    def __iter__(self) -> Iterator[T]:
        raise NotImplementedError('Iteration not implemented.')

    def __reversed__(self) -> Iterator[T]:
        #Slicing 
        raise

    def __delitem__(self, index: int) -> None:
       raise NotImplementedError('Delete not implemented.')

    def __contains__(self, item: Any) -> bool:
        #Numpy supports contain
        #Any function
        raise NotImplementedError('Contains not implemented.')

    def clear(self) -> None:
        raise NotImplementedError('Clear not implemented.')

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__item_count}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')