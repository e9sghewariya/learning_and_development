# Learning Python

## 5. Data Structures

Description about Data Structures in python:

-->Lists:
        Methods: append(), extend(), insert(), remove(), pop(), sort(), reverse().
        Use in to test membership.
    List comprehensions
        Short way to build lists: [x for x in range(5)].
        Can include conditions: [x for x in range(10) if x % 2 == 0].
    
-->del statement:
        Delete items or entire lists: del list[0], del list.


-->Tuples:
        Immutable sequences: t = (1, 2, 3).
        Single-element tuples need a comma: (1,).

-->Sets:
        Unordered collections of unique elements.
        Created with set(), set literals {1, 2, 3}.
        Support operations like union, intersection, difference.

-->Dictionaries:
        Key-value pairs: d = {'one': 1, 'two': 2}.
        Keys must be immutable (e.g., strings, numbers).
        Methods: keys(), values(), items(), get(), pop().

-->Looping Techniques:
        Loop through dictionaries: for k, v in d.items().
        Use enumerate() to get index and value.
        Use zip() to iterate over multiple sequences.

-->Common idioms:
        check list emptiness: if not list:.
        Use any() or all() for logical checks.