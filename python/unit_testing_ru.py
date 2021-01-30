# SPDX-FileCopyrightText: 2016 - Akshay Nagpal <akshaynagpal@user.noreplay.github.com>
# SPDX-FileCopyrightText: 2021 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: MIT

import unittest
import os

os.environ['w2n.lang'] = 'ru'

from word2numberi18n import w2n


class TestW2N(unittest.TestCase):
    def test_positives_ru(self):
        self.assertEqual(w2n.word_to_num('две целых три десятых'), 2.3)
        self.assertEqual(w2n.word_to_num("два миллиона три тысячи девятьсот восемьдесят четыре"), 2003984)
        self.assertEqual(w2n.word_to_num('сто двенадцать'), 112)
        self.assertEqual(w2n.word_to_num('сто тридцать-пять'), 135)

    def test_negatives_ru(self):
        self.assertRaises(ValueError, w2n.word_to_num, '112-')
        self.assertRaises(ValueError, w2n.word_to_num, '-')
        self.assertRaises(ValueError, w2n.word_to_num, 'бля')
        self.assertRaises(ValueError, w2n.word_to_num, 'миллион миллион')
        self.assertRaises(ValueError, w2n.word_to_num, 112)


if __name__ == '__main__':
    unittest.main()
