# SPDX-FileCopyrightText: 2021 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: MIT

import unittest
import sys
import logging
from word2numberi18n import w2n

class TestW2N(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestW2N, cls).setUpClass()
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)
        log = logging.getLogger("SYSTEM")
        log.info(f"Testsystem is {sys.implementation.name} v{sys.version_info.major}.{sys.version_info.minor}@{sys.platform}")


    def test_positives_en(self):
        instance = w2n.W2N(lang_param="sk")

        self.assertEqual(instance.word_to_num("devätnásť"), 19)
        self.assertEqual(instance.word_to_num("sto"), 100)
        self.assertEqual(instance.word_to_num("tisíc"), 1000)
        self.assertEqual(instance.word_to_num('tisíc jedna'), 1001)
        self.assertEqual(instance.word_to_num('tisíc jeden'), 1001)

    def test_negatives_es(self):
        instance = w2n.W2N(lang_param="sk")
        self.assertRaises(ValueError, instance.word_to_num, '112-')
        self.assertRaises(ValueError, instance.word_to_num, '-')
        self.assertRaises(ValueError, instance.word_to_num, 'on')

    def test_null_es(self):
        instance = w2n.W2N(lang_param="sk")
        noneValue :str = None
        self.assertRaises(ValueError, instance.word_to_num, noneValue)
        noneValue = ""
        self.assertRaises(ValueError, instance.word_to_num, noneValue)



if __name__ == '__main__':
    unittest.main()
