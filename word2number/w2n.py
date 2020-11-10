num_names = {
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
    'niner': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
}

dec_names = {
    'point': '.',
    'decimal': '.',
}

place_names = {
    'hundred':      100,
    'thousand':     1000,
    'million':      1000000,
    'billion':      1000000000,
    'trillion':     1000000000000,
    'quadrillion':  1000000000000000,
    'quintillion':  1000000000000000000,
    'sextillion':   1000000000000000000000,
    'septillion':   1000000000000000000000000,
}

word_to_number = { **num_names, **place_names, **dec_names }
            
def num_generator(phrase):
    words = [ word for word in phrase.lower().replace('-',' ').replace(',','').split(' ') if word != 'and' and word != '' ]
    
    if len(words) == 0:
        raise ValueError('No valid words provided')
    
    # Check if there are any illegal duplicates
    if 1 < words.count('point'):
        raise ValueError('Duplicate number word provided: point')
        
    for place in ( *place_names, *dec_names ):
        if place != 'hundred' and 1 < words.count(place):
            raise ValueError('Duplicate number word provided: {}'.format(place))
            return 0
    
    for word in words:
        if word.replace('.', '').replace(',', '').replace(';', '').isalpha():
            word = word.replace('.', '').replace(',', '').replace(';', '')
            try:
                yield word_to_number[word]
            except KeyError:
                raise ValueError('Non-number words provided: {}'.format(word))
                return 0
        else:
            try:
                yield int(word)
            except ValueError:
                yield float(word)
    
def word_to_num(phrase):
    if type(phrase) is not str:
        raise ValueError('Type of input is not string! Please enter a valid number word (eg. \'two million twenty three thousand and forty nine\')')
    
    running_total = [0]
    postDecimalCount = 0
    
    for num in num_generator(phrase):
        if num == '.':
            postDecimalCount = -1
            
        elif num in place_names.values():
            # Get the next index which is smaller than the current item
            index = next((i for i, x in enumerate(running_total) if x < num), -1)
            
            # Sum all the smaller parts
            # e.g. if we are parsing 'one million four hundred thirty six thousand', we'll have
            # [ 1000000, 400, 36 ] when handling 1000; since 400 and 36 are both smaller than 
            # 1000 but 1000000 is not, we'll sum the smaller stuff to give [ 1000000, 436 ].
            # We'll later multiply the last item by this place name
            running_total = running_total[:index] + [ sum(running_total[index:]) ]
            
            # Special case if someone starts with a place name, e.g. 'hundred twenty' rather than
            # 'one hundred twenty'
            if running_total[-1] == 0:
                running_total[-1] = 1
            
            running_total[-1] *= num
            
            # Append a new item after this - we've just handled a place name, and need to separate
            # the remaining content in case we have another place name coming
            running_total.append(0)
            postDecimalCount = 0
            
        else:
            # Special case to pre-adjust the decimal value, in case someone puts something like 
            # 'point nineteen'
            if postDecimalCount:
                postDecimalCount -= len(str(num)) - 1
            running_total[-1] += num * 10**postDecimalCount
            if postDecimalCount:
                postDecimalCount -= 1
        
    return sum(running_total)