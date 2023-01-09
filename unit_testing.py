import unittest
from word2number_es import w2n

# numeros del cero al cien
numeros = {'cero': 0, 'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5, 'seis': 6, 'siete': 7, 'ocho': 8, 'nueve': 9, 'diez': 10, 'once': 11, 'doce': 12, 'trece': 13, 'catorce': 14, 'quince': 15, 'dieciséis': 16, 'diecisiete': 17, 'dieciocho': 18, 'diecinueve': 19, 'veinte': 20, 'veintiuno': 21, 'veintidós': 22, 'veintitrés': 23, 'veinticuatro': 24, 'veinticinco': 25, 'veintiséis': 26, 'veintisiete': 27, 'veintiocho': 28, 'veintinueve': 29, 'treinta': 30, 'treinta y uno': 31, 'treinta y dos': 32, 'treinta y tres': 33, 'treinta y cuatro': 34, 'treinta y cinco': 35, 'treinta y seis': 36, 'treinta y siete': 37, 'treinta y ocho': 38, 'treinta y nueve': 39, 'cuarenta': 40, 'cuarenta y uno': 41, 'cuarenta y dos': 42, 'cuarenta y tres': 43, 'cuarenta y cuatro': 44, 'cuarenta y cinco': 45, 'cuarenta y seis': 46, 'cuarenta y siete': 47, 'cuarenta y ocho': 48, 'cuarenta y nueve': 49, 'cincuenta': 50, 'cincuenta y uno': 51, 'cincuenta y dos': 52, 'cincuenta y tres': 53, 'cincuenta y cuatro': 54, 'cincuenta y cinco': 55, 'cincuenta y seis': 56, 'cincuenta y siete': 57, 'cincuenta y ocho': 58, 'cincuenta y nueve': 59, 'sesenta': 60, 'sesenta y uno': 61, 'sesenta y dos': 62, 'sesenta y tres': 63, 'sesenta y cuatro': 64, 'sesenta y cinco': 65, 'sesenta y seis': 66, 'sesenta y siete': 67, 'sesenta y ocho': 68, 'sesenta y nueve': 69, 'setenta': 70, 'setenta y uno': 71, 'setenta y dos': 72, 'setenta y tres': 73, 'setenta y cuatro': 74, 'setenta y cinco': 75, 'setenta y seis': 76, 'setenta y siete': 77, 'setenta y ocho': 78, 'setenta y nueve': 79, 'ochenta': 80, 'ochenta y uno': 81, 'ochenta y dos': 82, 'ochenta y tres': 83, 'ochenta y cuatro': 84, 'ochenta y cinco': 85, 'ochenta y seis': 86, 'ochenta y siete': 87, 'ochenta y ocho': 88, 'ochenta y nueve': 89, 'noventa': 90, 'noventa y uno': 91, 'noventa y dos': 92, 'noventa y tres': 93, 'noventa y cuatro': 94, 'noventa y cinco': 95, 'noventa y seis': 96, 'noventa y siete': 97, 'noventa y ocho': 98, 'noventa y nueve': 99, 'cien': 100}

# numeros del doscientos al novecientos
doscientos = {
    "doscientos": 200,
    "doscientos uno": 201,
    "doscientos dos": 202,
    "doscientos tres": 203,
    "doscientos cuatro": 204,
    "doscientos cinco": 205,
    "doscientos seis": 206,
    "doscientos siete": 207,
    "doscientos ocho": 208,
    "doscientos nueve": 209,
    "doscientos diez": 210,
    "doscientos once": 211,
    "doscientos doce": 212,
    "doscientos trece": 213,
    "doscientos catorce": 214,
    "doscientos quince": 215,
    "doscientos dieciseis": 216,
    "doscientos diecisiete": 217,
    "doscientos dieciocho": 218,
    "doscientos diecinueve": 219,
    "doscientos veinte": 220,
    "doscientos veintiuno": 221,
    "doscientos veintidos": 222,
    "doscientos veintitres": 223,
    "doscientos veinticuatro": 224,
    "doscientos veinticinco": 225,
    "doscientos veintiseis": 226,
    "doscientos veintisiete": 227,
    "doscientos veintiocho": 228,
    "doscientos veintinueve": 229,
    "doscientos treinta": 230,
    "doscientos treinta y uno": 231,

   
}


class TestW2N(unittest.TestCase):
    def test_base(self):

        print("testing numbers from 0 to 100")
        for key, value in numeros.items():
            self.assertEqual(w2n.word_to_num(key), int(value))
        
        print("testing numbers from 200 to 299")
        for k, v in doscientos.items():
            self.assertEqual(w2n.word_to_num(k), v)


    def test_tens(self):
        self.assertEqual(w2n.word_to_num('treinta'), 30)
        self.assertEqual(w2n.word_to_num('treinta y uno'), 31)
        self.assertEqual(w2n.word_to_num('cuarenta'), 40)
        self.assertEqual(w2n.word_to_num('cuarenta y uno'), 41)
        self.assertEqual(w2n.word_to_num('cincuenta'), 50)
        self.assertEqual(w2n.word_to_num('cincuenta y uno'), 51)

        self.assertEqual(w2n.word_to_num('sesenta y uno'), 61)
        self.assertEqual(w2n.word_to_num('setenta'), 70)
        self.assertEqual(w2n.word_to_num('setenta y uno'), 71)
        self.assertEqual(w2n.word_to_num('ochenta'), 80)
        self.assertEqual(w2n.word_to_num('ochenta y uno'), 81)
        self.assertEqual(w2n.word_to_num('noventa'), 90)
        self.assertEqual(w2n.word_to_num('noventa y uno'), 91)


    """def test_negatives(self):
        self.assertRaises(ValueError, w2n.word_to_num, '112-')
        self.assertRaises(ValueError, w2n.word_to_num, '-')
        self.assertRaises(ValueError, w2n.word_to_num, 'on')
        self.assertRaises(ValueError, w2n.word_to_num, 'million million')
        self.assertRaises(ValueError, w2n.word_to_num, 'three million million')
        self.assertRaises(ValueError, w2n.word_to_num, 'million four million')
        self.assertRaises(ValueError, w2n.word_to_num, 'thousand million')
        self.assertRaises(ValueError, w2n.word_to_num, 'one billion point two million twenty three thousand and forty nine point two three six nine')
        self.assertRaises(ValueError, w2n.word_to_num, 112)"""

if __name__ == '__main__':
    unittest.main()
