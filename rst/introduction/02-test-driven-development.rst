Test Driven Development
#######################

..  include::   /header.inc

Writing code is simple. Well, it should be. But making sure your code does the
right thing is much harder. In today's development world, testing is the most
important way we verify that our code does what we want. So, in this set of
experiments, I will use `Test Driven Development`_ in writing the code. This
will not be as easy as I would like, simply because the programs I will write
need a graphical display. Testing how something looks is very hard, so we will
not deal with that. Instead, we will focus on testing that the user interface
works as desired, ans leave the artistic aspects of the code to the user's eye!

The starting point for this development is the Python code I wrote back in
2003 while working on am M.S. in Computer Science. At that time I was just
beginning to explore Python, and the easiest graphical tool set I could find
was Tkinter_ and the `Python Mega Widgets`_ tools. These tools are starting to
fall out of favor, so for this version, I want to use more polished tools.
Therefore, I am going to use PyQt5_ and limit my code to the aspects I can test
in a reasonable manner.

QTest
*****

The PyQt5_ project offers a simple testing interface using the QTest module. We
will start off development using this tool and then set up Travis-CI to make
sure testing is done every time we push changes to project code to Github_.

First Test
==========

We start off with a simple test that confirms that the basic application window
is displayed properly. This is something or a "hello, world' test that will
demonstrate the basic testing idea.

We start off with a simple test file that includes the needed libraries:

..  code-block:: python
    :caption:   test/test_gui.py

    import sys
    import unittest
    from PyQt5.QtGui import QApplication
    from PyQt5.QtTest import QTest

    import GUI

in this snippet, we set up the test code to run the actual GUI inteface, which we will set up later

t, we set up a test method that will simple wait for the window to display, then check that the window dimensions match the specifications. This is a basic setup. We will write some code that performs some action, then check that action in the test. This implies that we can query our application code and check the results in a test. Fortunately, pyqt5 supports this kind of work.

..  code-block:: python
    :caption:   test/test_gui.py

    def test-basic-window-geometry(self):
        pass

