NUMBERS = {
    'cero': 0,
    'uno': 1,
    'dos': 2,
    'tres': 3,
    'cuatro': 4,
    'cinco': 5,
    'seis': 6,
    'siete': 7,
    'ocho': 8,
    'nueve': 9,
    'diez' : 10,
    'once' : 11,
    'doce' : 12,
    'trece' : 13,
    'catorce' : 14,
    'quince' : 15,
    'dieciseis' : 16,
    'diecisiete' : 17,
    'dieciocho' : 18,
    'diecinueve' : 19,
    'veinte': 20,
    'veintiuno': 21,
    'veintiun': 21,
    'veintidos': 22,
    'veintitres': 23,
    'veinticuatro': 24,
    'veinticinco': 25,
    'veintiseis': 26,
    'veintisiete': 27,
    'veintiocho': 28,
    'veintinueve': 29,
    'treinta': 30,
    'cuarenta': 40,
    'cincuenta': 50,
    'sesenta': 60,
    'setenta': 70,
    'ochenta': 80,
    'noventa': 90,
    'cien': 100,
    'ciento': 100,
    'doscientos': 200,
    'trescientos': 300,
    'cuatrocientos': 400,
    'quinientos': 500,
    'seiscientos': 600,
    'setecientos': 700,
    'ochocientos': 800,
    'novecientos': 900,
    'mil': 1000,
    'punto': '.'
}

SECTION_WORDS = ['quintillon', 'quatrillon', 'trillon', 'billon', 'millones', 'millon', 'mil']
ALL_SEPARATORS = SECTION_WORDS + ['punto']
NUMBER_WORDS = list(NUMBERS.keys()) + SECTION_WORDS + ['ciento']
NUMBER_SAFE_WORDS = NUMBER_WORDS + ['y', '&']
DECIMAL_WORDS = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']


def _number_formation(number_strings):
    """
    function to form numeric multipliers for million, billion, thousand etc.
    input: list of strings
    return value: integer
    """
    if not number_strings:
        return 1  # to correctly handle "a hundred and twelve", "thousand", etc
    hundred_index = number_strings.index('ciento') if 'ciento' in number_strings else -1
    number = 0
    if hundred_index >= 0:
        number = 100 * _number_formation(number_strings[0:hundred_index])
        number_strings = number_strings[hundred_index + 1:]
    number += sum([NUMBERS[word] for word in number_strings])
    return number


def _get_decimal_sum(decimal_digit_words):
    """
    function to convert post decimal digit words to numerial digits
    input: list of strings
    output: double
    """
    decimal_number_str = []
    for dec_word in decimal_digit_words:
        if dec_word not in DECIMAL_WORDS:
            return 0
        else:
            decimal_number_str.append(NUMBERS[dec_word])
    final_decimal_string = '0.' + ''.join(map(str, decimal_number_str))
    return float(final_decimal_string)


def normalize_accent_marks(word):
    """
    function to normalize accent marks
    input: string
    output: string
    """
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        word = word.replace(a, b).replace(a.upper(), b.upper())
    return word


def word_to_num(number_sentence):
    """
    function to return integer for an input `number_sentence` string
    input: string
    output: int or double or None
    """
    if type(number_sentence) is not str:
        raise ValueError(
            "Type of input is not string! Please enter a valid number word (eg. \'two million twenty three thousand and forty nine\')")

    # normalize accent marks
    number_sentence = normalize_accent_marks(number_sentence)

    if number_sentence.isdigit():  # return the number if user enters a number string
        return int(number_sentence)

    split_words = number_sentence.replace('-', ' ').replace(',', ' ').lower().split()

    # removing and, & etc.
    clean_numbers = [word for word in split_words if word in NUMBER_WORDS]

    return _clean_words_to_num(clean_numbers)


def numwords_in_sentence(sentence):
    if type(sentence) is not str:
        raise ValueError(
            "Type of input is not string! Please enter a valid number word (eg. \'two million twenty three thousand and forty nine\')")

    # TODO: some way to tell the difference between "one thousand, two hundred, and three" = 1203 and
    # TODO  "four, seven, twelve, three" = "4, 7, 12, 3"
    number_sentence = sentence.replace('-', ' ').replace(',', ' ').lower()

    split_words = number_sentence.strip().split()  # strip extra spaces and split sentence into words

    last_found_index = 0
    new_sentence = ''
    i = 0

    while i < len(split_words):
        if split_words[i] in NUMBER_WORDS:
            num_words = split_words[i - 1:i + 1] if i > 0 and split_words[i - 1] == 'a' else [split_words[i]]
            clean_words = [split_words[i]]
            while i + 1 < len(split_words) and split_words[i + 1] in NUMBER_SAFE_WORDS:
                i += 1
                num_words.append(split_words[i])
                if split_words[i] in NUMBER_WORDS:
                    clean_words.append(split_words[i])
            num = _clean_words_to_num(clean_words)
            replace_start, replace_end = _get_replaceable(number_sentence, num_words, last_found_index)
            new_sentence += sentence[last_found_index:replace_start] + str(num)
            last_found_index = replace_end
        i += 1

    new_sentence += sentence[last_found_index:]

    return new_sentence


def _get_replaceable(sentence, clean_words, last_found_index):
    start = sentence[last_found_index:].find(clean_words[0]) + last_found_index
    end = start + len(clean_words[0])
    for word in clean_words[1:]:
        end += sentence[end:].lower().find(word) + len(word)
    return start, end


def _validate_clean_words(clean_words):
    # Error message if the user enters invalid input!
    if len(clean_words) == 0:
        raise ValueError(
            "No number words were found in the string.")

        # Error if user enters million, billion, thousand or decimal punto twice
    if clean_words.count('mi') > 1 or clean_words.count('millon') > 1 or clean_words.count(
            'billion') > 1 or clean_words.count('punto') > 1:
        raise ValueError(
            "Redundant number word! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")

    separators = list(filter(lambda x: x in ALL_SEPARATORS, clean_words))
    sorted_seps = sorted(separators, key=lambda i: ALL_SEPARATORS.index(i))

    if sorted_seps != separators:
        raise ValueError(
            "Malformed number! Something is out of order here.")


def _clean_words_to_num(clean_words):
    _validate_clean_words(clean_words)
    clean_decimal_numbers = []

    # separate decimal part of number (if exists)
    if clean_words.count('punto') == 1:
        clean_decimal_numbers = clean_words[clean_words.index('punto') + 1:]
        clean_words = clean_words[:clean_words.index('punto')]

    total_sum = 0  # storing the number to be returned

    if len(clean_words) > 0:
        for word in SECTION_WORDS:
            word_index = clean_words.index(word) if word in clean_words else -1
            if word_index > -1:
                total_sum += _number_formation(clean_words[:word_index])
                clean_words = clean_words[word_index + 1:]
            total_sum *= 1000

        if clean_words:
            total_sum += _number_formation(clean_words)

    # adding decimal part to total_sum (if exists)
    if len(clean_decimal_numbers) > 0:
        decimal_sum = _get_decimal_sum(clean_decimal_numbers)
        total_sum += decimal_sum

    return total_sum