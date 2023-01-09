import unittest
import json
from word2number_es import w2n

general_test_data = json.load(open('nums.json'))

sentence_test_data = [(
    'A hundred and twelve years, two hundred and twenty-one days, thirteen hours, and twenty-two minutes',
    '112 years, 221 days, 13 hours, and 22 minutes'),
    ('4 hours, ten days, 7 minutes, 6 seconds', '4 hours, 10 days, 7 minutes, 6 seconds')]


class TestW2N(unittest.TestCase):
    def test_word_to_num_positives(self):
        print("testing numbers from 0 to 1000")
        for key, value in general_test_data.items():
            self.assertEqual(w2n.word_to_num(key), int(value))

        self.assertEqual(w2n.word_to_num('mil doscientos veintiuno'), 1221)

    def test_word_to_num_negatives(self):
        self.assertRaises(ValueError, w2n.word_to_num, '112-')
        self.assertRaises(ValueError, w2n.word_to_num, '-')
        self.assertRaises(ValueError, w2n.word_to_num, 'on')
        self.assertRaises(ValueError, w2n.word_to_num, 'millon millon')
        self.assertRaises(ValueError, w2n.word_to_num, 'tres millon millon')
        self.assertRaises(ValueError, w2n.word_to_num, 'millon cuatro millon')
        self.assertRaises(ValueError, w2n.word_to_num, 'mil millones')
        self.assertRaises(ValueError, w2n.word_to_num, 112)

    """
    def test_numwords_in_sentence(self):
        for datapoint in general_test_data:
            self.assertEqual(
                str(datapoint[1]), w2n.numwords_in_sentence(datapoint[0]))
        for datapoint in sentence_test_data:
            self.assertEqual(
                datapoint[1], w2n.numwords_in_sentence(datapoint[0]))"""


if __name__ == '__main__':
    unittest.main()
