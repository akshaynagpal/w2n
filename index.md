# Word to Number i18n

Convert number words from different languages with Python or Java API eg. three hundred and forty two to numbers (342) or vingt-et-un (21) or две целых три десятых (2.3).Word2Number-i18n convert number words (eg. twenty one) to numeric digits (21).
Below is the installation, usage and other details of this module.

## Python

### Installation

Please ensure that you have **updated pip** to the latest version before installing word2number-i18n.

You can install the module using Python Package Index using the below command.

```
    pip3 install word2number-i18n 
```

### Installation from source

On macOS

```
    # git clone https://github.com/bastie/w2ni18n.git w2n
    # python3 setup.py install
```

Make sure you install all requirements given in requirements.txt

```
    pip3 install -r requirements.txt
```


### Usage

Add the word2number-i18n to requirements.txt in your project.
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


### i18n

word2number looking for your specific language with

    1. defined environment variable w2n.lang with ISO lang code like en, hi, de and if not found
    2. over locale.getdefaultlocale() and if not found
    3. over environment variable "LANGUAGE" and if not found
    4. fallback to english 
    
Place in the data directory your language specific dictionary file with ISO lang code in the name.
   
#### Request new language

Do follow steps

    1. check your request (directory data), textfile name ISO-639-1 code
    2. if not found check ISO-639-3 code
    3. if not found create new file with new ISO-639-1/3 code

##### Example
You want to tranfer NLP CARD to numeric value for Lower Sorbian. German (de) isn't it. 
You do not found an ISO-639-1 code, you do not found an ISO-639-1 file for ```dsb``` extension.
You create a new file ```number_system_dsb.txt``` with utf-8 encoding

```
    null 0
    jaden 1
    dwa 2
    tśi 3
    styri 4
    pěś 5
    šesć 6
    sedym 7
    wósym 8
    źewjeś 9
    źaseś 10
    [...]
    point ,
```


### Develop package

```
    # python3 -m reuse lint
    # python3 -m flake8 | grep -v ":80: E501"
    #
    # python3 setup.py sdist bdist_wheel
    # python3 -m twine check dist/*
    # python3 -m twine upload dist/*
```

Make sure you install all requirements given in development.txt

```
    pip3 install -r development.txt
```

## Java

Please note that these Java implementation is similar to Python.

### Installation

Download the latest version of word2number from GitHub.

### Installation from source

On macOS

```
    # git clone https://github.com/bastie/w2ni18n.git w2n
    # ./w2n/src/build.sh
```

### i18n

word2number looking for your specific language with

    1. defined environment variable (not property) w2n.lang with ISO lang code like en, hi, de and if not found
    2. over java.util.Locale.getDefault() and if null
    3. over environment variable "LANGUAGE" and if not found
    4. fallback to english
    
Place in the data directory your language specific dictionary file with ISO lang code in the name.
   
### Usage

Add the word2number-i18n to module-info.java in your project.

    requires word2number;

Then import the class using the below code.

    import word2number.W2N;

Then you can use the **wordToNum** method to convert a number-word to numeric digits, as shown below.

```
    Locale.setDefault(Locale.CANADA);
    W2N english = new W2N();
    System.out.println(english.wordToNum("three hundred fifty"));

    Locale.setDefault(Locale.CANADA_FRENCH);
    W2N french = new W2N();
    System.out.println(french.wordToNum("vingt et un"));
    
    System.out.println(english.wordToNum("three point one four"));
```

In result it prints

```
350
21
3.14
```


#### Request new language

Do follow steps

    1. check your request (directory data), textfile name ISO-639-1 code
    2. if not found check ISO-639-3 code
    3. if not found create new file with new ISO-639-1/3 code

##### Example
You want to tranfer NLP CARD to numeric value for Lower Sorbian. German (de) isn't it. 
You do not found an ISO-639-1 code, you do not found an ISO-639-1 file for ```dsb``` extension.
You create a new file ```number_system_dsb.txt``` with utf-8 encoding

```
    null 0
    jaden 1
    dwa 2
    tśi 3
    styri 4
    pěś 5
    šesć 6
    sedym 7
    wósym 8
    źewjeś 9
    źaseś 10
    [...]
    point ,
```

Call the build.sh script and use the new w2ni18n-VERSION-.jar file


## Bugs/Errors
- german language need more specific algorithm

### w2n fixed
- ``Add regex to fix comma bug`` fixed by jnelson16
- ``fixed floating point conversation bug``
- ``accept also number values`` because it is more understandable to handle str:112 as same as int:112



## Thanks
Thanks to word2number coder and contributors 
- Akshay Nagpal [akshaynagpal](https://github.com/akshaynagpal)
- Ben Batorsky [bpben](https://github.com/bpben)
- Alex [ledovsky](https://github.com/ledovsky)
- Tal Yarkoni [tyarkoni](https://github.com/tyarkoni)
- ButteredGroove [ButteredGroove](https://github.com/ButteredGroove)
- Jonathan Nelson [jnelsen16](https://github.com/jnelson16)
- Daniel Junior [danieljunior](https://github.com/danieljunior)

## License
The MIT License (MIT)

Copyright (c) 2016 Akshay Nagpal 

Copyright (c) 2020-2021 Sebastian Ritter

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

