CFD Experiments
###############
:Author: Roie R. Black
:Date: April 6, 2020
"Email: roie.black@gmail.com
:Documentation: https://rblack42.github.io/CFDexpreiments

|travis-build| |license|

This project hosts my experiments with Computational Fluid Dynamics on a
variety of machines using several common programming languages. The experiment
is based on code I developed in 1975 while working at the USAF Aerospace
Research Laboratory in Dayton, Ohio. The work was part of my (incompleted)
Aerospace Engineering PhD research project. Specifically, we will examining a
simple solution to the problem of axisymmetric flow over a projectile
traveling at high mach numbers. The numerical solution technique used is
reduces the governing Navier-Stokes equations to a parabolized form, then
solves those equations using an  explicit finite-difference scheme based on
MacCormack's Predictor-Corrector method. 

The original code was developed in FORTRAN and ran on a CDC 6600 machine in
about 10 minutes. I even managed to get the code running on an early
Smith-Corona programmable desktop calculator, but the run-time was measured in
many hours.

I rewrote the code in Python in 2003 as part of a course in object-oriented
design at Texas State University while I was working on a Masters in Computer
Science.

The expremnents will cast this solution in three languages: Python, C++, and
Go. The resulting code will be run on a variety of machines including a modern
8-core Intel chip in my Macbook Pro, a Raspberry Pi, a Cluster of eight
Raspberry Pi machines, and on an array of machines hosted on Digital Ocean. In
an ideal world, I may try to get the code run on a modern supercomputer.

..  |travis-build| image:: https://travis-ci.org/rblack42/CFDexperiments.svg?branch=master
    :alt: Build badge from Travis-CI

..  |license| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
    :alt: BSD 3-Clause License

