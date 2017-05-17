.. image:: https://codecov.io/gh/akshaynagpal/w2n/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/akshaynagpal/w2n

==============
Word to Number
==============
This is a Python module to convert number words (eg. twenty one) to numeric digits (21). It works for positive numbers upto the range of 999,999,999,999 (i.e. billions).

++++++++++++
Installation
++++++++++++
Please ensure that you have **updated pip** to the latest version before installing word2number.

You can install the module using Python Package Index using the below command.

>>> pip install word2number


+++++
Usage
+++++
First you have to import the module using the below code.

>>> from word2number import w2n

Then you can use the **word_to_num** method to convert a number-word to numeric digits, as shown below.

>>> print w2n.word_to_num("two million three thousand nine hundred and eighty four")
2003984

>>> print(w2n.word_to_num('two point three')) 
2.3

>>> print(w2n.word_to_num('112')) 
112

>>> print(w2n.word_to_num('point one')) 
0.1

>>> print(w2n.word_to_num('one hundred thirty-five')) 
135

>>> print(w2n.word_to_num('million million'))
Error: Redundant number! Please enter a valid number word (eg. two million twenty three thousand and forty nine)
None

>>> print(w2n.word_to_num('blah'))
Error: No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)
None

+++++++++++
Bugs/Errors
+++++++++++

Please ensure that you have updated pip to the latest version before installing word2number.

If you find any bugs/errors in the usage of above code, please raise an issue through `Github <http://github.com/akshaynagpal/w2n>`_. If you don't know how to use Github or raise an issue through it, I suggest that you should learn it. Else, send an email to akshay2626@gmail.com with a clear example that can reproduce the issue.