
# 
# Game: Implements the core game logic, including player and dealer turns, win conditions, and score calculation.
from datastructures.bag import Bag
from projects.project1.card import Card,CardSuit,CardFace
from projects.project1.multideck import Multideck
from projects.project1.player import Player
import random as radm

class Game:
    def __init__(self, player: Player, dealer: Player, deck: Multideck): 
        self.__deck: Multideck = deck
        self.__player: Player = player
        self.__dealer: Player = dealer
    

    def deal(self): #Deals two cards for dealer and player using functions in the deck & player class

        for i in range(2):
            card = self.__deck.deal_Card()
            self.__player.addCards(card)

        for i in range(2):
            card = self.__deck.deal_Card()
            self.__dealer.addCards(card)


    def start_game(self):

        self.__deck.create_Deck()

        self.deal() #Deals two cards to dealer & player
        
        match self.__dealer.returnHand()[0].card_face.value:
                case "J" | "K" | "Q":
                    print(f"\nInitial Deal \n Player's hand: {self.__player.returnHand()} | Score: {self.__player.totalHand()} \n Dealer's hand: {self.__dealer.returnHand()[0]} [Hidden] | Score: 10")
                case _:
                    print(f"\nInitial Deal \n Player's hand: {self.__player.returnHand()} | Score: {self.__player.totalHand()} \n Dealer's hand: {self.__dealer.returnHand()[0]} [Hidden] | Score: {self.__dealer.returnHand()[0].card_face.value}")
        
        if (self.__player.totalHand() == 21): #Catches if player begins with blackjack
            print("Player has blackjack! Player wins.")
        else:

            while(self.__player.totalHand() < 21 and self.__dealer.totalHand() < 21 ): #Allows the game to loop until player value becomes more than 21
                    
                    print(f"\nPlayer's Turn \n Players hand: {self.__player.returnHand()} | Score: {self.__player.totalHand()}")

                    choice = (input(" Would you like to [H]it or [S]tay?: "))

                    while(choice != "H" and choice != "S"): #If players choice is not H or S, will ask for new choice
                        choice = (input("That is not a valid input. Would you like to [H]it or [S]tay?: "))
                    
                    if choice == "H":
                        hits = 1
                        dealerScore = 0
                        self.__player.hit(self.__deck) #player hits and adds another card to their deck
                        for i in range(hits):
                            match self.__dealer.returnHand()[hits].card_face.value:
                                case "J" | "K" | "Q":
                                    dealerScore+=10
                                case _:
                                    dealerScore+=self.__dealer.returnHand()[hits].card_face.value
                        hits +=1

                        print(f"\n Dealer's hand: {self.__dealer.returnHand()[0:hits]} [Hidden] | Score: {dealerScore}\n Players hand: {self.__player.returnHand()} | Score: {self.__player.totalHand()}")


                        if(self.__player.totalHand() >= 21): #Check if player busts
                            print(f"\nPlayer's hand: {self.__player.returnHand()} | Score: {self.__player.totalHand()}\nBust! You went over 21.")

                            print(f"\nDealer's hand: {self.__dealer.returnHand()}| Score: {self.__dealer.totalHand()}\n Dealer wins! Player busted.")
                
                        self.__dealer.hit(self.__deck)

                    else: #If player decides to stay

                        while(self.__dealer.totalHand() < 17): #Continuously adds cards to dealers hand until dealer's score becomes < than 17
                            self.__dealer.hit(self.__deck)

                        print(f"\n Dealer's hand: {self.__dealer.returnHand()} | Score: {self.__dealer.totalHand()}")

                        if(self.__dealer.totalHand()>self.__player.totalHand() and self.__dealer.totalHand()<21): #If dealer score is more than player score, dealer wins
                            print("Dealer wins!")
                            break #Breaks from the while loop
                        elif(self.__dealer.totalHand()>=21):
                            print("Player wins! Dealer busted!")
                        else: #Player score > dealer, player wins
                            print("Player wins!")
                            break
        self.play_again()
        

    def play_again(self): #Asks the player to play again
            play_again = input("\nWould you like to play again? [Y]es or [N]o: ")
            if (play_again == "Y"):
                self.__dealer.clearHand()
                self.__player.clearHand()
                self.__deck.clear_Deck()
                self.start_game()
            elif (play_again == "N"):
                exit
            else: #Asks until player answers with Y or N
                print("That is not a valid input.")
                self.play_again()
            