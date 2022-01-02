"""
    THIS IS THE PRACTICE PROJECT OF JOSE PYTHON COURSE.
    THIS IS CARD GAME CALLED WAR.
"""

import random

suits = ("Hearts", "Diamonds", "Clubs", "Spades")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

class Card():

    def __init__(self, rank, suit):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


mycard = Card('King', 'Hearts')
print(mycard)
print(mycard.rank)
print(mycard.suit)
print(mycard.value)

class Deck():

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:

                created_card = Card(rank, suit)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


mydeck = Deck()

mydeck.shuffle()
first_card = mydeck.all_cards[0]
print(first_card)

class Player():

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # For list of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card object.
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


myplayer = Player("Aditya")

print(myplayer)
myplayer.add_cards(first_card)
print(myplayer)
myplayer.remove_one()
print(myplayer)
myplayer.add_cards([first_card, first_card, first_card])
print(myplayer)
myplayer.remove_one()
myplayer.remove_one()
myplayer.remove_one()
print(myplayer)


# GAME LOGIC

player_one = Player("one")
player_two = Player("two")

new_deck = Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

print(len(player_one.all_cards), len(player_two.all_cards))

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player one is out of cards! Player two wins!")
        game_on = False
        break
    
    if len(player_two.all_cards) == 0:
        print("Player two is out of cards! Player one wins!")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print('player one unable to play war! game over at war')
                print('player two wins! player one loses!')
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print('player two unable to play war! game over at war')
                print('player one wins! player two loses!')
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

