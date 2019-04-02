import unittest
from word2number import w2n


class TestW2N(unittest.TestCase):
    def test_word_to_num_positives(self):
        self.assertEqual(w2n.word_to_num("two million three thousand nine hundred and eighty four"), 2003984)
        self.assertEqual(w2n.word_to_num("nineteen"), 19)
        self.assertEqual(w2n.word_to_num("two thousand and nineteen"), 2019)
        self.assertEqual(w2n.word_to_num("two million three thousand and nineteen"), 2003019)
        self.assertEqual(w2n.word_to_num('three billion'), 3000000000)
        self.assertEqual(w2n.word_to_num('three million'), 3000000)
        self.assertEqual(w2n.word_to_num('one hundred twenty three million four hundred fifty six thousand seven hundred and eighty nine')
, 123456789)
        self.assertEqual(w2n.word_to_num('eleven'), 11)
        self.assertEqual(w2n.word_to_num('nineteen billion and nineteen'), 19000000019)
        self.assertEqual(w2n.word_to_num('one hundred and forty two'), 142)
        self.assertEqual(w2n.word_to_num('112'), 112)
        self.assertEqual(w2n.word_to_num('11211234'), 11211234)
        self.assertEqual(w2n.word_to_num('five'), 5)
        self.assertEqual(w2n.word_to_num('two million twenty three thousand and forty nine'), 2023049)
        self.assertEqual(w2n.word_to_num('two point three'), 2.3)
        self.assertEqual(w2n.word_to_num('two million twenty three thousand and forty nine point two three six nine'), 2023049.2369)
        self.assertEqual(w2n.word_to_num('one billion two million twenty three thousand and forty nine point two three six nine'), 1002023049.2369)
        self.assertEqual(w2n.word_to_num('point one'), 0.1)
        self.assertEqual(w2n.word_to_num('point'), 0)
        self.assertEqual(w2n.word_to_num('point nineteen'), 0)
        self.assertEqual(w2n.word_to_num('one hundred thirty-five'), 135)
        self.assertEqual(w2n.word_to_num('hundred'), 100)
        self.assertEqual(w2n.word_to_num('thousand'), 1000)
        self.assertEqual(w2n.word_to_num('million'), 1000000)
        self.assertEqual(w2n.word_to_num('billion'), 1000000000)
        self.assertEqual(w2n.word_to_num('nine point nine nine nine'), 9.999)
        self.assertEqual(w2n.word_to_num('seventh point nineteen'), 0)

    def test_word_to_num_negatives(self):
        self.assertRaises(ValueError, w2n.word_to_num, '112-')
        self.assertRaises(ValueError, w2n.word_to_num, '-')
        self.assertRaises(ValueError, w2n.word_to_num, 'on')
        self.assertRaises(ValueError, w2n.word_to_num, 'million million')
        self.assertRaises(ValueError, w2n.word_to_num, 'three million million')
        self.assertRaises(ValueError, w2n.word_to_num, 'million four million')
        self.assertRaises(ValueError, w2n.word_to_num, 'thousand million')
        self.assertRaises(ValueError, w2n.word_to_num, 'one billion point two million twenty three thousand and forty nine point two three six nine')
        self.assertRaises(ValueError, w2n.word_to_num, 112)

    def test_num_to_word_positives(self):
        self.assertEqual(w2n.num_to_word(2003984), "two million three thousand nine hundred eighty four")
        self.assertEqual(w2n.num_to_word(19), "nineteen")
        self.assertEqual(w2n.num_to_word(2019), "two thousand nineteen")
        self.assertEqual(w2n.num_to_word(2003019), "two million three thousand nineteen")
        self.assertEqual(w2n.num_to_word(3000000000), 'three billion')
        self.assertEqual(w2n.num_to_word(3000000), 'three million')
        self.assertEqual(w2n.num_to_word(9.999), 'nine point nine nine nine')
        self.assertEqual(w2n.num_to_word(0), 'zero')
        self.assertEqual(1002023049.24, w2n.word_to_num(w2n.num_to_word(1002023049.24)))

    def test_num_to_word_negatives(self):
        self.assertRaises(ValueError, w2n.num_to_word, '112')
        self.assertRaises(ValueError, w2n.num_to_word, ['fifty'])
        self.assertRaises(ValueError, w2n.num_to_word, True)

if __name__ == '__main__':
    unittest.main()
