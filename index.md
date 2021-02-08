# Word to Number i18n

**Word to Number i18n** is a full new implementation of great Python word2number module for English sentences. In result of this work it

- support non-english languages
- provide the business logic as
    - Java Archiv
    - Python Module
- exclude some bugs from word2number

The implementation want to be that
- more readable than using high-end programming language features
- more simplify than build high speed (compiler) result but also 
- more a usable than an extended ``Hello World``

**Word to Number i18n** convert number words from different languages with different programming languages eg. three hundred and forty two to numbers (342) or vingt-et-un (21) or две целых три десятых (2.3). 

## Download

- Python:   pip3
- Java:     GitHub repository
- CSharp:	nuget

## Programming language features

### Python
### Java
- To convert a ``String`` to ``double`` localization information is ignored (``Locale``) and the **dot** is needed.
<br>``double doubleValue = Double.valueOf(decimalValueWithPoint);``

### CSharp
- Unlike Java it is important at converting a ``string`` to ``double`` the right localization information in the background exists (``CultureInfo``).
<br>``double doubleValue; double.TryParse (pointDelimitedDecimalValue, NumberStyles.Any,CultureInfo.InvariantCulture, out doubleValue);``
- Semantic sugar is to get KEY and VALUE from dictionary at same time.
<br>`` foreach (KeyValuePair<keyType, valueType> pair in this.filebasedNumberSystem){}``
- ...


## Test system

Local test system is

- CPython 3.9 @ Darwin
- Java AdoptOpenJDK 15 @ Darwin
- CSharp net5.0 @ Darwin


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

