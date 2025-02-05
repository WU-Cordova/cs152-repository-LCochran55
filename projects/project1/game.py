
# 
# Game: Implements the core game logic, including player and dealer turns, win conditions, and score calculation.
from datastructures.bag import Bag
from projects.project1.card import Card,CardSuit,CardFace
from projects.project1.multideck import Multideck
import random as radm

class Game:
    def __init__(self, player: Bag, dealer: Bag, deck: Multideck):
        self.__deck: Multideck = deck
        self.__player: Bag = player
        self.__dealer: Bag = dealer
    
    def deal(self):
        card = Card
        for i in range(2):
            card = self.__deck.deal_Card()
            playerCards = self.__player.add(card)
        print(playerCards)