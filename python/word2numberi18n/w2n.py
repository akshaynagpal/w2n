# SPDX-FileCopyrightText: 2020-2021 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: MIT

"""
"""


import os
import locale
import codecs
import re

number_system = {}
normalize_data = {}
sorted_measure_values = []# = [1_000_000_000_000,1_000_000_000,1_000_000,1_000,100]

lang = "en"

# first get programming language specific local spoken language
lang = locale.getlocale()[0]
if "w2n.lang" in os.environ:
    lang = os.environ["w2n.lang"]
if lang is None:
    lang = locale.getdefaultlocale()[0]
if lang is None or lang[0] is None:
    lang = None
    if "LANGUAGE" in os.environ:
        lang = os.environ["LANGUAGE"]
if lang is None:
    lang = "en"  # fallback
lang = lang[:2]

# Now analyse the configuration file for the local spoken language
data_file = os.path.dirname(__file__)+os.sep+"data"+os.sep+"config_"+lang+".properties"
with codecs.open(data_file, "rU", encoding="utf-8") as number_system_data:
    for line in number_system_data:
        if line.startswith('#'):
            pass
        else:
            (key, val) = line.split("=")
            if key.startswith("replace:"):
                key =key[len("replace:"):]
                normalize_data[key] = val.strip()
            elif key.startswith("measure:"):
                sorted_measure_values.append(int(val.strip()))
            else:
                if "point" != key:
                    val = int(val)
                else:
                    val = val.strip()
                number_system[key] = val

sorted_measure_values = sorted(sorted_measure_values,reverse=True)
decimal_words = list(number_system.keys())[:10]


def number_formation(number_words):
    """ [internal] function to form numeric multipliers
    
    input: list of strings
    return value: integer
    """
    digit_values = []
    # calculate the three digit values (max)
    for word in number_words:
        next_number_candidat = number_system[word]
        digit_values.append(next_number_candidat)
    hundred_index = digit_values.count(100)
    hundred_index = digit_values.index(100) if 100 in digit_values else -1
    if hundred_index == 1:
        digit_values[0] = digit_values[0] * digit_values[1] # this is like other languages need to do it
        del digit_values[1]
    if len(digit_values) > 3 and digit_values[0] < 100:
        digit_values[0] *= digit_values[1]
        del digit_values[1]
    elif len(digit_values) > 3 and digit_values[0] > 100:
        digit_values[1] *= digit_values[2]
        del digit_values[2]
    # add the three digits
    while len(digit_values) > 1:
        digit_values[0] += digit_values[1]
        del digit_values[1]
    # return the result
    return digit_values[0]


def get_decimal_string(decimal_digit_words):
    """ [internal] function to convert post decimal digit words to numerial digits
    it returns a string to prevert from floating point conversation problem
    
    input: list of strings
    output: string
    """
    decimal_number_str = []
    for dec_word in decimal_digit_words:
        if(dec_word not in decimal_words):
            return 0
        else:
            decimal_number_str.append(number_system[dec_word])
    final_decimal_string = ''.join(map(str, decimal_number_str))
    return final_decimal_string


def normalize(number_sentence):
    """ [internal] function to normalize the whole(!) input text
    note: float or int parameters are allowed 
    
    input: string the full text
    output: string
    """
    # we need no check for numbers...
    if type(number_sentence) is float:
        return number_sentence
    if type(number_sentence) is int:
        return number_sentence

    # ...but if it is a string we need normalizing
    number_sentence = number_sentence.lower()  # converting input to lowercase

    # for examples: both is right "vingt et un" and "vingt-et-un"
    # we change this to composed value "vingt-et-un" over the localized data file "replace:" entry
    for non_composed_number_value, composed_number_value in normalize_data.items():
        if non_composed_number_value.count(' ') >1:
            number_sentence = number_sentence.replace(non_composed_number_value, composed_number_value)

    return number_sentence.strip()


def check_double_input (new_number, clean_numbers):
    """ [internal] function to check false redundant input
    note: this method has language configuration dependency
    
    note: call this after lemma text
    
    example: check_double_input (1000, "thousand thousand") with lang="en" throws a ValueError
    example: check_double_input (1000, "thousand thousand") with lang="de" its ok
    example: check_double_input (1000, "tausend tausend") with lang="de" throws a ValueError
    
    input: int new_number, string[] words - looking for count of localized name of new_numerb in words     
    raise: if redundant input error
    """
    localized_name = get_name_by_number_value(new_number)
    countGreaterOne = clean_numbers.count(localized_name) > 1  # in result of same logic like Java extra step insert
    if countGreaterOne:
        raise ValueError(f"Redundant number word {localized_name} in! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")
        # i18n save für later:
        # de: "Redundantes Nummernwort! Bitte gebe ein zulässiges Nummernwort ein (z.B. zwei Millionen Dreiundzwanzigtausend und Neunundvierzig)"
        # ru: "Избыточное числовое слово! Введите правильное числовое слово (например, два миллиона двадцать три тысячи сорок девять)" 


def get_name_by_number_value (new_number):
    """ [internal] function to get the localized name form value
    
    input: numeric value
    output: name from language configuration or None if not found 
    """
    for number_name, number_value in number_system.items():
        if new_number == number_value:
            return number_name
    return None


def get_index_for_number(new_number, clean_numbers):
    """ [internal] function to get the index of name for given number 
        note: call this after lemma text

        input: int number
        output: index or -1 if not found
    
    """
    # in result of get name by numeric value, the localized name came from dictionary
    # and we need no language specific code
    localized_name = get_name_by_number_value(new_number)
    return clean_numbers.index(localized_name) if localized_name in clean_numbers else -1


def get_number_value (clean_numbers):
    """ [internal] function to get the pre-decimal number from clean_number
    
        input: sorted array with number words
        output: int number
        raise: ValueError 
    """
    result = 0

    #
    # The simple algorithm based on the idea from NLP to work with tagging (key)words
    # but yes it is handmade implemented today.
    #
    # -- 2021-02-05 --
    # The tagging can be tested on for example https://parts-of-speech.info and tell for
    # nine trillion one billion two million twenty three thousand and forty nine point two three six nine
    # - "and" is a conjunction
    # - "point" is a none
    # - all other are numbers
    # But also contains this line these "measure words" for numbers:
    # - trillion
    # - billion
    # - million
    # - thousand
    # - hundred
    # This new algorithm split the word array from highest value to lowest 
    # (because hundred can be a measure and also a number). Then it work
    # only with number for this measure, simplify so the algorithm and
    # make it free from other measure part in the number.
    # Also it is no different to calculate a trillion or a million or other
    #
    
    for measure_value in sorted_measure_values:
        measure_value_index = get_index_for_number(measure_value, clean_numbers)
        if measure_value_index > -1:
            result +=  get_measure_multiplier(measure_value_index, clean_numbers) * measure_value
            clean_numbers = clean_numbers[measure_value_index+1:]
        # fi
    # rof
    # Now we add the value of less then hundred
    if len(clean_numbers) > 0:
        multiplier = number_formation(clean_numbers)
        result +=  multiplier * 1
    
    return result


def get_measure_multiplier (measure_index :int, clean_numbers):
    """ [internal] function to get the value for the measure aka 1000, 1_000_000 ...
    
    input: index of measure
    output: multiplier for measure
    """
    param = clean_numbers[0:measure_index]
    param = param if len(param)>0 else {get_name_by_number_value(1)}
    multiplier = number_formation(param)
    return multiplier


def word_to_num(number_sentence):
    """ public function to return integer for an input `number_sentence` string
    This function return as result
    - the same float if float is input
    - the same int if int is given
    - None if no number can be extracted
    - ValueError if extracted number is formal incorrect

    preconditions: number_sentence is type of float, int or str
    input: string
    output: int or float or None
    raise: given number is formal incorrect
    """
    result = None
    clean_numbers = []
    clean_decimal_numbers = []

    # check preconditions

    if type(number_sentence) is float:
        return number_sentence
    if type(number_sentence) is int:
        return number_sentence
    
    if type(number_sentence) is not str:
        raise ValueError("Type of input is not string! Please enter a valid number word (eg. \'two million twenty three thousand and forty nine\')")

    number_sentence = normalize(number_sentence) 

    if(number_sentence.isdigit()):  # return the number if user enters a number string
        result = int(number_sentence)
    else:
        split_words = re.findall(r'\w+', number_sentence)  # strip extra spaces and comma and than split sentence into words
    
        localizedPointName = number_system['point']
        # removing unknown words form text
        for word in split_words:
            word = normalize_data.get(word,word) # replacing words and lemma text
            if word in number_system:
                clean_numbers.append(word)
            elif word == localizedPointName:
                clean_numbers.append(word)
    
        # Error message if the user enters invalid input!
        if len(clean_numbers) == 0:
            raise ValueError("No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")
    
        # check point count
        if clean_numbers.count(localizedPointName)>1:
             raise ValueError("Redundant point word "+localizedPointName+"! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")
                  
        # split in pre-decimal and post-decimal part
        point_count = clean_numbers.count(localizedPointName)
        if point_count == 1:
            clean_decimal_numbers = clean_numbers[clean_numbers.index(localizedPointName)+1:]
            clean_numbers = clean_numbers[:clean_numbers.index(localizedPointName)]

        # check measure word errors
        measure_words_sequence = []
        # check for to much measure words like "million million"
        for measure_value_double_check in sorted_measure_values:
            if measure_value_double_check >= 1000: # measure values under 1000 can be more than one in text
                check_double_input(measure_value_double_check, clean_numbers)
                # save index for next check
                if -1 != get_index_for_number(measure_value_double_check,clean_numbers):
                    measure_words_sequence.append(get_index_for_number(measure_value_double_check,clean_numbers))

        # check generic measure words are in right sequence
        if measure_words_sequence != sorted(measure_words_sequence):
            raise ValueError("Malformed number in result of false measure word sequence eg. trillion after thousand! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")

        # check no measure words in decimal numbers
        for measure_value in sorted_measure_values:
            measure_name = get_name_by_number_value(measure_value)
            if measure_name in clean_decimal_numbers:
                raise ValueError("Malformed number in result of false measure word after point eg. trillion after thousand! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")

        # Now we calculate the pre-decimal value
        result = get_number_value(clean_numbers)
        
        # And add the post-decimal value
        if len(clean_decimal_numbers) > 0:
            total_sum_as_string = str(result)+"."+str(get_decimal_string(clean_decimal_numbers))
            result = float(total_sum_as_string)

    return result

#EOF

