# Word to Number ![Build Status](https://travis-ci.org/akshaynagpal/w2n.svg?branch=master)  ![codecov](https://codecov.io/gh/akshaynagpal/w2n/branch/master/graph/badge.svg) ![rtdbadge](https://readthedocs.org/projects/w2n/badge/)

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

    from word2number import w2n

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

You can also use the **num_to_word** method to convert an int or float to a number-word string, as shown below.
```
print w2n.num_to_word(42)
"forty two"
```
```
print w2n.num_to_word(7654321)
"seven million six hundred fifty four thousand three hundred twenty one"
```
```
print w2n.num_to_word(1.23456)
"one point two three four five six"
```
```
print w2n.num_to_word("five")
Error: Type of input is not a number! Please enter a valid number (eg. '42' or '0.01')
```
## Bugs/Errors

Please ensure that you have updated pip to the latest version before installing word2number.

If you find any bugs/errors in the usage of above code, please raise an issue through [Github](http://github.com/akshaynagpal/w2n). If you don't know how to use Github or raise an issue through it, I suggest that you should learn it. Else, send an email to akshay2626@gmail.com with a clear example that can reproduce the issue.

## Contributors
- Ben Batorsky [bpben](https://github.com/bpben)
- Alex [ledovsky](https://github.com/ledovsky)
- Tal Yarkoni [tyarkoni](https://github.com/tyarkoni)
- ButteredGroove [ButteredGroove](https://github.com/ButteredGroove)
- Adam Rhine [OptimusRhine](https://github.com/OptimusRhine)

## License
The MIT License (MIT)

Copyright (c) 2016 Akshay Nagpal (https://github.com/akshaynagpal)

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
