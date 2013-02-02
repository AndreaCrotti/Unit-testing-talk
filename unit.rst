.. TODO: add example of a "sed/like" function and how to move out the logic of replacing

==============
 Unit testing
==============

.. First of all an introduction about myself, I'm not a great expert
.. of Test Driven Development, because I started to do it properly
.. only 6 month ago.

.. However, having worked with and without I really decided that I'm
.. never going to do the mistake to work in another way anymore, and
.. I'm also now doing pushing all the people around me to do the same.

.. I recently changed job and in my new job there are no almost no
.. tests, I created the whole infrastrure and told my colleagues how
.. to do them and we already see the benefits.

**If it's not tested, it's broken**


Twitter: @andreacrotti

Slides: https://github.com/AndreaCrotti/Unit-testing-talk


Benefits
========

.. If you really embrace TDD I can promise you a few things that will
.. really improve the way you work.

.. Here are some of the benefits that you I think will gain.

.. If you have a good test coverage you will almost never need again
.. to spend endless time with your debugger, trying to find out what's
.. happened, because it will be very easy to know what can be the
.. source.

.. The last one seems exagerated but for me it was not.  When I had
.. some code without tests and someone asked me if it worked, the best
.. answer I could give is "it didn't fail yet", even if I thought
.. the code was good.
.. But I had no proof of what were the boundaries, I could only trust
.. myself that I did a good job.

- forget your debugger
.. TODO: fixme this 
- avoid over-engineering (small steps when required)
- better design and better code
.. FIXME: not good
- do only what necessary
- sleep at night



Dynamic language
================

.. So Python is a great language, but it's also very dynamic and
.. basically it only gives you runtime errors (except for syntax
.. errors).  You can use some great tools like Pylint to get a much
.. better static analysis but it's still far from what you can get
.. from a less dynamic language.
.. So more than enough rope to hang yourself!

*Python is awesome*, but...

- no type checking
- no checked exceptions
- no compilation

.. image:: img/noose.jpg

Why
===
.. Here for example I have this function that under some rare
.. condition would fail
.. Can you see any problem with it?

.. rst-class:: build

.. code-block:: python
   
    Traceback (most recent call last):
      File "rare_cond.py", line 21, in <module>
        smart_function(42)
      File "rare_cond.py", line 7, in smart_function
        report_error(argO)
    NameError: global name 'argO' is not defined
    
.. literalinclude:: code/rare_cond.py
    :pyobject: smart_function

Fail
====

.. image:: img/testing-goat.jpg
   :scale: 150%
    
Why 2
=====

.. Here is another example from my personal experience, I actually got
.. bitten many times by this.  What happens if you pass by mistake a
.. string instead of a list of strings to a function that takes an
.. iterable?

.. Well thanks to duck typing it just threats the string as an
.. iterable and gives you a result, which is most likely not the one
.. you want!

.. rst-class:: build

::

    ['W', 'O', 'R', 'D', '1']

::

    >>> uppercase_words("word1")


.. literalinclude:: code/wrong.py
    :pyobject: uppercase_words

Does not fails, but still clearly **wrong**

Fail
====

.. image:: img/testing-goat.jpg
   :scale: 150%


Unit test
=========

.. The good news though is that Python is really awesome for writing
.. unit tests, (I even used it in the past to unit test java code with
.. Jython for example).

.. A unit test is small, isolated, testing a very small part of the
.. code.  When a test fail you would know the 5-lines range of code
.. that generates the problem.

.. It's not a unit test if something else that it's not the specific
.. part of the code has to work

.. The fast is really important actually, because for TDD you really
.. need to run your tests continuosly, before every commit, and if you
.. start to have slow tests it will get too annoying very quickly.

- small
- isolated
- localized
.. FIXME: check
- don't depend on anything external
- *fast*

Not a unit test
===============

.. Here is an example 

.. literalinclude:: code/not_unit.py

Change of perspective
=====================

.. TODO: add 

Not *how I hack a solution for this*, but *how do I test it*?

What is the easiest thing to test?

.. TODO: add something

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

Dependency injection
====================

.. literalinclude:: code/dep_inj.py
    :lines: 1-6

How do I remove the external dependecy?

*Dependency injection*

Dependency injection 2
======================

.. literalinclude:: code/dep_inj.py
    :pyobject: ReportDep
    
.. literalinclude:: code/dep_inj.py
    :pyobject: test_report


*Gets ugly*

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


Mocking
=======

Automate the Mocking process.

.. _mock: http://www.voidspace.org.uk/python/mock/

- patch a name
- mock an object

*Every time I mock I do one step away from the real system*
Functional core, imperative shell.

.. _func_imp: https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell

Patching
========

lib.py:

::

    from os import listdir
    
    def filter_dirs(pth):
        for l in listdir(pth):
            if 'x' in l:
                yield l
    
test_lib.py:

::

    class TestLib(unittest.TestCase):
        @patch('lib.listdir', new=lambda x: ['one', 'two', 'x'])
        def test_filter_dirs(self):
            res = list(lib.filter_dirs('.'))
            self.assertEqual(len(res), 1)

Mocking
=======

Mock the behaviour of an object that we don't want to run.

::

    class ComplexObject(object):
        def method(self):
            print("Very complex and expensive")
    
    
    class Obj(object):
        def __init__(self):
            self.c = ComplexObject()
            self.c.method()
    
::

    fake_complex_object_auto = Mock(autospec=lib.ComplexObject)
    @patch('lib.ComplexObject', new=fake_complex_object_auto)
    def test_obj(self):
        v = lib.Obj()



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


Make it pass
============

.. After we wrote a test, write the simplest thing that can make it
.. pass, and not more

- simplest solution but nothing more

.. show some examples of why these things can be bad (passing wrong types,
.. raising things from anywhere and so on)



Teaser example
==============

.. literalinclude:: code/refactor/refactor.py
   :pyobject: long_crappy_function

.. how can I actually test this function, it takes no arguments and it
.. needs to access to the filesystem, mysql and manipulate a list

.. the great thing about python is that we can still do but it's much
.. harder


Coverage
========

- set a tracer function
- runs a script
- keep track of all the lines executed
- show a report

.. integrates well with nose and other test runners
.. TODO: talk about test discovery somewhere


.. the C code is not quite useful in this case
.. Testing C code
.. ==============

.. - create a shared library
.. - load it with *ctypes*
.. - run it and check the results

..     :language: c
..     :lines: 1-11

.. Testing C code 2
.. ================

.. .. literalinclude:: code/test_c.py
..     :language: python


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
