==============
Word to Number
==============
This is a Python module to convert number words (eg. twenty one) to numeric digits (21). It works for positive numbers upto the range of 999,999,999,999 (i.e. billions).
It supports i18n under Python3.

++++++++++++
Installation
++++++++++++
Please ensure that you have **updated pip** to the latest version before installing word2number.

You can install the module using Python Package Index using the below command.

.. code-block:: python

  pip install word2number

Make sure you install all requirements given in requirements.txt

.. code-block:: python

  pip install -r requirements.txt

+++++
Usage
+++++
First you have to import the module using the below code.
.. code-block:: python

    from word2number import w2n

Then you can use the **word_to_num** method to convert a number-word to numeric digits, as shown below.

.. code-block:: python

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


word2number user change the import to

    from word2numberi18n import w2n


+++++++++++
Bugs/Errors
+++++++++++

Please ensure that you have updated pip to the latest version before installing word2number.

If you find any bugs/errors in the usage of above code, please raise an issue through `Github <https://github.com/bastie/w2ni18n>`_. 
If you don't know how to use Github or raise an issue through it, I suggest that you should learn it. 


++++++++++++
Thanks to 
++++++++++++
Thanks to word2number coder and contributors 
- Akshay Nagpal (`akshaynagpal <https://github.com/akshaynagpal>`__)
- Ben Batorsky (`bpben <https://github.com/bpben>`__)
- Alex (`ledovsky <https://github.com/ledovsky>`__)
- Tal Yarkoni (`tyarkoni <https://github.com/tyarkoni>`__)
- ButteredGroove (`ButteredGroove <https://github.com/ButteredGroove>`__)

