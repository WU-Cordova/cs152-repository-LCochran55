
from datastructures.bag import Bag
from projects.project1.card import Card,CardSuit,CardFace
from projects.project1.multideck import Multideck
from projects.project1.game import Game

def main():

    player = Bag
    dealer = Bag
    deck = Multideck()
    game = Game(player,dealer,deck)
    game.deal()




if __name__ == '__main__':
    main()
