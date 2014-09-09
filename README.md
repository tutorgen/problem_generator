Math Problem Generator
=================

A web service for generating math problem sets.

Dependencies
============
Python 3.4
Flask
SymPy

Routes
======

route                   | options   | description 
------------------------|-----------|-------------
/category/list          |           | List the categories supported
/<category>/skill/list  |           | List the skills supported for category
/<category>/<skill>/new | count=int | Generate a new problem for a specific category and skill (optionally request multiple at a time)
/<category>/random      | count=int | Generate a new problem for a specific category (optionall request multiple at a time)