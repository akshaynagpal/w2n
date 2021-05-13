import unittest
from word2number import w2n


class TestW2N(unittest.TestCase):
    def test_positives(self):
        # Boring normal-people numbers
        self.assertEqual(w2n.word_to_num('five'), 5)
        self.assertEqual(w2n.word_to_num('eleven'), 11)
        self.assertEqual(w2n.word_to_num('hundred'), 100)
        self.assertEqual(w2n.word_to_num('thousand'), 1000)
        self.assertEqual(w2n.word_to_num('million'), 1000000)
        self.assertEqual(w2n.word_to_num('billion'), 1000000000)
        self.assertEqual(w2n.word_to_num('two million three thousand nine hundred and eighty four'), 2003984)
        self.assertEqual(w2n.word_to_num('two thousand and nineteen'), 2019)
        self.assertEqual(w2n.word_to_num('two million three thousand and nineteen'), 2003019)
        self.assertEqual(w2n.word_to_num('three billion'), 3000000000)
        self.assertEqual(w2n.word_to_num('three million'), 3000000)
        self.assertEqual(w2n.word_to_num('three hundred thousand'), 300000)
        self.assertEqual(w2n.word_to_num('one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine'), 123456789)
        self.assertEqual(w2n.word_to_num('two million twenty three thousand and forty nine'), 2023049)
        
        # Handling metric suffixes
        self.assertEqual(w2n.word_to_num('$150k'), 150000)
        self.assertEqual(w2n.word_to_num('310 M'), 310000000)
        
        # Minus/negative
        self.assertEqual(w2n.word_to_num('negative ten'), -10)
        self.assertEqual(w2n.word_to_num('-10'), -10)
        self.assertEqual(w2n.word_to_num('minus 10'), -10)
        self.assertEqual(w2n.word_to_num('minus ten point five'), -10.5)
        self.assertEqual(w2n.word_to_num('minus point five'), -0.5)
        
        # Excess spaces testing
        self.assertEqual(w2n.word_to_num('nineteen'), 19)
        self.assertEqual(w2n.word_to_num(' nineteen'), 19)
        self.assertEqual(w2n.word_to_num('nineteen '), 19)
        self.assertEqual(w2n.word_to_num('nineteen   '), 19)
        
        # Excess punctuation testing
        self.assertEqual(w2n.word_to_num('nineteen;'), 19)
        self.assertEqual(w2n.word_to_num('nineteen,'), 19)
        self.assertEqual(w2n.word_to_num('nineteen.'), 19)
        self.assertEqual(w2n.word_to_num('19;'), 19)
        self.assertEqual(w2n.word_to_num('19,'), 19)
        self.assertEqual(w2n.word_to_num('19.'), 19)
        self.assertEqual(w2n.word_to_num('$19'), 19)
        self.assertEqual(w2n.word_to_num('19 ;'), 19)
        self.assertEqual(w2n.word_to_num('19 ,'), 19)
        self.assertEqual(w2n.word_to_num('$ 19'), 19)
        
        # Joining words/symbols
        self.assertEqual(w2n.word_to_num('nineteen billion and nineteen'), 19000000019)
        self.assertEqual(w2n.word_to_num('one hundred and forty two'), 142)
        self.assertEqual(w2n.word_to_num('one hundred & forty two'), 142)
        self.assertEqual(w2n.word_to_num('one hundred thirty-five'), 135)
        self.assertEqual(w2n.word_to_num('six-four'), 64)
        
        # Handling regular digits alone
        self.assertEqual(w2n.word_to_num('112'), 112)
        self.assertEqual(w2n.word_to_num('11211234'), 11211234)
        self.assertEqual(w2n.word_to_num('2.3'), 2.3)
        
        # Handling decimals
        self.assertEqual(w2n.word_to_num('two point three'), 2.3)
        self.assertEqual(w2n.word_to_num('two point thirteen'), 2.13)
        self.assertEqual(w2n.word_to_num('nine point nine nine nine'), 9.999)
        self.assertEqual(w2n.word_to_num('two million twenty three thousand and forty nine point two three six nine'), 2023049.2369)
        self.assertEqual(w2n.word_to_num('one billion two million twenty three thousand and forty nine point two three six nine'), 1002023049.2369)
        self.assertEqual(w2n.word_to_num('1 billion 2 million 23 thousand and 49.2369'), 1002023049.2369)
        # I don't even know if this should be allowed, but it works so we'll go with it
        self.assertEqual(w2n.word_to_num('one.one'), 1.1)
        
        # Handling decimals as multipliers
        self.assertEqual(w2n.word_to_num('four point nine million'), 4900000)
        self.assertEqual(w2n.word_to_num('1.3 thousand'), 1300)
        
        # Handling ommitted expected terms
        self.assertEqual(w2n.word_to_num('hundred twenty'), 120)
        self.assertEqual(w2n.word_to_num('point one'), 0.1)
        self.assertEqual(w2n.word_to_num('point nineteen'), 0.19)
        self.assertEqual(w2n.word_to_num('thousand million'), 1000000000)
        
        # Handling spelling out numbers by digit
        self.assertEqual(w2n.word_to_num('one niner niner'), 199)
        self.assertEqual(w2n.word_to_num('minus one niner niner'), -199)
        self.assertEqual(w2n.word_to_num('four four eight seven eight'), 44878)
        self.assertEqual(w2n.word_to_num('four four eight seven eight point eight nine'), 44878.89)
        
        # Less common number names
        self.assertEqual(w2n.word_to_num('two dozen'), 24)
        self.assertEqual(w2n.word_to_num('a gross'), 144)
        self.assertEqual(w2n.word_to_num('four score and seven'), 87)
        self.assertEqual(w2n.word_to_num('naught point five'), 0.5)
        self.assertEqual(w2n.word_to_num('two naught one one'), 2011)
        self.assertEqual(w2n.word_to_num('one decimal niner'), 1.9)
        self.assertEqual(w2n.word_to_num('zero eight five decimal niner'), 85.9)
        self.assertEqual(w2n.word_to_num('one zero eight five decimal niner'), 1085.9)
        
        # Testing the boring indexing method
        self.assertEqual(w2n.num_word_indices('zero one two three four five six seven'), [ 0, 1, 2, 3, 4, 5, 6, 7 ])
        self.assertEqual(w2n.num_word_indices('four'), [ 0 ])
        self.assertEqual(w2n.num_word_indices('fourteen rats and three mice'), [ 0, 3 ])
        self.assertEqual(w2n.num_word_indices('1.5 rats (ew!) and -2 mice'), [ 0, 4 ])
        self.assertEqual(w2n.num_word_indices('Who wants to win $150,000'), [ 4 ])
        self.assertEqual(w2n.num_word_indices('There are no numbers in this sentence'), [ ])

    def test_negatives(self):
        self.assertRaises(ValueError, w2n.word_to_num, 'seventh point nineteen')
        self.assertRaises(ValueError, w2n.word_to_num, '19 calculators')
        self.assertRaises(ValueError, w2n.word_to_num, '-')
        self.assertRaises(ValueError, w2n.word_to_num, '19-')
        self.assertRaises(ValueError, w2n.word_to_num, '19 minus')
        self.assertRaises(ValueError, w2n.word_to_num, 'minus -10')
        self.assertRaises(ValueError, w2n.word_to_num, 'on')
        self.assertRaises(ValueError, w2n.word_to_num, 'million four million')
        self.assertRaises(ValueError, w2n.word_to_num, 'million million')
        self.assertRaises(ValueError, w2n.word_to_num, 'million million.')
        self.assertRaises(ValueError, w2n.word_to_num, 'million. million.')
        self.assertRaises(ValueError, w2n.word_to_num, 'million & million')
        self.assertRaises(ValueError, w2n.word_to_num, 'three million million')
        self.assertRaises(ValueError, w2n.word_to_num, 'one billion point two million twenty three thousand and forty nine point two three six nine')
        self.assertRaises(ValueError, w2n.word_to_num, 'one decimal niner decimal eight')
        self.assertRaises(ValueError, w2n.word_to_num, 'zero point eight five decimal niner')
        self.assertRaises(ValueError, w2n.word_to_num, 112)
        self.assertRaises(ValueError, w2n.word_to_num, False)
        self.assertRaises(ValueError, w2n.word_to_num, 'point')
        self.assertRaises(ValueError, w2n.word_to_num, '.')

if __name__ == '__main__':
    unittest.main()
