.. TODO: functional core, imperative shell

.. TODO: the best thing with TDD is that you will learn to write
.. better code what's the easiest thing to test? A pure function with
.. no side effects is the easiest thing, because you can simply
.. declare a dictionary of input output

.. add example of a "sed/like" function and how to move out the logic of replacing

==============
 Unit testing
==============

.. TODO: where should I talk about Designing for testability??

**If it's not tested, it's broken**


Testing
=======

- **Unit testing**:

  Testing individual units of source code, where a *unit* is the smallest testable part.

- **Integration testing**:

  Individual software modules are combined and tested as a group.

- **Validation testing**:

  Software system meets specifications and that it fulfills its intended purpose.

**Design for testability**

Teaser example
==============

.. literalinclude:: code/refactor/refactor.py
   :pyobject: long_crappy_function

Unit testing cycle
==================

1. add a test, focusing on the *requirements*
2. run the test to make it fail
3. make it pass minimally
4. refactor
5. back to 1

.. show an example of how this is done

Writing the test
================

- understand the requirement
- focus on *how do I test it*

.. TODO: example of test that shows the requirement very well

.. Being able to write the tests before writing the code means that we
.. really need to understand the requirement well, and we force
.. ourselves to take some time thinking about them, before we get
.. cracking writing some code.

Make it fail
============

.. this second step is understimated but it's very important, because
.. it removes the possibility that the test you're writing would not
.. be always passing for a programming error, and thus completely useless

.. The reason is that there is nothing wrong than having tests with
.. simple bugs that are always passing, because in this way you would
.. never check that the bug is in the *empty* since there is a passing
.. test for that.

- the test should fail if there is a bug

::
    class Queue(object):
        def __init__(self):
            self.queue = []
    
        def empty(self):
            return self.queue == []
    
::

    def test_queue_empty():
        q = Queue()
        assert q.empty, "Queue is not empty in the beginning"

::

     assert q.empty(), "Queue is not empty"


Dynamic language
================

- no type checking
- no checked exceptions
- no compilation
- monkey patching

.. show some examples of why these things can be bad (passing wrong types,
.. raising things from anywhere and so on)

Why
===

.. rst-class:: build

.. code-block:: python
   
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

Does not fails, but still clearly **wrong**

Pure Functions
==============

.. literalinclude:: code/funcs.py
    :pyobject: adder

Passing input X to function F will always return the same output Y.

- adder(1, 2) = 3
- adder(3, 4) = 7

.. show how to test pure functions, in calc_one.py and calc_2.py


Testing pure functions
======================
.. literalinclude:: code/calc_1.py
    :lines: 1-16

.. show examples from calc_1.py and calc_2.py

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

**Hard to test!!**


Unit testing
============

Test Driven Development:

1. write a specific test
2. watch it fail
3. make it pass
4. go back to 1

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

library.py:

.. literalinclude:: code/library.py


Dynamic Python 2
================

Rebinding names from other modules!

prog.py:

.. literalinclude:: code/prog.py


Coverage
========

- set a tracer function
- runs a script
- keep track of all the lines executed
- show a report

.. integrates well with nose and other test runners
.. TODO: talk about test discovery somewhere


Testing C code
==============

- create a shared library
- load it with *ctypes*
- run it and check the results

.. literalinclude:: code/sum.c
    :language: c
    :lines: 1-11

Testing C code 2
================

.. literalinclude:: code/test_c.py
    :language: python


Conclusion
==========

.. rst-class:: build

**Don’t worry about tests, Chuck Norris’s test cases cover your code too.**

- tests are good
- tests are documentation
- testing is easy
- testing alleviates the fear of change
- testable code is *better code*

.. bad: 69edafd
