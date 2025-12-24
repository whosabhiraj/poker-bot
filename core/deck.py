ranks = '23456789TJQKA'
suits = 'cdhs'

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

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
    
    def __lt__(self, other):
        return self.rank < other.rank
    
    @staticmethod
    def full_deck():
        return [Card(r, s) for s in suits for r in ranks]
    
    def remaining_deck(self, hole, community):
        full_deck = self.full_deck()

        seen = set(hole)
        seen.add(community)

        return [card for card in full_deck if card not in seen]
