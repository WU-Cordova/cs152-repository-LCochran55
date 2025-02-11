
from projects.project1.card import Card,CardSuit,CardFace
from projects.project1.multideck import Multideck

class Player:
    def __init__(self, hand: list) -> None:
        self.__hand: list = hand
    
    def addCards(self, card: Card) -> list: #Adds cards to hand
        self.__hand.append(card)

    def totalHand(self) -> int:
        total = 0

        for card in self.__hand:
            match card.card_face.value:
                case "J" | "K" | "Q":
                    total += 10
                case _:
                    total += int(card.card_face.value)
        return total
    
    def hit(self, deck: Multideck): #adds a single card to the deck and removes that card from the multi deck
        card = deck.deal_Card()
        self.addCards(card)
        deck.remove_Card(card)
    
    def returnHand(self): #Returns list of cards from the hand
        return self.__hand
    
    def clearHand(self):
        self.__hand.clear()
        return