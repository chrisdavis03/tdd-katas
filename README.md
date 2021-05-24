# Purpose/Intention
This repo aim to hold my Test Driven Development journal. 

I aim to develop a (mostly) daily practice of TDD methodology.

## Core Principles
1. Write a failing test.
    1. In TDD, we aim NOT to write a line of application code that is not demanded of by a test.
1. Write the simplest code to pass the test. 
1. Refactor

## Learnings

### directrory structure
(not sure how to get 'tree' to ignore pyc files.)
```buildoutcfg
.
├── README.md
├── getting_started
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   └── easy_math.cpython-39.pyc
│   └── easy_math.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-39.pyc
    │   └── conftest.cpython-39-pytest-6.2.4.pyc
    ├── conftest.py
    ├── pytest.ini
    └── test_getting_started
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-39.pyc
        │   └── test_sum.cpython-39-pytest-6.2.4.pyc
        └── test_sum.py

```

### Setup files
The pytest.ini file stores configuration for the 'test' package. 
The conftest.py file stores pytest 'fixtures'.  
Both my be empty at first. 

### Fixtures
Fixtures are located in the conftest.py file and are represented by the @pytest.fixure decorator.
Fixtures are, by default, executed before each test. Fixtures can exist inside the test as well. 

They can be used to clear the database after each test and create a new one before each test.
  

Following this example.
https://testdriven.io/blog/modern-tdd/ 
