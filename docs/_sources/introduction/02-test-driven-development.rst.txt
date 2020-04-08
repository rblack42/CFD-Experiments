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
was Tkinter_ and the `Python Mega Widgets`_ tools. these tools are starting to
fall in favor, so ror this version, I want to use more polished tools.
Therefore, I am going to use PyQt5_ and limit my code to the aspects I can test
in a reasonable manner.

QTest
*****

The PyQt5 project offers a simple testing interface using the QTest module. We will start off development using this tool and Travis-CI to mke sure testing is done every time we push changes to project code to Github_.
