# Word to Number

This is a Python module to convert number words (eg. twenty one) to numeric digits (21).
It works for positive numbers upto the range of 999,999,999,999 (i.e. billions)
Below is the installation, usage and other details of this module.

## Installation

Please ensure that you have **updated pip** to the latest version before installing word2number.

You can install the module using Python Package Index using the below command.

    pip install word2number

Make sure you install all requirements given in requirements.txt
```
pip install -r requirements.txt
```
## Usage

First you have to import the module using the below code.

    from word2numberi18n import w2n

Then you can use the **word_to_num** method to convert a number-word to numeric digits, as shown below.
```
print(w2n.word_to_num("two million three thousand nine hundred and eighty four"))
2003984
```
```
print(w2n.word_to_num('two point three')) 
2.3
```
```
print(w2n.word_to_num('112')) 
112
```
```
print(w2n.word_to_num('point one')) 
0.1
```
```
print(w2n.word_to_num('one hundred thirty-five')) 
135
```
```
print(w2n.word_to_num('million million'))
Error: Redundant number! Please enter a valid number word (eg. two million twenty three thousand and forty nine)
None
```
```
print(w2n.word_to_num('blah'))
Error: No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)
None
```

### for word2number user
Change your import from word2number to word2numberi18n.

    from word2numberi18n import w2n

## i18n
word2number looking for your specific language with
    1. defined environment variable w2n.lang with ISO lang code like en, hi, de and if not found
    2. over locale.getdefaultlocale() and if not found
    3. over environment variable "LANGUAGE" and if not found
    4. fallback to english 
Place in the data directory your language specific dictionary file with ISO lang code in the name.
    

## Bugs/Errors
- german language need more specific algorithm

## Thanks
Thanks to word2number coder and contributors 
- Akshay Nagpal [akshaynagpal](https://github.com/akshaynagpal)
- Ben Batorsky [bpben](https://github.com/bpben)
- Alex [ledovsky](https://github.com/ledovsky)
- Tal Yarkoni [tyarkoni](https://github.com/tyarkoni)
- ButteredGroove [ButteredGroove](https://github.com/ButteredGroove)

## License
The MIT License (MIT)

Copyright (c) 2016 Akshay Nagpal 
Copyright (c) 2020 Sebastian Ritter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
