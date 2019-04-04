# Socialize
[![Build Status](https://travis-ci.org/sohaibfarooqi/socialize.svg?branch=master)](https://travis-ci.org/sohaibfarooqi/socialize)

This application let the user browse questions and record their responses. They will get a shareable link
at the end which they can share with their friends. The app will tell how their answers are as compared to
their friends.

Complete details of application workflow can be found [app_flow.md](app_flow.md)

### Installation and Running
To run this application please follow these steps

 - `git clone https://github.com/sohaibfarooqi/socialize.git`
 - `virtualenv -p python3 .env`
 - `source .env/bin/activate`
 - `pip install -r requirements/dev.txt`
 - `python manage.py migrate`
 - `python manage.py runserver`

To run test cases use:

 - `python manage.py test friendship`
 - `coverage run manage.py test friendship`
 - `coverage report -m`

### Database model
The application consists of following models

  - Question
  - Answer
  - User
  - Quiz
  - QuizResults
  - QuizDetails

They are related to each other in following way:

 - A Question can have one or many answers.
 - A Question can appear in many Quizes and a Quiz can have many Questions.
 - A user can take multiple Quizes and a Quiz can be taken by multiple Users.
 - QuizDetails is associative entity between User and Quiz.
 - QuizResults contains which User responses to Questions in a particular Quiz.

### Static Analysis
This project comes with three static analysis tools

 - bandit (To locate common security flaws in code)
 - autopep8 (PEP8 adherence)
 - isort (Organizing imports)

To run use

  - `bandit -r .`
  - `autopep8 --recursive --in-place campaign`
  - `isort **/*.py`

### Tech Stack

 - Python 3.7.2
 - Django
 - Django Rest Framework
 - autopep8
 - bandit
 - coverage
 - PostgreSQL
 - SQLite

### Further Improvements

 - Provide Fb login support.
 - Implement share on facebook feature.
 - Provide frontend for users.
 - Write more unit tests.
 - Add continuous deployment script.
 - Write integration test.
 - Write load test to determine system's capacity.
 - Deploy application with uWSGI and Nginx.



