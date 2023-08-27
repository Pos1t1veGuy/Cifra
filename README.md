# cifra
It has some ciphers and number systems, for start we must to download library.


# Downloading
Clone this repository:
```
git clone https://github.com/Pos1t1veGuy/cifra
```
After you can put it in Python/Libs for use 'import cifra' in any directory.


# Using
Importing:
```
import cifra
```
After you can use ciphers and number systems, let's start with number systems:


# Number Systems

## Custom System
You can convert your number to any base:
```
cifra.convert_to_base(number, base, digits)
```
'number' (int) is your number, that you want to convert.
'base' (int) is your base, for example 8 is octal number system.
'digits' (str) is your representations of digits of numbers in a given number system. ( default: string.digits + string.ascii_letters + string.punctuation )

## Roman System

### Roman Class
You can create cifra.Roman object:
```
roman = cifra.Roman(num)
```
'num' (Union[str, int, float]) is your number, that you want to convert, may be python int or float more than 0 (or roman number in python str).

And work with it as python int, for example:
```
>>> from cifra import Roman
>>> roman = Roman(10)
>>> roman > 1
True
>>> roman < 11
True
>>> roman + 1
Roman(int=11,value='XI',augments=1)
>>> roman*2
Roman(int=20,value='XX',augments=1)
```

To get int value enter it:
```
int(roman)
```
Or it:
```
roman.int
```

To get roman value enter it:
```
str(roman)
```
Or it:
```
roman.roman
```

### Roman Static Methods
Or you can convert python int to roman number:
```
cifra.Roman.int_to_roman(num)
```
'num' (Union[str, int, float]) is your number, that you want to convert, must be more than 0.
It returns python str with roman number.

And convert roman number to python int:
```
cifra.Roman.roman_to_int(num)
```
'num' (Union[str, int, float]) is your roman number, that you want to convert.
It returns python int.

To check roman number spelling you can use:
```
cifra.Roman.is_valid_roman(num)
```
'num' (Union[str, int, float]) is your roman number, that you want to check.
It returns python bool

### Roman Using
Easier to work cifra.Roman than Roman Static Methods.

Fun Fact: Roman number system has limit of 3999.
To bypass the limit cifra.Roman use augments. It adds "MMMCMXCIX + " to roman number, "MMMCMXCIX" = arabic 3999, it called ONE augment. When you try to overcome roman limit class adds some augments to roman number, for example:
```
>>> from cifra import Roman
>>> roman = Roman(4000)
>>> roman.roman
'MMMCMXCIX + I'
>>> roman = Roman(121_212)
>>> roman.roman
'MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MCCXLII'
>>> Roman(4444).roman
'MMMCMXCIX + CDXLV'
>>> len(Roman(4000))
1
```
'len(cifra.Roman)' returns a count of augments.

You can change augments separator in 'sep' kwarg in static methods or in cifra.Roman constructor:
```
>>> from cifra import Roman
>>> str(Roman(4000, sep='-'))
'MMMCMXCIX-I'
>>> Roman.int_to_roman(8000, sep='+')
'MMMCMXCIX+MMMCMXCIX+II'
```

If the number is large enough ( more than Roman threshold ), it will be reduced:
```
>>> from cifra import Roman
>>> str(Roman(200_000))
'MMMCMXCIX*50 + L'
>>> str(Roman(20_000))
'MMMCMXCIX*5 + V'
```
You can change Roman threshold in constructor:
```
>>> from cifra import Roman
>>> str(Roman(25_000))
'MMMCMXCIX*6 + MVI'
>>> str(Roman(25_000, threshold=26_000))
'MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MMMCMXCIX + MVI'
```


# Ciphers
This is list of ciphers:
```
Vigenere,
Cesar,
a1z26,
Atbash,
Morse.
```
You can find cipher in 'cifra.( cipher name )'.
Every cipher has 'encode' method and some has 'decode'. ( because it is not necessary for some ciphers )

## Vigenere
```
encoded = cifra.Vigenere.encode(key, text)
decoded = cifra.Vigenere.encode(key, text)
```
Coding and decoding python str 'text' with python str 'key' to Vigenere, for example:
```
>>> from cifra import Vigenere
>>> Vigenere.encode("keyword", "testword")
'DIQPKFUN'
>>> Vigenere.decode("keyword", "DIQPKFUN")
'TESTWORD'
```

## Cesar
Has only one method 'encode'.
```
encoded = cifra.Vigenere.encode(text, step, chars)
```
'text' (str) is your text, that you want to encode.
'step' (int) is your step for encode.
'chars' (Union[str, list]) is your alphabet. ( default: string.ascii_letters + string.digits + string.punctuation )

Coding and decoding python str 'text' with python str 'key' to Cesar, for example:
```
>>> from string import ascii_letters, digits
>>> from cifra import Cesar
>>> Cesar.encode("testword", 5, chars = ascii_letters + digits)
'flrxDJPV'
>>> Cesar.encode("flrxDJPV", -5, chars = digits)
'51739517'
```

## a1z26
```
encoded = cifra.a1z26.encode(text, chars, sep)
decoded = cifra.a1z26.decode(text, chars, sep)
```
'text' (str) is your text, that you want to encode.
'chars' (Union[str, list]) is your alphabet. ( default: string.ascii_letters + string.digits + string.punctuation + ' ' )
'sep' (str) is your separator between numbers, for example: "12-11-10" if sep is '-' ( default: '-' )

Coding and decoding python str 'text' with python str alphabet 'chars' and separator between numbers 'sep' to a1z26, for example:
```
>>> from cifra import a1z26
>>> a1z26.encode('testword', sep = '~')
'19~4~18~19~22~14~17~3'
>>> a1z26.decode('19~4~18~19~22~14~17~3', sep = '~')
'testword'
```


## Atbash
Has only one method 'encode'.
```
encoded = cifra.a1z26.encode(text)
```
'text' (str) is your text, that you want to encode.

Coding and decoding python str 'text' to Atbash, for example:
```
>>> from cifra import Atbash
>>> Atbash.encode('testword')
'gvhgdliw'
>>> Atbash.encode('gvhgdliw')
'testword'
```


### Morse
```
encoded = cifra.Morse.encode(text)
decoded = cifra.Morse.decode(text)
```
'text' (str) is your text, that you want to encode.

Coding and decoding python str 'text' to Morse, for example:
```
>>> from cifra import Morse
>>> Morse.encode('testword')
'- . ... - .-- --- .-. -..'
>>> Morse.decode('- . ... - .-- --- .-. -..')
'TESTWORD'
```
