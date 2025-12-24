from .eval import evaluate
from .deck import Card
from .hand import Hand

def probabilities(hole1, hole2, community) -> dict[str, float]:
    seen = {hole1, hole2, community}
    hand_self = Hand(hole1, hole2, community)
    score_self = evaluate(hand_self)

    full_deck = Card.full_deck()
    remaining_deck = [card for card in full_deck if card not in seen]

    wins = 0
    losses = 0
    ties = 0
    iterations = 0

    for i in range(len(remaining_deck)):
        for j in range(i+1, len(remaining_deck)):
            hand_opponent = Hand(remaining_deck[i], remaining_deck[j], community)
            score_opponent = evaluate(hand_opponent)

            iterations += 1

            if score_self > score_opponent:
                wins += 1
            elif score_self < score_opponent:
                losses += 1
            else: ties += 1

    P_win = wins/iterations
    P_loss = losses/iterations
    P_tie = ties/iterations

    return({
        "win": P_win,
        "tie": P_tie,
        "loss": P_loss,
    })

def EVs(hole1, hole2, community) -> dict[str, float]:
    prob = probabilities(hole1, hole2, community)
    return({
        "fold": -1,
        "call": 2*prob["win"] + -2*prob["loss"] + 0*prob["tie"],
        "raise": 3*prob["win"] + -3*prob["loss"] + 0*prob["tie"],
    })
