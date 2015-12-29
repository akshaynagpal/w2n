import math

american_number_system = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000,
    'billion': 1000000000
}

#TODO
indian_number_system = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'lac': 100000,
    'lakh': 100000,
    'crore': 10000000
}

#######################################################################################
"""
testing for american_number_system

'one hundred and forty two': 1,100,40,2 -> 1*100+40+2 = 142
'three thousand four hundred and seventy four': 3, 1000, 4,100, 70, 4 -> 3*1000,4*100,70+4 = 3474
'thirty five thousand seven hundred eight nine' : 30,5,1000,7,100,80,9 ->
'thirty five thousand seven hundred ninety': 30,5,1000,7,100,90
'three hundred thousand four hundred forty two': 3,100,1000,4,100,40,2

algo -
BEGIN
1. start from left
2. initialize total_sum and temp_sum to zero.
3. Start adding numbers to temp_sum till you reach a 1000,100,100000 etc.
4. when reach 1000,1000000 etc. multiply temp_sum with 100, 1000 whatever reached.
5. add this to total sum and reset temp_sum=0.
6. if(you reach end and temp_sum does not include 100):
7. 			add temp_sum to total_sum.
END
"""
########################################################################################

def word_to_num(number_sentence):
    split_words = number_sentence.split()  # split sentence into words
    separate_numbers = []  # map words to numbers through number system dictionaries
    for word in split_words:
        if word in american_number_system:
            separate_numbers.append(american_number_system[word])
    number_formation(separate_numbers)
    return 0


def number_formation(separate_numbers):
    print separate_numbers
    total_sum = 0
    temp_sum = 0
    for number in separate_numbers:
        if (math.log10(number)).is_integer() and (math.log10(number)) != 0:
            if temp_sum == 0:
                total_sum += number
            else:
                total_sum += (number * temp_sum)
                temp_sum = 0
        else:
            temp_sum += number
    total_sum += temp_sum
    print total_sum
    return 0

word_to_num('one hundred and forty two')

word_to_num('three thousand four hundred and seventy four')

word_to_num('thirty five thousand seven hundred eighty nine')

word_to_num('three hundred thousand four hundred forty two')