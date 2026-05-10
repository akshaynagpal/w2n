# Word to Number i18n

**Word to Number i18n** is a full new implementation of great Python word2number module for English and other languages sentences. In result of this work it

- support non-english languages (es, fr, ru, sk - yes and en)
- provide the business logic as
    - Java Archiv
    - Python Module
    - .net DLL
- exclude some bugs from word2number
- *include some own bugs in result of it is a program not god*

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

This is a part-feature-list of some features you would be see in result of compare the similar languages implementations. It does not mean these features are bad or good.

### Python
- Dynamic arrays inside language can use this instead of an Collection framework.
- Optional parameters
- Wrap OO-Class with procedural call in same source
- ...

### Java
- To convert a ``String`` to ``double`` localization information is ignored (``Locale``) and the **dot** is needed.
<br>``double doubleValue = Double.valueOf(decimalValueWithPoint);``
- Optional parameters
- ...

### CSharp
- Unlike Java it is important at converting a ``string`` to ``double`` the right localization information in the background exists (``CultureInfo``).
<br>``double doubleValue; double.TryParse (pointDelimitedDecimalValue, NumberStyles.Any,CultureInfo.InvariantCulture, out doubleValue);``
    - but I need to declare variable ``doubleValue`` before(?).
- Semantic sugar is to get KEY and VALUE from dictionary at same time.
<br>``foreach (KeyValuePair<keyType, valueType> pair in this.filebasedNumberSystem){}``
- Working with Dictionary like Array with non-numeric index.
<br>``object value = this.dictionaryInstance[key];``
- Optional parameters
- ...


## Test system

Local test system is

- CPython 3.9 @ Darwin
- Java AdoptOpenJDK 15 @ Darwin
- CSharp net5.0 @ Darwin

Test can be better and add for error a new test case.

## License
The MIT License (MIT)

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

