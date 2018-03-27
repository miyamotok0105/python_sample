#トランプの組みの表現するクラス
import collections

#python2.6以降：単純なクラスをnamedtupleで作れる。
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    from frenchdeck import FrenchDeck, Card
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck))

    print("この機能は__getitem__が提供している。")
    print(deck[0])

    print("スライス指定もできる")
    print(deck[:3])

    print(deck[12::13])

    print("インテレーションは暗黙的。コレクションに__contains__がなければin演算子が順番にスキャンしていく。")
    print(Card('Q', 'hearts') in deck)
    print("zはいないのでFales")
    print(Card('Z', 'clubs') in deck)

    for card in deck[:3]:  # doctest: +ELLIPSIS
        print(card)

    for card in reversed(deck[:3]):  # doctest: +ELLIPSIS
        print(card)

    for n, card in enumerate(deck[:3], 1):  # doctest: +ELLIPSIS
        print(n, card)

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]
    print(spades_high(Card('2', 'clubs')))
    print(spades_high(Card('A', 'spades')))

    for card in sorted(deck[:3], key=spades_high):  # doctest: +ELLIPSIS
        print(card)

