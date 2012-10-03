==============
 Unit testing
==============

**If it's not tested, it's broken**

Dynamic language
================

- no type checking
- no checked exceptions
- no compilation stage
- monkey patching

.. show some examples of why these things can be bad (passing wrong types,
.. raising things from anywhere and so on)

Why
===

.. literalinclude:: code/funcs.py
    :pyobject: smart_function

Can you see the problem?

Why 2
=====

Works, but is it right??

.. literalinclude:: code/wrong.py
    :pyobject: uppercase_words

Never fails, but still clearly **wrong**

.. code-block:: python

    >>> uppercase_words("word1")
    ['W', 'O', 'R', 'D', '1']

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


Dynamic Python
==============

- names are bound at run-time
- things can change

.. literalinclude:: code/library.py


Dynamic Python 2
================

Rebinding names from other modules!

.. literalinclude:: code/prog.py


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


Mocking
=======

*automating name binding*



Coverage
========

Trace program execution

Demo time
=========

.. call people out to create a simple project done via unit testing.
.. first write the test and then write the implementation

Real conversion
===============

.. take something that is badly coded and rewrite it using tests
.. - reading from the filesystem
.. - generating some results
.. - writing back to the database

.. check for expired files in the log directory and delete the expired ones

.. literalinclude:: code/wrong.py
    :pyobject: remove_expired_files


Links
=====

.. _mock:
.. _coverage:
.. _nose:

.. bad: 69edafd
