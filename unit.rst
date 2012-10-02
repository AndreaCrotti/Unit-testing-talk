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

    >>> uppercase_words("Word1")
    >>> ['W', 'O', 'R', 'D', '1']

- no compiler help
- extremely dynamic language

Functions
=========

*pure function*

.. literalinclude:: code/funcs.py
    :pyobject: adder


Side effects
============

.. something on testing classes (setUp tearDown)

.. literalinclude:: code/funcs.py
    :pyobject: silly_function

**WRONG**



Dynamic Python
==============

- names are bound at run-time
- things can change

.. literalinclude:: code/library.py


Dynamic Python 2
================

Rebinding names from other modules!

.. literalinclude:: code/prog.py


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
