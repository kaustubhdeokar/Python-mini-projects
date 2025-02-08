from collections import namedtuple

"""
 A tuple in Python is a contiguous block of memory that stores references (pointers) to objects, 
 which can be located anywhere in memory. This allows for efficient access to the elements of the 
 tuple while keeping the memory footprint low.
"""

Card = namedtuple('Card', ['rank', 'suit'])


# Create a deck of cards
def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [Card(rank, suit) for suit in suits for rank in ranks]
    return deck


deck = create_deck()


def compare_two_cars(card1, card2):
    str_card_rank_1 = card1.rank
    str_card_rank_2 = card2.rank
    str_card_suite_1 = card1.suit
    str_card_suite_2 = card2.suit

    card_1 = Card(str_card_rank_1, str_card_suite_1)
    card_2 = Card(str_card_rank_2, str_card_suite_2)

    index_card_1 = deck.index(card_1)
    index_card_2 = deck.index(card_2)
    print('i1', index_card_1, 'i2', index_card_2)


if __name__ == "__main__":
    Card1 = Card('Ace', 'Hearts')
    Card2 = Card('King', 'Hearts')
    compare_two_cars(Card2, Card1)
