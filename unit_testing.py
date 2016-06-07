import unittest
from word2number import w2n

class TestW2N(unittest.TestCase):

	def test_output(self):
		self.assertEqual(w2n.word_to_num("two million three thousand nine hundred and eighty four"),2003984)
		self.assertEqual(w2n.word_to_num("nineteen"),19)
		self.assertEqual(w2n.word_to_num('three billion'),3000000000)
		self.assertEqual(w2n.word_to_num('three million'),3000000)
		self.assertEqual(w2n.word_to_num('one hundred twenty three million four hundred fifty six thousand seven hundred and eighty nine')
,123456789)
		self.assertEqual(w2n.word_to_num('eleven'),11)
		self.assertEqual(w2n.word_to_num('nineteen billion and nineteen'),19000000019)
		self.assertEqual(w2n.word_to_num('one hundred and forty two'),142)
		self.assertEqual(w2n.word_to_num('one hundred thirty-five'),135)

if __name__ == '__main__':
	unittest.main()
