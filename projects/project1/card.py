
#   Card: Represents a single playing card (face, suit, and value).
from dataclasses import dataclass
from enum import Enum

class CardSuit(Enum):
    HEARTS = "♡"
    SPADES = "♤"
    CLUBS = "♧"
    DIAMONDS = "♢"

class CardFace(Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    JACK = "10"
    QUEEN = "10"
    KING = "10"
    ACE = "11"

@dataclass
class Card:
    card_face: CardFace
    card_suit : CardSuit