import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.deck import Card

card1 = Card('K', 's')

print(Card.full_deck())