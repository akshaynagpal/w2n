import unittest
from word2number_es import w2n

sentence_test_data = [
	(
		'mil años', '1000 años',
		'cien años', '100 años'
	),
	(
		'cuatro horas, diez dias, 7 minutos, seis segundos',
		'4 horas, 10 dias, 7 minutos, 6 segundos'
	),
	(
    'ciento doce años, doscientos veintiun dias, trece horas y dos minutos',
    '112 años, 221 dias, 13 horas y 2 minutos'
	),
	(
		'crea una alarma en cinco min',
		'crea una alarma en 5 min'
	),
	(
		"el reloj me costo diez mil pesos",
		"el reloj me costo 10000 pesos"
	),
	(
		"necesito cinco punto cinco litros de agua",
		"necesito 5.5 litros de agua"
	),
	(
		'punto cinco litros de agua',
		'0.5 litros de agua'
	),
	(
		'el señor donó dos millon novecientos noventa y dos mil pesos',
		'el señor donó 2992000 pesos'
	)
]

class TestW2N(unittest.TestCase):
	def test_nums_in_sentence(self):
		for datapoint in sentence_test_data:
			self.assertEqual(datapoint[1], w2n.numwords_in_sentence(datapoint[0]))