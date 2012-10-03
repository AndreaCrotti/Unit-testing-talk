==============
 Unit testing
==============

**If it's not tested, it's broken**

Dynamic language
================

- no type checking
- no checked exceptions
- no compilation step
- monkey patching

.. show some examples of why these things can be bad (passing wrong types,
.. raising things from anywhere and so on)

Why
===

.. rst-class:: build

::
   
    Traceback (most recent call last):
      File "funcs.py", line 45, in <module>
        test_smart()
      File "/home/andrea/.local/lib/python2.7/site-packages/mock.py", line 1224, in patched
        return func(*args, **keywargs)
      File "funcs.py", line 24, in test_smart
        smart_function(100)
      File "funcs.py", line 17, in smart_function
        report_error(argO)
    NameError: global name 'argO' is not defined

.. literalinclude:: code/funcs.py
    :pyobject: smart_function
    
Why 2
=====

.. rst-class:: build

::

    ['W', 'O', 'R', 'D', '1']

::

    >>> uppercase_words("word1")


.. literalinclude:: code/wrong.py
    :pyobject: uppercase_words

Never fails, but still clearly **wrong**

Functions
=========

*pure function*

.. literalinclude:: code/funcs.py
    :pyobject: adder


Side effects
============

*In addition to returning a value, it also modifies some state or has an observable interaction with calling functions or the outside world*


.. literalinclude:: code/funcs.py
    :pyobject: silly_function

::

     >>> funcs.silly_function(1)
     3
     >>> funcs.silly_function(1)
     4



Testing
=======

- Unit testing
- Integration testing
- Functional testing


Unit testing
============

- write the test
- watch it fail
- make it pass

.. show an example of this approach

Testing sum
===========

.. literalinclude:: code/funcs.py
    :pyobject: test_adder

.. literalinclude:: code/funcs.py
    :pyobject: adder


Dynamic Python
==============

- names are bound at run-time
- things can change

.. literalinclude:: code/library.py


Dynamic Python 2
================

Rebinding names from other modules!

.. literalinclude:: code/prog.py


Mocking
=======

*automating name binding*


Coverage
========

- set a tracer function
- keep track of all the lines executed
- show a report


Real conversion
===============

.. take something that is badly coded and rewrite it using tests
.. - reading from the filesystem
.. - generating some results
.. - writing back to the database

.. check for expired files in the log directory and delete the expired ones

.. literalinclude:: code/wrong.py
    :pyobject: remove_expired_files


Conclusion
==========

.. rst-class:: build

**Don’t worry about tests, Chuck Norris’s test cases cover your code too.**

- testing is good
- testing is easy
- testing removes the fear of change
- testable code is *better code*


Links
=====

.. _mock:
.. _coverage:
.. _nose:

.. bad: 69edafd
