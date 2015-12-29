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
"""
########################################################################################



def word_to_num(number_sentence):
    split_words = number_sentence.split()  # split sentence into words
    clean_numbers = []  # removing and, & etc.
    for word in split_words:
        if word in american_number_system:
            clean_numbers.append(word)

    billion_index = clean_numbers.index('billion') if 'billion' in clean_numbers else -1
    million_index = clean_numbers.index('million') if 'million' in clean_numbers else -1
    thousand_index = clean_numbers.index('thousand') if 'thousand' in clean_numbers else -1

    total_sum = 0
    if billion_index>-1 :
        billion_multiplier = number_formation(clean_numbers[0:billion_index])
        # print "billion_multiplier",str(billion_multiplier)
        total_sum += billion_multiplier * 1000000000

    if million_index>-1 :
        if billion_index>-1:
            million_multiplier = number_formation(clean_numbers[billion_index+1:million_index])
        else:
            million_multiplier = number_formation(clean_numbers[0:million_index])
        total_sum += million_multiplier * 1000000
        # print "million_multiplier",str(million_multiplier)

    if thousand_index > -1:
        if million_index > -1:
            thousand_multiplier = number_formation(clean_numbers[million_index+1:thousand_index])
        elif billion_index>-1 and million_index==-1:
            thousand_multiplier = number_formation(clean_numbers[billion_index+1:thousand_index])
        else:
            thousand_multiplier = number_formation(clean_numbers[0:thousand_index])
        total_sum += thousand_multiplier * 1000
        # print "thousand_multiplier",str(thousand_multiplier)

    if thousand_index>-1 and thousand_index != len(clean_numbers)-1:
        hundreds = number_formation(clean_numbers[thousand_index+1:])
    elif million_index>-1 and million_index != len(clean_numbers)-1:
        hundreds = number_formation(clean_numbers[million_index+1:])
    elif billion_index>-1 and billion_index != len(clean_numbers)-1:
        hundreds = number_formation(clean_numbers[billion_index+1:])
    elif thousand_index==-1 and million_index==-1 and billion_index==-1:
        hundreds = number_formation(clean_numbers)
    else:
        hundreds = 0
    total_sum += hundreds
    # print "hundreds",str(hundreds)
        
    print total_sum
    return total_sum


def number_formation(number_words):
    numbers = []
    for number_word in number_words:
        numbers.append(american_number_system[number_word])
    if len(numbers)==4:
        return (numbers[0]*numbers[1])+numbers[2]+numbers[3]
    elif len(numbers)==3:
        return numbers[0]*numbers[1] + numbers[2]
    elif len(numbers)==2:
        if 100 in numbers:
            return numbers[0]*numbers[1]
        else:
            return numbers[0]+numbers[1]
    else:
        return numbers[0]

word_to_num('one hundred and forty two')

word_to_num('three thousand four hundred and seventy four')

word_to_num('thirty five thousand seven hundred eighty nine')

word_to_num('three hundred thousand four hundred forty two')

word_to_num('three million') ##

word_to_num('three billion') ##

word_to_num('three thousand') ##

word_to_num('three hundred thousand four hundred') ##

word_to_num('thirty five thousand seven hundred eighty one')

word_to_num('one hundred twenty three million four hundred fifty six thousand seven hundred and eighty one')

word_to_num('four hundred and forty three thousand') ##