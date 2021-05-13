num_names = {
    'zero': 0,
    'naught': 0,
    'nil': 0,
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

place_abbrev = {
    'k':            1000,
    'm':            1000000,
    'b':            1000000000,
}

place_names = {
    'dozen':        12,
    'score':        20,
    'hundred':      100,
    'gross':        144,
    'thousand':     1000,
    'million':      1000000,
    'billion':      1000000000,
    'trillion':     1000000000000,
    'quadrillion':  1000000000000000,
    'quintillion':  1000000000000000000,
    'sextillion':   1000000000000000000000,
    'septillion':   1000000000000000000000000,
    **place_abbrev
}

dec_names = {
    'point': '.',
    'decimal': '.',
    '.': '.',
}

neg_names = {
    'minus': '-',
    'negative': '-',
    '-': '-',
}

ignore_chars = [ '$', ';', ',' ]
ignore_words = [ 'a', 'and', '&', '' ]

word_to_number = { **num_names, **place_names, **dec_names, **neg_names }
            
def num_generator(phrase):
    # remove dirty characters - commonly put in numbers but not "part of" the number
    cleanphrase = ''.join(char for char in phrase if char not in ignore_chars)
    # make . its own word so we can treat it like the other decimal words
    splitphrase = cleanphrase.replace('.', ' . ').lower()
    
    words = [ ]
    # remove dirty words - commonly put in number words but not "part of" the number
    for word in (word for word in splitphrase.split(' ') if word not in ignore_words):
        # separate suffixes (e.g. 150k -> 150 k)
        if word[:-1].isdigit() and word[-1] in place_abbrev:
            words.append(word[:-1])
            words.append(word[-1])
        # - is confusing, since it can be a separator (sixty-six) or a negative (-10)
        # fortunately, to be a negative it must be at the start of a word
        elif '-' in word:
            i = word.index('-')
            if i == 0:
                words.append('-')
                words.append(word[1:])
            else:
                words.append(word[:i])
                words.append(word[i+1:])
        else:
            words.append(word)
    
    if len(words) == 0:
        raise ValueError('No valid words provided')
    
    countDec = sum( words.count(dec) for dec in dec_names )
    countNeg = sum( words.count(neg) for neg in neg_names )
    
    # Check if there are any valid number words
    if len(words) == countDec + countNeg:
        raise ValueError('No valid number words provided')
    
    # Check if there are any illegal duplicates
    if 1 < countDec:
        raise ValueError('At most one of the following allowed: {}'.format(dec_names))
        
    if 1 < countNeg:
        raise ValueError('At most one of the following allowed: {}'.format(countNeg))
        
    for place in place_names:
        # Hundred is a special case, since "one hundred thousand one hundred" is a valid number
        if place != 'hundred' and 1 < words.count(place):
            raise ValueError('Duplicate number word provided: {}'.format(place))
            return 0
    
    # Iterate over the words, yielding them consecutively as numbers
    for word in words:
        if word in word_to_number:
            yield word_to_number[word]
        else:
            try:
                yield int(word)
            except ValueError:
                try:
                    yield float(word)
                except:
                    raise ValueError('Non-number words provided: {}'.format(word))
                    return 0
    
def word_to_num(phrase):
    if type(phrase) is not str:
        raise ValueError('Type of input is not string! Please enter a valid number word (eg. \'two million twenty three thousand and forty nine\')')
    
    running_total = [ 0 ]
    postDecimalCount = 0
    sign = 1
    
    for num in num_generator(phrase):
        if num == '.':
            postDecimalCount = -1
            
        elif num == '-':
            if running_total[0] != 0:
                raise ValueError('Negating word must be first word')
            sign = -1
            
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
            
        elif len(str(num)) != len(str(running_total[-1])) or postDecimalCount:
            # Special case to pre-adjust the decimal value, in case someone puts something like 
            # 'point nineteen'
            if postDecimalCount:
                postDecimalCount -= len(str(num)) - 1
            running_total[-1] += num * 10**postDecimalCount
            if postDecimalCount:
                postDecimalCount -= 1
                
        else:
            running_total.append(0)
            running_total[-1] = num
        
    if all( num < 10 for num in running_total ):
        return sign * sum( num * 10**i for i, num in enumerate(reversed(running_total)) )
    else:
        return sign * sum(running_total)
        
def num_word_indices(phrase):
    indices = []
    for i, word in enumerate(phrase.lower().split(' ')):
        cleanWord = ''.join(char for char in word if char not in ignore_chars + [ '.', '-' ])
        if cleanWord.isdigit() or cleanWord in word_to_number:
            indices.append(i)
    
    return indices