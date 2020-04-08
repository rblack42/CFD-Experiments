Testing on Travis-CI
####################

..  include::   /references.inc

We will be using `Test Driven Development`_ for this project. I use Travis-CI_
for this purpose, and this note covers the testing approach we will need to
use.

One of the goals of this project is to compare solutions using three different
languages. Testing the entire project in one shot is not going to work since
Travis-CI_ only supports setting up a test environment in one language at a
time. The solution to this problem is fairly simple, and probably a good idea
anyway. We can establish a simple solver |API| so additional solvers can be
added later.

Separation of Concerns
**********************

Any software project should be designed so major components as as isolated from
each other as possible. For our CFD_ experiments, that means we build a GUI
interface as a separate subproject, then build CFD_ solvers for each major
language. By making the solvers separate tools, we can even install them on
separate machines, and use a messaging protocol so the GUI_ can fetch results
as needed for display. Each solver module then can be tested independently.

A simple solution seems to be to split the project into separate component
repositories, then merge them into a single package for distribution. For the
present setup that means we will work on these components:

	* CFDexperiments-GUI: Python and PyQt5

	* Solvers

		* CFDexperiments-Python
		* CFDexperiments-Cpp
		* CFDexperiments-Go

The top-level project will host all project documentation, and provide
installation tools to set up a test environment. At some point the GUI module
will support a web-based interface so the experiments can be performed in a
classroom or at home. This feature will be set up at https://cfd.pylit.org
