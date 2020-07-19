# Imports

import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
from config import database_setup
from sqlalchemy import func, desc

# ----------------------------------------------------------------------------#
# Unittest Getting Started 😇😇😇😇😇😇😇😇
# ----------------------------------------------------------------------------#


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize Flask application."""

        db_user = database_setup["user_name"]
        db_name = database_setup["database_name_test"]
        db_pass = database_setup["password"]
        db_port = database_setup["port"]

        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = "postgres://{}:{}@{}/{}".format(
            db_user, db_pass, db_port, db_name
        )
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # ----------------------------------------------------------------------------#
    # @TODO IS DONE 100% 😇
    # Write at least one test for each test for successful operation and for expected errors.
    # ----------------------------------------------------------------------------#

    # ----------------------------------------------------------------------------#
    # Tests for /categories GET 😍😍😍😍
    # ----------------------------------------------------------------------------#

    def test_get_categories(self):

        res = self.client().get("/categories")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["categories"]))

    # ----------------------------------------------------------------------------#
    # Tests for /questions GET 😍😍😍😍
    # ----------------------------------------------------------------------------#

    def test_get_questions(self):

        res = self.client().get("/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["questions"]))

    # ----------------------------------------------------------------------------#
    # Tests for /questions by /categories 😍😍😍😍
    # ----------------------------------------------------------------------------#

    def test_get_questions_by_categories(self):

        res = self.client().get("/categories/2/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["questions"]))

    # ----------------------------------------------------------------------------#
    # Tests for Error (404) - /questions 😒😒😒😒😒
    # ----------------------------------------------------------------------------#

    def test_404_get_questions_beyond_validpage(self):

        res = self.client().get("/questions?page=5")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"], "Resource Not Found 😔😔")

    # ----------------------------------------------------------------------------#
    # Tests for Error (404) - /questions by /categories 😒😒😒😒😒
    # ----------------------------------------------------------------------------#

    def test_404_get_questions_by_categories_beyond_validpage(self):

        res = self.client().get("/categories/10/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"], "Resource Not Found 😔😔")

    # ----------------------------------------------------------------------------#
    # Tests for /questions DELETE 👨‍💻
    # ----------------------------------------------------------------------------#

    def test_delete_questions(self):

        res = self.client().delete("/questions/5")
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 5).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(question, None)

    def test_404_delete_questions_not_exist(self):

        res = self.client().delete("/questions/100")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"], "unprocessable 😁😁")

    # ----------------------------------------------------------------------------#
    # Tests for /questions POST 👨‍💻
    # ----------------------------------------------------------------------------#

    def test_create_questions(self):

        res = self.client().post("/questions", json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_404_create_questions_not_allowed(self):

        res = self.client().post("/questions/100", json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"], "method not allowed 😁😁")

    # ----------------------------------------------------------------------------#
    # Tests for search /questions 🔎🔎🔎🔎
    # ----------------------------------------------------------------------------#

    def test_search_questions(self):

        res = self.client().post("/questions/search", json={"searchTerm": "title"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_404_search_questions_not_found(self):

        res = self.client().post("/questions/search", json={"searchTerm": "123"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"], "Resource Not Found 😔😔")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
