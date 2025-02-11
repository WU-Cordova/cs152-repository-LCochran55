
from datastructures.bag import Bag
from projects.project1.card import Card,CardSuit,CardFace
from projects.project1.multideck import Multideck
from projects.project1.player import Player
from projects.project1.game import Game

def main():

    player_hand = []
    dealer_hand = []
    deck_Bag = Bag()
    player = Player(player_hand)
    dealer = Player(dealer_hand)
    deck = Multideck(deck_Bag)
    game = Game(player,dealer,deck)

    game.start_game()


if __name__ == '__main__':
    main()
