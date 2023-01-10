import unittest
import json
from word2number_es import w2n

general_test_data = json.load(open('test/nums.json'))

class TestW2N(unittest.TestCase):
    def test_word_to_num_positives(self):
        
        # testing numbers from 0 to 1000
        for key, value in general_test_data.items():
            self.assertEqual(w2n.word_to_num(key), int(value))

    def test_word_to_num_negatives(self):
        self.assertRaises(ValueError, w2n.word_to_num, '112-')
        self.assertRaises(ValueError, w2n.word_to_num, '-112')
        self.assertRaises(ValueError, w2n.word_to_num, '-')
        self.assertRaises(ValueError, w2n.word_to_num, 'on')
        self.assertRaises(ValueError, w2n.word_to_num, 'millon millon')
        self.assertRaises(ValueError, w2n.word_to_num, 'tres millon millon')
        self.assertRaises(ValueError, w2n.word_to_num, 'millon cuatro millon')
        self.assertRaises(ValueError, w2n.word_to_num, 'mil millones')
        self.assertRaises(ValueError, w2n.word_to_num, 112)