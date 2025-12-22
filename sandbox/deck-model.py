class Card:
    rank_map = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
        'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    def __init__(self, rank_str, suit):
        self.rank_str = rank_str
        self.suit = suit
        self.rank = self.rank_map[rank_str]

        suit_id = {'c': 0, 'd': 1, 'h': 2, 's':3}[self.suit]
        self.id = (suit_id * 13) + (self.rank - 2)

    def __repr__(self):
        return(f"{self.rank_str}{self.suit}")
    
    def __isLower__(self, other):
        return self.rank < other.rank
    
    def __eq__(self, other):
        if not isinstance(other, Card): # if Card is compared to any other type 
            return False
        return self.id == other.id # compares the unique rank/suit ID
    
    def __hash__(self):
        return hash(self.id) # unique and uniform for a particular card eg. 'As'

ranks = '23456789TJQKA'
suits = 'shdc'

full_deck = [Card(r, s) for r in ranks for s in suits]
my_hole_cards = [Card('K', 's'), Card('A', 's')]
community_card = Card('Q', 's')

print(full_deck)

seen = set(my_hole_cards) 
seen.add(community_card)
print(seen)

remaining = {card for card in full_deck if card not in seen}

print(remaining)

card1 = Card('Q', 's')
card2 = Card('Q', 's')

print(f"Memory Address 1: {id(card1)}")
print(f"Memory Address 2: {id(card2)}")
print(f"Are they the same object? {card1 is card2}")
print(f"Are they 'Equal' because of the code? {card1 == card2}")

print(card1.id)
print(card1.__hash__())

"""
python usually compares memory addresses when "if card not in seen" is called.
it fails because card1 card2 are two different objects even if their value seems the same
__eq__ is used to compare two card objects using ==, also used by "not in"

seen is made as a set() which builds a lookup table
when a card is checked for seen, it calls __hash__ on the card we want to check and then DIRECTLY goes to the address in seen
if its empty, we instantly know its not seen. if it has something, we use __eq__ to check if its the same card
"""