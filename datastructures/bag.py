from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]): #Bag implements IBAG interface
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.__bag: dict[T,int] = {}

        if items:
             for item in items:
                  self.add(item)

        # raise NotImplementedError("__init__ method not implemented")

    def add(self, item: T) -> None:
        if item in self.__bag:
            self.__bag[item] += 1
        else:
            self.__bag[item] = 1
        # raise NotImplementedError("add method not implemented")

    def remove(self, item: T) -> None:
        if item in self.__bag:
            self.__bag.pop(item)
        else:
            print("There are no items of that type in your bag")
            return
        # raise NotImplementedError("remove method not implemented")

    def count(self, item: T) -> int:
        if item in self.__bag:
            count = self.__bag[item]
            print("There are" + count + item + "s in your bag")
        else:
            print("There are no items of that type in your bag")
            return
        # raise NotImplementedError("count method not implemented")

    def __len__(self) -> int:
        raise NotImplementedError("__len__ method not implemented")

    def distinct_items(self) -> Iterable[T]:
        raise NotImplementedError("distinct_items method not implemented")

    def __contains__(self, item) -> bool:
        raise NotImplementedError("__contains__ method not implemented")

    def clear(self) -> None:
        raise NotImplementedError("clear method not implemented")