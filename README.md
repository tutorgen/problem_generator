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

route                          | options   | description 
-------------------------------|-----------|-------------
/list                          |           | List everything supported
/subject/list                  |           | List the subjects supported
/:subject/category/list        |           | List the categories supported for a specific subject
/:subject/:category/skill/list |           | List the skills supported for a specific subject and category
/:subject/:category/:skill/new | count=int | Generate a new problem for a specific subject, category and skill
/:subject/:category/new        | count=int | Generate a new problem for a specific subject and category
/:subject/new                  | count=int | Generate a new problem for a specific subject

License
=======

Copyright (c) 2014, TutorGen
All rights reserved.

Contributors
---
Raymond Chandler III

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the {organization} nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
