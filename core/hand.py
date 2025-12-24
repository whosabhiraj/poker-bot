from .deck import Card

class Hand:
    def __init__(self, hole1, hole2, community):
        self.cards = [hole1, hole2, community]
        self.cards.sort(reverse = True)

    def __repr__(self):
        return(f"{[card for card in self.cards]}")
