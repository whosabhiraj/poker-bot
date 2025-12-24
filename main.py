from core.deck import Card
from core.engine import probabilities, EVs
def main():
    hole1 = Card('Q', 's')      #
    hole2 = Card('A', 'h')      # examples
    community = Card('2', 'c')  #

    probs = probabilities(hole1, hole2, community)
    evs = EVs(hole1, hole2, community)
    action = max(evs, key=lambda k: evs[k])

    print("Hand:")
    print(f"  Hole cards: {hole1}, {hole2}")
    print(f"  Community:  {community}\n")

    print("Probabilities:")
    for k, v in probs.items():
        print(f"  P({k}) = {v}")

    print("\nExpected Values:")
    for k, v in evs.items():
        print(f"  EV({k}) = {v}")

    print(f"\nChosen action: {action.upper()}")

if __name__ == "__main__":
    main()
