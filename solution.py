from itertools import combinations
from collections import Counter





def hand(hole_cards, community_cards):
    ranks = {
        "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10, "J": 11, "Q": 12,
        "K": 13, "A": 14,
    }

    hand_names = {
        9: "straight-flush",
        8: "four-of-a-kind",
        7: "full-house",
        6: "flush",
        5: "straight",
        4: "three-of-a-kind",
        3: "two pair",
        2: "pair",
        1: "nothing"
    }

    def rank(card):
        return ranks[card[0]]

    def find_straight(cards):
        ranks_card = sorted({rank(c) for c in cards}, reverse=True)

        if 14 in ranks:
            ranks_card.append(1)

        for i in range(len(ranks) - 4):
            window = ranks[i:i+5]
            if window[0] - window[4] == 4:
                return window[0]

        return None

    def score_five(cards):
        ranks_card = [rank(c) for c in cards]
        counts = Counter(ranks_card)

        groups = sorted(
            counts.items(),
            key=lambda x: (x[1], x[0]),
            reverse=True
        )

        flush = len({c[1] for c in cards}) == 1
        straight = find_straight(cards)

        if flush and straight:
            return (8, straight)

        if groups[0][1] == 4:
            quad = groups[0][0]
            kicker = max(r for r in ranks_card if r != quad)
            return 7, quad, kicker
    hole_grouped_cards = [list(card) for card in hole_cards]
    community_card_grouped_cards = [list(card) for card in community_cards]
    print(hole_grouped_cards)

    all_cards = sum(hole_grouped_cards,[]) + sum(community_card_grouped_cards, [])
    counts = Counter(all_cards)
    print(counts)

    return "nothing", ["2", "3", "4", "7", "8"]


hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"])