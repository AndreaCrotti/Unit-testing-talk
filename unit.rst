==============
 Unit testing
==============

.. TODO: find a nice example to use to do the interactive talk

Why
===

**If it's not tested, it's broken**

.. literalinclude:: code/funcs.py
    :pyobject: smart_function

Can you see the problem?

Dynamic Python
==============

- names are bound at run-time
- things can change


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


Coverage
========

Trace program execution

Demo time
=========

.. call people out to create a simple project done via unit testing.
.. first write the test and then write the implementation


Links
=====

.. _mock:
.. _coverage:
.. _nose:
