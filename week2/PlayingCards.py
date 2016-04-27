import unittest
class PlayingCard:
    """creates a playing card with (suit, value)"""
    def __init__ (self, suit=0, value=2):
        self.suit = suit
        self.value = value


    suit_names = ['heart', 'diamond', 'spade', 'club']
    value_names = [None, 'ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                   'jack','queen', 'king']


    def __str__(self):
        return '{0} of {1}s'.format(PlayingCard.value_names[self.value],
                                    PlayingCard.suit_names[self.suit]
                                    )

    def short(self):
        shortName = '{0}{1}'.format(PlayingCard.value_names[self.value][0],
                                    PlayingCard.suit_names[self.suit][0]
                                    )
        return shortName


    def long(self):
        longName = '{0} of {1}s'.format(PlayingCard.value_names[self.value],
                                        PlayingCard.suit_names[self.suit]
                                        )
        return longName

card1 = PlayingCard(2, 5)

print(card1)
print(card1.short())
print(card1.long())

class TestPlayingCard(unittest.TestCase):

    def test_constructor(self, suit=3):
        self.name = self.__class__.__name__

    def test___str__(self):
        pass

    def test_short(self):

        self.asserTrue(short()= '2 of spades')


    def test_long(self):
        pass







if __name__ == '__main__':
    unittest.main()
