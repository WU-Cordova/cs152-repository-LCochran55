
#   Card: Represents a single playing card (face, suit, and value).
from dataclasses import dataclass
from enum import Enum

class CardSuit(Enum): 
    HEARTS = "♡"
    SPADES = "♤"
    CLUBS = "♧"
    DIAMONDS = "♢"

class CardFace(Enum):
    TEN = "10"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "1"

@dataclass
class Card:
    card_face: CardFace
    card_suit : CardSuit
    
    def __hash__(self): #Allows each card to have a unique hash
        return hash(self.card_face.name) + hash(self.card_suit.name)
        # if(self.card_face.value not in ["J","K","Q"]):
        #     if(self.card_suit.name == "HEARTS"):
        #         return int(self.card_face.value)*1
        #     elif(self.card_suit.name == "SPADES"):
        #         return int(self.card_face.value)*2
        #     elif(self.card_suit.name == "CLUBS"):
        #         return int(self.card_face.value)*3
        #     elif(self.card_suit.name == "DIAMONDS"):
        #         return int(self.card_face.value)*4
        # else:
        #     if(self.card_suit.name == "HEARTS"):
        #         return 10*1
        #     elif(self.card_suit.name == "SPADES"):
        #         return 10*2
        #     elif(self.card_suit.name == "CLUBS"):
        #         return 10*3
        #     elif(self.card_suit.name == "DIAMONDS"):
        #         return 10*4
    
    def __repr__(self): #Makes the card return in a nicer looking way
        return str(f"[{self.card_suit.value} {self.card_face.value}]")