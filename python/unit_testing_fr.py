# SPDX-FileCopyrightText: 2021 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: MIT

import unittest
import sys
import logging
import os

os.environ['w2n.lang'] = 'fr'

from word2numberi18n import w2n


class TestW2N(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(TestW2N, cls).setUpClass()
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)
        log = logging.getLogger("SYSTEM")
        log.info(f"Testsystem is {sys.implementation.name} v{sys.version_info.major}.{sys.version_info.minor}@{sys.platform}")

    
    def test_positives_fr(self):
        # test french
        self.assertEqual(w2n.word_to_num('trente-et-un'), 31)
        self.assertEqual(w2n.word_to_num('quatre-vingt-dix-neuf'), 99)
        self.assertEqual(w2n.word_to_num('cent'), 100)
        self.assertEqual(w2n.word_to_num('trois cent quatre-vingt sept mille cinq cent soixante-quatorze'),387574)
        self.assertEqual(w2n.word_to_num('six mille deux cent'), 6200)
        self.assertEqual(w2n.word_to_num(' un million six mille cent'), 1006100)
        self.assertEqual(w2n.word_to_num(' cinq milliard un million six mille cent'), 5001006100)
        self.assertEqual(w2n.word_to_num('neuf billion huit  milliard sept   million six mille cent'), 9008007006100)

        # test case for float values
        self.assertEqual(w2n.word_to_num('zero point zero un deux trois quatre cinq six sept huit neuf'), 0.0123456789)
        self.assertEqual(w2n.word_to_num('zero point zero un deux trois quatre cinq six sept huit neuf zero'), 0.0123456789)

    def test_negatives_fr(self):
        self.assertRaises(ValueError, w2n.word_to_num, 'on')


if __name__ == '__main__':
    unittest.main()
