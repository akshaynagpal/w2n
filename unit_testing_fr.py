# SPDX-FileCopyrightText: 2021 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: MIT

import unittest
import os

os.environ ['w2n.lang'] = 'fr'

from word2numberi18n import w2n


class TestW2N(unittest.TestCase):
    def test_positives_fr(self):
        # test french
        self.assertEqual(w2n.word_to_num('trente-et-un'), 31)
        self.assertEqual(w2n.word_to_num('quatre-vingt-dix-neuf'), 99)

    def test_negatives_fr(self):
        self.assertRaises(ValueError, w2n.word_to_num, 'on')

if __name__ == '__main__':
    unittest.main()


