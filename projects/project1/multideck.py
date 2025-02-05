 
# MultiDeck: Represents a deck supporting multiple decks and provides functionality for dealing and shuffling.
from datastructures.bag import Bag
from projects.project1.card import Card,CardSuit,CardFace
import random as rdm

class Multideck:
    def __init__(self) -> None:
        num_of_decks = rdm.choice([2,4,6,8])
        self.__multi_deck = Bag
        card_list = []
        for cardFace in CardFace:
            for cardSuit in CardSuit:
                card = Card(card_face=cardFace,card_suit=cardSuit)
                print(card)
                self.__multi_deck.add(card)
        
    def shuffle_Deck(self):
        rdm.shuffle(self.__multi_deck)

    def deal_Card(self):
        rCard = rdm.choice(self.__multi_deck)
        return rCard

