---
title: Python Language Notes
date: '2016-11-27T21:45:02+04:00'
lastmod: '2023-03-31T14:43:47+04:00'
original_id: '{A420}'
original_name: python
original_blob: blob/B/11/661.txt
revisions: 116
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: python
draft: false
topics:
- python
---

[Python Libraries, tools and Links](pythonlibrariestoolsandlinks.md) | [Official Python Docs](https://docs.python.org/3/)
| [Intro to Pygame](intropygame.md) | [spaCy](pythonspacy.md)

# Python Language Notes

1. **Lexical Analysis**
1. [Keywords](pykeywords.md)
1. ```
   name      ::=  lc_letter (lc_letter | "_")*
   lc_letter ::=  "a"..."z"
  ```
1. **Operators and Builtin Functions**
1. 1. **All Types**
    1. ```
      type(obj) --> type object
      ```
    1. ```
      isinstance(obj, typ) --> bool
      ```
    1. ```
      repr(obj) #evaluatable representation
      ```
    1. ```
      str(obj)  #printable representation
      ```
    1. ```
      is, is not # are two objects the same
      ```
1. - **All Numeric Types**
    - - ` abs(-1) # 1`
          - ` chr(65) #'A' `
          - ` ord('A')#65 `
          - ` complex(1) #(1+0j) `
          - ` divmod(25,7) #(3,4) `
          - ` pow(2,8) #256 `
          - ` round(2.75,1) #2.8, rounds up `
1. **Objects**
1. ```
  int, float, bool, dict, set, tuple, str, bytes
   None
  ```
1. **Classification**
1. - Primative, Numeric, Sequence, Container: Can contain other types, Collection
    - Common use cases
    - - Dictionaries for lookups
          - Tuples for data that is invariant at runtime
          - Lists for dynamic runtime data
1. **Primative Types**
1. - **bool** -> `True, False`
    - - ` bool(float("NaN")) --> True `
          - ` bool(0.0) --> False `
          - ` bool(0) --> False `
          - ` bool([]) --> False `
    - **int**
    - - ` 2**31 - 1 `
          - binary: ` 0b10 `, ` bin(20) #'0b10100' `
          - octal: ` 0o77 `, ` oct(20) #'0o24" `
          - hex: ` 0xFF `, ` hex(20) #'0x14' `
          - ` int(3.5); int("3.5"); int("1111", 1) --> 15`
          - ` abs(-1)`
          - ` 1//3 #0, integer division`
    - **float**
    - - ` 1.41 `
          - ` 3e-5 `
          - ` float(3), float("3.14") `
          - ` float("nan"), float("inf"), float("-inf")`
          - : {round(1.234, 2)
1. **Complex**
1. ```
   complex(2,3) #(2+3j)
  ```
1. **Sequence** (Builtin Functions)
1. `len(obj)`
1. - **character** (char): `ord(char)` --> int
    - **strings**
    - ```
      help(str)
      >>> m = """This is
      ... a multiline
      ... string"""
      'This is\na multiline\nstring'
      print(m)
      str(666)
      "Vi er så glad for å høre og lære om Python!" # 'Vi er så glad for å høre og lære om Python!'
      "Vi er s\u00e5 glad for \u00e5 h\xf8re og l\u00e6re om Python!" ' #Vi er så glad for å høre og lære om Python!'
      ```
    - ```
      '\\xe5'
      'å' 
      ```
    - ```
      '\\345' 'å'
      ```
    - ```
      str.title(), str.upper(), str.lower, str.lstrip(), .rstrip, .strip
      var = 'in'
      print(f"I am {var} trouble!")
      ```
    - **f**
    - raw strings `r'this is t raw'`
    - - implicit concatantion `"hello" "world"`
    - bytes `b'this is a byte string'`
    - ```
      b'this is a byte string'.split()
      [b'this', b'is', b'a', b'byte', b'string']
      "Vi er så glad for ".encode('utf-8')
      b'Vi er sa\\xcc\\x8a glad for '.decode('utf-8')
      ```
    - **bytearray**
    - **tuple**
    - ```
       (1,2)
       (False, 1, 'c')
       (2,) + (9,) => (2,9)
      ```
    - **Lists**
    - ```
      [1,2,3]
      [True, False, '7']
      ```
    - ```
      append(x), count(x), extend(L), index(x), insert(x), insert(i,x), pop(x), remove(x), reverse(), sort()
      ```
    - ```
      alist = [0, 1, 2, 3]
      del alist[2]  #[0, 1, 3]
      ```
    - **slice**
    - ```
      mylist[:]
      ```
    - - **Sorting Lists**
          - ```
            sorted() #generate a copy
            sort
            sorted(x, reverse=True)
            reverse()
            ```
          - **Numerical Lists**
          - ` range() `
          - ```
            list(range(5))
            list(range(5,11))
            nums = []
            for exp in range(5):
                nums.append(2**exp)
            ```
          - **List Comprehensions**
          - ```
            [2**exp for exp in range(5)]
            ```
          - ` [i**3 for i in range(10) if True] `
          - ```
            f = open("test.txt", 'r')
            data = [line.strip for line in f]
            f.close()
            # now process data
            ```
          - **Generator Expressions**
          - *list comprensions*
          - ```
            f = open("test.txt", 'r')
            data = (line.strip for line in f)
            #now process data before closing the file!
            f.close()
            ```
    - **dictionary**
    - ` {key:value}`
    - ` 'key' in dict `
    - ```
      states = {
      	'ca': 'California',
      	'il': 'Illinois',
      	'fl': 'florida',
      	}
      states['ca']
      states.get('xx', 'default value') # equivalant to: states['xx'] if 'xx' in states else 'default value'
      states.setdefault('xx', 'default value') #in not there set and return the key.
      states['ny'] = 'New York'
      del states['il']
      states.values() #dict_values([...]), <class 'dict_values'>
      states.items()
      states.keys()
      ```
    - ```
      has_key(), keys(), values(), dict.items(), clear(), copy(), update(x), get(x,[y])
      ```
    - **Set**
    - ` {1,2,3}`
    - ```
      s = set()
      s.add(1)
      s.add('foo')
      t = set()
      s | t #union of t & s
      ```
    - *Set Comprehensions*
    - ```
      odd = \{i for i in range(10) if i % 2\}
      ```
    - **Frozenset**
    - **Complex**
1. **Modules and Packages**
1. - **Modules**
    - ```
      import module
      import module as mod
      from module import specific_function
      ```
    - **Packages**
    - *maps*
    - ```
      maps/
       __init__.py
       cities.py
       navigation.py
       gpsdata.py
      ```
    - **__init__.py**
    - ```
      import maps 
      ```
    - ```
      maps.navigation.turn_right() 
      ```
1. **Standard Library / Types**
1. - **math**
    - ```
      import math
      math.sqrt(16)
      PI = math.pi
      math.sin(PI)
      math.log(1000, 10)
      ```
    - **Fraction**
    - **Decimal**
    - **Date**
    - **Array**
    - **range**
    - ```
      range(5)
      ```
1. **Converstion Functions**
1. - `int, float, bool, str, tuple, list, dict, set`
    - `chr(int)` --> char
1. **Operators**
1. - ` + 1 * ** / // % `
    - ` ~ >> << & ^ | `
    - ` < > <= >= <> != == `
    - ` and, or, not `
    - ```
        <string | list> + <string | list>
        'five' + 'four'
        <int> * <string | list>
        <obj> in <seq>
      ```
    - **Function application**
    - ` function(args...)`
    - **Indexing**
    - ` seq[index | range] `
    - **Lookup (dictionaries)**
    - ` d[key] `
1. **Expressions**
1. ```
   Operator Precedence
  | no. | operators  | description          |
  |   1 | f(...)     | function application |
  |   2 | o[l]       | index lookups        |
  |   3 | o.f(...)   | method call          |
  |   4 | **         | exponentiation       |
  |   5 | -N         | sign change          |
  |   6 | *,/,//,%   | numeric              |
  |   7 | +,-        | numeric              |
  |   8 | <, <=, ... | comparisons          |
  |   9 | in, not in | membership           |
  |  10 | not o      | logical              |
  |  11 | and 0      | logical              |
  |  12 | or         | logical              |
  ```
1. **Rules for Well-formedness**
1. - R1
    - ```
       Every Value is well formed
      ```
    - R2 (E)
    - ```
       if E is well formed then (E) is well formed
      ```
    - R3 `<uop> E`
    - ```
       <uop> is a unary operation
       if E, then <uop> E is well formed
      ```
    - R4 `E1 <bop> E2`
    - ```
       <bop> is a binary operation
       if E1, E2, then E1 <bop> E2
      ```
    - R5 E1[E2]
    - ```
       if E1, E2, the E1[E2]
      ```
    - R6 F(A, ...)
    - ```
       if F is a function with A, A1, A2, ... expressions
       then F(), F(A), F(A, A1), F(A, A1, A2), ...
      ```
    - R7 if O.f(E)
    - ```
       if O, f, E, E1, ...
       then O.f(), O.f(E), O.f(E, E1), ...
      ```
1. **Printing**
1. ```
   print("hello", 'how')
   print("hello", end='')
   from pprint import *
   pprint(expressions)
  ```
1. **Functions**
1. *anonymous*
1. - **lambda**
    - ```
       lambda x: x
      ```
    - **def**
    - ```
      def f(x,y):
        return x + y
      ```
    - ```
      def h():
        "hello"
        #This function returns None
      h() #None
      ```
    - **keyword**
    - ```
      def f(x=0, y=0):
        print("x = ", x, "y = ", y)
        return (x, y)
      f(x=1, 2)
      f()
      f(1)
      ```
    - **Destructuring with Tuples**
    - *positional*
    - ```
      def ff(*a):
        print("first = ", a[0], "Second = ", a[1])
        return (len(a), a)
      ```
    - **Destructuring with Dictionaries**
    - ```
      def fff(**a):
        print(a["first"])
        return a
      ```
    - **destructuring with both**
    - ```
      def g(*a,**b):
        return (a,b)
      ```
1. **Methods**
1. ```
   x+1
   [is actually]
   x.__add__(1)
  ```
1. - **Magic Methods**
    - ```
      __add__(self, y)        # x + y
      __sub__(self, y)        # x - y
      __mul__(self, y)        # x * y
      __mod__(self, y)        # x % y
      __neg__(self)           # -x
      __eq__(self, y)         # x == y
      __ge__(self, y)         # x >= y
      __gt__(self, y)         # x >  y
      __lt__(self, y)         # x <  y
      __le__(self, y)         # x <= y
      __ne__(self, y)         # x != y
      __contains__(self,y)    # y in x
      __getitem__(self, y)    # x[y]
      __setitem__(self, i, y) # x[i] = y
      __hash__(self)          # hash(x)
      __int__(self)           # int(x)
      __iter__(self)          # for y in x
      __len__(self)           # len(x)
      __repr__(self)          # repr(x)
      __str__(self)           # str(x)
      ```
1. **Some Builtins**
1. ```
   abs, min, max
   type
   len
   dir
  gives internal dictionary of names
  ```
1. **Testing**
1. ```
   Doctests
   test_sqrt.py
  """
  >>> sqrt(4)
  2.0
  >>> sqrt(2)
  1.4142135623730951
  >>> sqrt(-1)
  0+1j
  """
  from sqrt import *
  if __name__ == "__main__":
      import doctest
      doctest.testmod()
   sqrt.py
  def sqrt(x):
    x**0.5
  ```
1. **Conditionals**
1. ```
  if  expr:
    expr
  elif expr:
    expr
  else:
    True
  ```
1. ```
  while x:
    expr
      break;
  ```
1. **break**
1. **continues**
1. **Sequence Operations**
1. - **Slicing**
    - **before**
    - ```
      '0123456789'[1:5]
      [0,1,2,3,4,5,6,7,8,9][1:5]
      ```
    - **step**
    - `sequence[i;j;k]`
    - ```
      s = "Python"
      s[::-1] #'nohtyP'
      s[::2] #'Pto'
      ```
    - **Strings**
    - - split
          - ```
            'this.is.a.string'.split('.')
            ''.split(':')
            ```
    - **for loops**
    - [learn.txt (txt)](/assets/learn-txt.txt)
    - ```
      cities = ["London", "New York", "Paris", "Oslo", "Helsinki"]
      for city in cities:
        print(city)
      colors = {'crimson': 0xdc143c, 'coral': 0xff7f50, 'teal': 0x008080}
      for color in colors:
        print(color, colors[color])
      from urllib.request import urlopen
      def get_words():
          with urlopen('http://thevikidtruth.com/5000/!download?-A1624') as story:
              story_words = []
              for line in story:
                  line_words = line.decode('utf-8').split()
                  for word in line_words:
                      story_words.append(word)
          for word in story_words:
              print(word)
      if __name__ == '__main__':
          get_words()
      ```
1. **Classes**
1. - **Creating Classes**
    - **class**
    - **data**
    - **actions**
    - **instances**
    - **attribute**
    - **method**
    - ```
      class Microphone():
        """ A Documentation String """
        def __init__(self, type, volume=50):  #init method is
          self.type = type                    #called automatically
          self.volume = volume                #self=current instance
        def record(self, input):
          """blah blah"""
          print(f"using \{self.type\} on \{input\}.")
      ```
    - ```
      mic1 = Microphone('laffler')
      mic1.record(5)
      ```
    - **Inheritance**
    - ```
      class Condenser(Microphone):
        """documentation"""
        def __init__(self, type, volume=30):
          super().__init__(type, volume)
          self.power = True
        def record(self, input):
          if self.power == True:
            super().record(input)
            print(" And I have power")
          else:
            print("Please put on Power.")
      ```
    - ```
      mic2 = Condenser('heavy')
      mic2.record(4)
      mic2.power
      ```
1. **User Input**
  ```
  name = input("what is your name? ")
  ```
