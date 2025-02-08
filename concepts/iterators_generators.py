from collections import namedtuple
import re
import reprlib

RE_WORD = re.compile('\w+')
Card = namedtuple('Card1', ['rank', 'suit'])

class FrenchDeck:
    range = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suits = [s.capitalize() for s in suits]
    print(range)
    print(suits)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.range]

    def __len__(self):
        return len(self._cards)

    def get_cards(self):
        return self._cards

    # iterator function
    # def __iter__(self):
    #     return iter(self._cards)

    # generator function.
    def __iter__(self):
        for card in self._cards:
            yield card
        return

    def __next__(self):
        for card in self._cards:
            yield card
        return

    def __getitem__(self, position):
        return self._cards[position]


"""
dunder methods are special methods that Python uses to perform various operations.
"""

class Sentence:
    def __init__(se, text):
        se.text = text
        se.words = RE_WORD.findall(text)
    # when iter is calling, this is access.
    def __iter__(self):
        return iter(self.words)
    # if iter is not found, get item is accessed.
    def __getitem__(self, index):
        return self.words[index]
    # else python throws an error that object is not iterable.

    def __repr__(self): ## this is like the toString metohd in java.
        return f'Sentence is {self.text}'

    def get_words(se):
        return se.words


if __name__ == "__main__":
    f = FrenchDeck()
    #
    # print(f[2]) # this works when python has __getitem__ method implemented
    # for card in f: # this works when python has __iter__ method implemented
    #     print(card.rank)
    # print(f[2:5]) # this works when python has __getitem__ method implemented

    # to check if the instance is iterable or not.
    try:
        iter(f)
    except TypeError:
        print('Type Error')

    c = f.__next__()
    print(next(c))
    print(next(c))

if __name__ == "__main__":
    s = Sentence('hello i am ron weasely')
    print(s.get_words())
    print(s)
