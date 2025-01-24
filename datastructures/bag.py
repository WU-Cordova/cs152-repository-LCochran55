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
        elif item == None:
            raise ValueError("Cannot add None")
        else:
            self.__bag[item] = 1
        # raise NotImplementedError("add method not implemented")

    def remove(self, item: T) -> None:
        if item in self.__bag:
            self.__bag[item] -= 1
        elif item == None:
            raise ValueError("Cannot remove None")
        else:
            print("There are no items of that type in your bag")
            return
        # raise NotImplementedError("remove method not implemented")

    def count(self, item: T) -> int:
        if item in self.__bag:
            count = self.__bag[item]
            return count
        else:
            print("There are no items of that type in your bag")
            return
        # raise NotImplementedError("count method not implemented")

    def __len__(self) -> int:
        total = 0
        for items in self.__bag:
            total += self.__bag[items]
        return total
        # raise NotImplementedError("__len__ method not implemented")

    def distinct_items(self) -> Iterable[T]:
        raise NotImplementedError("distinct_items method not implemented")

    def __contains__(self, item) -> bool:
        if item in self.__bag:
            return True
        else:
            return False
        # raise NotImplementedError("__contains__ method not implemented")

    def clear(self) -> None:
        self.__bag.clear()
        # raise NotImplementedError("clear method not implemented")