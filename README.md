Math Problem Generator
=================

A web service for generating math problem sets.

Dependencies
============
- Python 3.4
- Flask
- SymPy
- Sure (for testing)
- Nose (for testing)

Installation
============
1. Install Python 3.4
2. Install virtualenv
3. Create a new virtualenv: `virtualenv -p python3 env`
4. Activate the virtualenv: `source env/bin/activate`
5. Install Dependencies with pip `pip3 install -r requirements.txt`

6. Run Test Suite `cd tests && nosetests`

7.a. Run the application in debug mode: `python3 app.py debug` or
7.b. Run the application in release mode `python3 app.py release`

Routes
======

route                 | options   | description 
----------------------|-----------|-------------
/category/list        |           | List the categories supported
/:category/skill/list |           | List the skills supported for category
/:category/:skill/new | count=int | Generate a new problem for a specific category and skill (optionally request multiple at a time)
/:category/random     | count=int | Generate a new problem for a specific category (optionall request multiple at a time)