import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit






class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def suffle(self):
        suffle = random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop(0)

value_list = []
class Player:
    def __init__(self):
        deck = Deck()
        self.deck_sufffle = deck.suffle()
        self.cards = deck.all_cards
        print(self.cards[0])
        print(self.cards[1])
        value_list.append(self.cards[0].value)
        value_list.append(self.cards[1].value)
        print(value_list)
        self.cards.pop(0)
        self.cards.pop(1)

    def value_list_sum(self):
        soma = sum(value_list)
        print(soma)
        if soma < 21:
            return True
    def request(self):
        on = True
        while on:
            if self.value_list_sum():
                hit_stand = input('Choose: \nHit[1] \nStand[2]: ')
                if hit_stand == '1':
                    print(self.cards[0])
                    self.cards.pop(0)
                    value_list.append(self.cards[0].value)
                    print(value_list)
            else:
                on = False
        print('tchau')


# player = Player()
# player.request()

value_list_dealer = []
class Dealer:
    def __init__(self):
        print("Dealer's round")
        deck = Deck()
        self.deck_sufffle = deck.suffle()
        self.cards = deck.all_cards
        print('misterious card')
        print(self.cards[1])
        value_list_dealer.append(self.cards[0].value)
        value_list_dealer.append(self.cards[1].value)
        print(value_list_dealer)
        self.cards.pop(0)
        self.cards.pop(1)



dealer = Dealer()




