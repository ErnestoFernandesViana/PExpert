
import random 

class Deck:
    suit = ('D', 'H', 'C', 'S')
    value = [str(x) for x in range(2,11)] + ['J','Q','K','A']


    def __init__(self):
        self.deck = [x+y for x in Deck.value for y in Deck.suit]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, n):
        if n < len(self.deck):
            return [self.deck.pop() for x in range(n)]
        else:
            return self.deck
        
    def sort_by_suit(self):
        hearts = [x for x in self.deck if x[1] == 'H']
        diamonds = [x for x in self.deck if x[1] == 'D']
        clubs = [x for x in self.deck if x[1] == 'C']
        spades = [x for x in self.deck if x[1] == 'S']
        self.deck = hearts + diamonds + clubs + spades

    def contains(self, card):
        if card in self.deck:
            return True 
        else: 
            return False 

    def copy(self):
        new_deck = Deck()
        new_deck.deck = self.deck[:]
        return new_deck
        

    def get_cards(self):
       return self.deck[:]

    def __len__(self):
        return len(self.deck)


d = Deck()
d.shuffle()
print(d.sort_by_suit())
print(d.deck)