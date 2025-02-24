
from datastructures.bag import Bag

def main():
    
    print("Hello, World!")
    bag = Bag()
    bag.add("apple")
    print(bag.distinct_items())
    print(bag.count("apple"))

main()