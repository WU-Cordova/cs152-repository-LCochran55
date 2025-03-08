 
# MultiDeck: Represents a deck supporting multiple decks and provides functionality for dealing and shuffling.
from datastructures.bag import Bag
from projects.project1.card import Card,CardSuit,CardFace
import random as rdm

class Multideck: #Initializes the Bag for the deck and adds cards to it
    def __init__(self, multi_deck: Bag) -> None:

        self.__multi_deck: Bag = multi_deck



    def deal_Card(self): #Returns a random card from the deck, and removes that card
        dist_cards = self.__multi_deck.distinct_items() #Makes a list of each card in the deck, with doubles
        rCard = dist_cards[rdm.randint(0,len(dist_cards)-1)] #Chooses random card from the list by choosing a random index #
        self.remove_Card(rCard) #Removes the chosen card from the list
        return rCard
    
    def remove_Card(self,item): #Removes a card from the deck
        self.__multi_deck.remove(item)

    def clear_Deck(self):
        self.__multi_deck.clear()

    def create_Deck(self):
        num_of_decks = rdm.choice([2,4,6,8]) #Picks a random number of decks to be added to the multi deck

        for i in range(num_of_decks):
            for cardFace in CardFace: 
                for cardSuit in CardSuit: #loops through the card faces and suites to get a deck of cards
                    card = Card(cardFace,cardSuit)
                    self.__multi_deck.add(card)
