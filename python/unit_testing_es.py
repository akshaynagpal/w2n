# SPDX-FileCopyrightText: 2016 - Akshay Nagpal <akshaynagpal@user.noreplay.github.com>
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
    
    
    def test_positives_es(self):
        instance = w2n.W2N(lang_param="es")
        
        self.assertEqual(instance.word_to_num("dos millones tres mil novecientos ochenta y cuatro"), 2003984)
        self.assertEqual(instance.word_to_num("diecinueve"), 19)
        self.assertEqual(instance.word_to_num("dos mil diecinueve"), 2019)
        self.assertEqual(instance.word_to_num("dos millones tres mil diecinueve"), 2003019)
        self.assertEqual(instance.word_to_num('tres mil millones'), 3000000000)
        self.assertEqual(instance.word_to_num('tres millones'), 3000000)
        self.assertEqual(instance.word_to_num('ciento veintitres millones cuatro cientos cincuenta y seis mil setecientos ochenta y nueve'), 123456789)
        self.assertEqual(instance.word_to_num('once'), 11)
        self.assertEqual(instance.word_to_num('diecinueve mil millones diecinueve'), 19000000019)
        self.assertEqual(instance.word_to_num('ciento cuarenta y dos'), 142)
        self.assertEqual(instance.word_to_num('cinco'), 5)
        self.assertEqual(instance.word_to_num('dos millones veintitres mil cuarenta y nueve'), 2023049)
        self.assertEqual(instance.word_to_num('dos coma tres'), 2.3)
        self.assertEqual(instance.word_to_num('dos millones veintitres mil cuarenta y nueve coma dos tres seis nueve'), 2023049.2369)
        self.assertEqual(instance.word_to_num('mil millones dos millones veintitres mil cuarenta y nueve coma dos tres seis nueve'), 1002023049.2369)
        self.assertEqual(instance.word_to_num('cero coma uno'), 0.1)
        self.assertEqual(instance.word_to_num('coma'), 0)
        self.assertEqual(instance.word_to_num('ciento treinta y cinco'), 135)
        self.assertEqual(instance.word_to_num('cien'), 100)
        self.assertEqual(instance.word_to_num('mil'), 1000)
        self.assertEqual(instance.word_to_num('un millon'), 1000000)
        self.assertEqual(instance.word_to_num('mil millones'), 1000000000)

    def test_negatives_es(self):
        instance = w2n.W2N(lang_param="es")
        self.assertRaises(ValueError, instance.word_to_num, '112-')
        self.assertRaises(ValueError, instance.word_to_num, '-')
        self.assertRaises(ValueError, instance.word_to_num, 'on')

    def test_null_es(self):
        instance = w2n.W2N(lang_param="es")
        noneValue :str = None 
        self.assertRaises(ValueError, instance.word_to_num, noneValue)
        noneValue = ""
        self.assertRaises(ValueError, instance.word_to_num, noneValue)


if __name__ == '__main__':
    unittest.main()
