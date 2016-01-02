==============
Word to Number
==============
This is a Python module to convert number words (eg. twenty one) to numeric digits (21).
It works for positive numbers upto the range of 999,999,999,999 (i.e. billions)
Below is the installation, usage and other details of this module.

++++++++++++
Installation
++++++++++++
You can install the module using Python Package Index using the below command.::

>>>pip install w2n


+++++
Usage
+++++
First you have to import the module using the below code.::

>>> from w2n import w2n



Then you can use the **word_to_num** method to convert a number-word to numeric digits, as shown below.::

>>> print w2n.word_to_num("two million three thousand nine hundred and eighty four")
    2003984

+++++++++++
Bugs/Errors
+++++++++++
If you find any bugs/errors in the usage of above code, please send an email at akshay2626@gmail.com or contact through .. _github: http://github.com/akshaynagpal/w2n .

+++++++
License
+++++++
The MIT License (MIT)

Copyright (c) 2016 Akshay Nagpal (github.com/akshaynagpal)

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