## Purpose of the repository
It presents some patterns used in python testing: patching, using mocks, running different scenarios.

## Layout:
Code which is being tested is located in main.py and django_like.py.  
main.py file contains some functions which: make a request to external API (coinpaprika), use "django like" models (but without any database) and so on.  
django_like.py contains simple classes which are similar in a layout to Djagno ORM - model, which contains "objects" property for which you can query a database.  
Filter query has time.sleep added to simulate time of query (to show how mocking dependencies makes test faster).  

## How to run the code
- Create venv
- Activate venv
- Install dependencies from requirements.txt
- Run command: `pytest`
