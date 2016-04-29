import unittest
class PlayingCard:
    """creates a playing card with (suit, value)"""
    def __init__ (self, suit=0, value=2):
        self.suit = suit
        self.value = value


    suit_names = ('heart', 'diamond', 'spade', 'club')
    values = {'ace': 'ace',
              '2': 'two',
              '3': 'three',
              '4': 'four',
              '5': 'five',
              '6': 'six',
              '7': 'seven',
              '8': 'eight',
              '9': 'nine',
              '10': 'ten',
              'queen': 'queen',
              'king': 'king',
              'jack': 'jack'}


    def __str__(self):
        return '{0} of {1}s'.format(PlayingCard.value_names[self.value],
                                    PlayingCard.suit_names[self.suit])

    def short(self):
        shortName = '{0}{1}'.format(PlayingCard.value_names[self.value][0],
                                    PlayingCard.suit_names[self.suit][0])
        return shortName


    def long(self):
        longName = '{0} of {1}s'.format(PlayingCard.value_names[self.value],
                                        PlayingCard.suit_names[self.suit])
        return longName

card1 = PlayingCard(2, 5)

print(card1)
print(card1.short())
print(card1.long())

class TestPlayingCard(unittest.TestCase):

    def test_suits(self):
        self.name = self.__class__.__name__
        self.assertEqual(4, len(PlayingCard.suits))
        self.assertTrue('hearts' in PlayingCard.suits)
        self.assertFalse('weasels' in PlayingCard.suits)

    def test_values(self):
        self.assertEqual(13, len(PlayingCard.values))
        self.assertTrue('9' in PlayingCard.values)
        self.assertTrue('21' not in PlayingCard.values)

    def test_Init(self):
        pc1 = PlayingCard('ace', 'hearts')
        self.assertEqual('ace', pc1.value)
        self.assertEqual('hearts', pc1.suit)
        with self.assertRaises(TypeError):
            pc2 = PlayingCard()

        with self.assertRaises(AttributeError):
            pc3 = PlayingCard('duke', 'earl')


    def test_Short_Name(self):
        pc1 = PlayingCard('9', 'clubs')
        self.assertEqual('9C', pc1.shortName())

    def test_Long_Name(self):
        pc = PlayingCard('10', 'hearts')
        self.assertEqual('ten of hearts', pc.longName())







if __name__ == '__main__':
    unittest.main()
