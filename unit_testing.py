import unittest
from word2number import w2n


class TestW2N(unittest.TestCase):
    def test_positives(self):
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

    def test_leading_scale_words(self):
        # Reproduction tests for Issue #13:
        # Scale words without explicit leading "one" must not crash with IndexError
        self.assertEqual(w2n.word_to_num("thousand and five"), 1005)
        self.assertEqual(w2n.word_to_num("thousand twenty"), 1020)
        self.assertEqual(w2n.word_to_num("million and ten"), 1000010)
        self.assertEqual(w2n.word_to_num("billion and one"), 1000000001)

    def test_hundred_prefixed_addition(self):
        # Scale word 'hundred' followed by smaller numbers must add, not multiply
        self.assertEqual(w2n.word_to_num("hundred and five"), 105)
        self.assertEqual(w2n.word_to_num("hundred and twenty"), 120)

    def test_boundary_and_compound_scales(self):
        # Comprehensive boundary tests for compound scale combinations
        self.assertEqual(w2n.word_to_num("thousand and ninety nine"), 1099)
        self.assertEqual(w2n.word_to_num("million two thousand and fifty"), 1002050)
        self.assertEqual(w2n.word_to_num("billion and one hundred"), 1000000100)
        self.assertEqual(w2n.word_to_num("hundred twenty five"), 125)
        self.assertEqual(w2n.word_to_num("hundred and one"), 101)
        self.assertEqual(w2n.word_to_num("thousand and one"), 1001)
        self.assertEqual(w2n.word_to_num("million and one"), 1000001)

    def test_decimal_with_leading_scales(self):
        # Decimals combined with scale words
        self.assertEqual(w2n.word_to_num("thousand point five"), 1000.5)
        self.assertEqual(w2n.word_to_num("hundred and five point two"), 105.2)
        self.assertEqual(w2n.word_to_num("million point zero five"), 1000000.05)

    def test_boundary_error_handling(self):
        # Ensure invalid inputs strictly continue to raise ValueError
        self.assertRaises(ValueError, w2n.word_to_num, "")
        self.assertRaises(ValueError, w2n.word_to_num, "   ")
        self.assertRaises(ValueError, w2n.word_to_num, "random text with no numbers")
        self.assertRaises(ValueError, w2n.word_to_num, "million billion")

    def test_negatives(self):
        self.assertRaises(ValueError, w2n.word_to_num, '112-')
        self.assertRaises(ValueError, w2n.word_to_num, '-')
        self.assertRaises(ValueError, w2n.word_to_num, 'on')
        self.assertRaises(ValueError, w2n.word_to_num, 'million million')
        self.assertRaises(ValueError, w2n.word_to_num, 'three million million')
        self.assertRaises(ValueError, w2n.word_to_num, 'million four million')
        self.assertRaises(ValueError, w2n.word_to_num, 'thousand million')
        self.assertRaises(ValueError, w2n.word_to_num, 'one billion point two million twenty three thousand and forty nine point two three six nine')
        self.assertRaises(ValueError, w2n.word_to_num, 112)

if __name__ == '__main__':
    unittest.main()
