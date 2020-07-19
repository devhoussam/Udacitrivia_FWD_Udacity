# Full Stack Web Application - 🤩 Trivia API Backend Part 😎😎
Udacity - Full Stack Web Developer 👨‍💻 Nanodegree Project 02

## A. Getting Started 😉😉

### A.1. Installing Dependencies 🔥🔥

#### A.1.1. Python 3.8 👨‍💻👨‍💻

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### A.1.2. Virtual Environment 👨‍💻👨‍💻

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
also, checkout [pipenv](https://pypi.org/project/pipenv/), as it's a great package to manage virtual environments.

#### A.1.3. PIP Dependencies 👨‍💻👨‍💻

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```
bash
pip install -r requirements.txt
```
or
```
bash
pipenv install -r requirements.txt
```

This will install all the required packages we selected within the `requirements.txt` file.

#### A.1.4. Project Key Dependencies 👨‍💻👨‍💻

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## B. setting up 😉😉 

Follow these setup instructions to get the project up and running

### B.1. setting up the environment variables 🔥🔥

Before running the project, you should set some environment variables, preferably in your ```.env``` file.
Below are the environment variables for the project. You can put them in a `.env` file in the root of your virtual environment, or set the variables in the terminal as follows:

```
bash
export FLASK_CONFIG=development
```

- `FLASK_CONFIG`: Specifies a configuration class for the app. possible choices are development, testing, or production. If not set, the app will run in the development environment by default.  
E.G: `FLASK_CONFIG = 'development'`
    - `development`: Start the app in the development environment. `FLASK_ENV` will be set to `development`. which detects file changes and restarts the server automatically.
    - `testing`: Same as development, but with `testing` set to `True`. This helps in automated testing.
    - `production`: Start the app in the production environment, with `FLASK_ENV` set to `production`, and `debug` and `testing` set to `False`.
- `SECRET_KEY`: Set your secret_key which is your data's encryption key. This key should be random. Ideally, you shouldn't even know what it is.  
E.g.: `SECRET_KEY = 'yoursecretkeyhere...'.
- `PROD_DATABASE_URI`, `DEV_DATABASE_URI`, and `TEST_DATABASE_URI`: Set the database uri for SQLAlchemy for the different configuration classes  

```
# Production DB URI
PROD_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/trivia'
# development DB URI 
DEV_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/trivia_dev'
# testing DB URI
TEST_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/trivia_test'
```

### B.1.2. Database Setup (_Important_) 🔥🔥

Install and setup "PostgreSQL" on the system and create a database named `trivia` in the Postgres server.
```bash
createdb trivia
```

Instructions (macOS): https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
cd database
psql trivia < database/trivia.psql
```


### B.1.3. Running the server 🔥🔥

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```
bash
python wsgi.py
```

## C. API Reference 😉😉















