import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets: Array[LinkedList[Tuple[KT, VT]]] = \
                Array(starting_sequence=[LinkedList(data_type=tuple) for _ in range(number_of_buckets)],
                      data_type=LinkedList)
        self._count: int = 0
        self._load_factor: float = 0

        self._hash_function = custom_hash_function or self._default_hash_function
    
    def get_bucket_index(self,key: KT, bucket_size: int) -> int:
        bucket_index = self._hash_function(key)
        return bucket_index % len(bucket_size)

    def __getitem__(self, key: KT) -> VT:

        bucket_chain: LinkedList = self._buckets[self.get_bucket_index(key,len(self._buckets))]
        
        for (k,v) in bucket_chain:
            if k == key:
                return k #FOUND
        raise IndexError

    def __setitem__(self, key: KT, value: VT) -> None:        
        raise NotImplementedError("HashMap.__setitem__() is not implemented yet.")

    def keys(self) -> Iterator[KT]:
        raise
    
    def values(self) -> Iterator[VT]:
        raise NotImplementedError("HashMap.values() is not implemented yet.")

    def items(self) -> Iterator[Tuple[KT, VT]]:
        raise NotImplementedError("HashMap.items() is not implemented yet.")
            
    def __delitem__(self, key: KT) -> None:
        raise NotImplementedError("HashMap.__delitem__() is not implemented yet.")
    
    def __contains__(self, key: KT) -> bool:
        #1. Get bucket index based on key
        bucket_index = self.get_bucket_index(key,len(self._buckets))

        #2 Get bucket chain
        bucket_chain: LinkedList = self._buckets[bucket_index]

        #3 Search if that key exist
        for (k,v) in bucket_chain:
            if k == key:
                return True #FOUND
        return False #NOT FOUND
    
    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:
        raise NotImplementedError("HashMap.__iter__() is not implemented yet.")
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("HashMap.__eq__() is not implemented yet.")

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)
    