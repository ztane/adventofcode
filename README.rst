Advent of Code 2016
===================

As solved by Antti Haapala
--------------------------

Last year I did pretty well in Advent of Code until the last puzzle.
The last puzzle proved to be a bit tricky because of lack of coffee - the 
puzzles were released at 7 AM local time, and I couldn't get up early enough
on the Christmas Day and thus wasn't ranked among final top 100.

This year I am a bit smarter and trying to reduce the amount of boilerplate
code - I've made a runner executable and a helper module that contains 
some shortcuts, including reading the input in various ways, so that instead of

:: 

    with open('input') as f:
        for i in f.strip().split(', '):
            

I can directly use

::

    for i in input_split():

The helpers also imports the contents of ``collections``, ``itertools``, ``functools``
and ``math`` so that their contents can be used without prologue.

Finally I've written some useful functions such as ``clamp`` to force a value to be 
within minimum and maximum.

