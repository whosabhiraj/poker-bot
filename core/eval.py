from deck import Card
from hand import Hand

def ev(hand):
    cards = hand.cards
    ranks = []
    for card in cards:
        if card.rank not in ranks: ranks.append(card.rank) 
    unique_ranks = len(ranks)

    if unique_ranks == 1:
        return(5, cards[0].rank)
    
    elif unique_ranks == 2:
        rank_freq = {}
        pair_rank = None
        kicker_rank = None

        for card in hand.cards:
            if card.rank in rank_freq:
                rank_freq[card.rank] += 1
            else:
                rank_freq[card.rank] = 1
        
        for rank, count in rank_freq.items():
            if count == 2:
                pair_rank = rank
            else:
                kicker_rank = rank
                
        return(2, pair_rank, kicker_rank)

    elif unique_ranks == 3:
        ranks = [card.rank for card in cards]
        suits = [card.suit for card in cards]
        ranks.sort(reverse = True)
        
        x = min(ranks)

        if x == 2 and 3 in ranks and 14 in ranks: # special: A23 straight
            if suits[0] == suits[1] and suits[0] == suits[2]:
                return(6, 3)
            else:
                return(4, 3)

        elif suits[0] == suits[1] and suits[0] == suits[2]:
            if x+1 in ranks and x+2 in ranks: # straight flush
                return(6, x+2)
            else: # flush
                return(3, ranks[0], ranks[1], ranks[2])

        elif x+1 in ranks and x+2 in ranks: # straight
            return(4, x+2)
        
        else: return(1, ranks[0], ranks[1], ranks[2])
