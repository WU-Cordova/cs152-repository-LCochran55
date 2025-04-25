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
            raise TypeError("Cannot add None")
        else:
            self.__bag[item] = 1
        # raise NotImplementedError("add method not implemented")

    def remove(self, item: T) -> None:
        if item in self.__bag:
            self.__bag[item] -= 1
        else:
            raise ValueError("Cannot remove None")

        # raise NotImplementedError("remove method not implemented")

    def count(self, item: T) -> int:
        if item in self.__bag:
            count = self.__bag[item]
            return count
        else:
            return 0
        # raise NotImplementedError("count method not implemented")

    def __len__(self) -> int:
        total = 0
        for items in self.__bag:
            total += self.__bag[items]
        return total
        # raise NotImplementedError("__len__ method not implemented")

    def distinct_items(self) -> Iterable[T]:
        dist_items = []
        for items in self.__bag:
            for i in range (0,self.count(items)):
                dist_items.append(items)
        return dist_items

        # raise NotImplementedError("distinct_items method not implemented")

    def __contains__(self, item) -> bool:
        if item in self.__bag:
            return True
        else:
            return False
        # raise NotImplementedError("__contains__ method not implemented")

    def clear(self) -> None:
        self.__bag.clear()
        # raise NotImplementedError("clear method not implemented")

    def __str__(self) -> str:
        return f"%s" % str (self.__bag)