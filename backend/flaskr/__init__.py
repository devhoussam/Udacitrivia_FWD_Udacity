# ----------------------------------------------------------------------------#
# Imports 😇😇😇😇😇😇😇😇
# ----------------------------------------------------------------------------#

import os
import random
from flask import Flask, request, redirect, url_for, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from werkzeug.exceptions import HTTPException
from models.models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

# ----------------------------------------------------------------------------#
# Application Getting Started 😇😇😇😇😇😇😇😇
# ----------------------------------------------------------------------------#


def create_app(test_config=None):
    # create and configure the Flask application.
    app = Flask(__name__)
    setup_db(app)

    # ----------------------------------------------------------------------------#
    # @TODO IS DONE 100% 😇
    # Set up CORS. Allow '*' for origins.
    # ----------------------------------------------------------------------------#

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # ----------------------------------------------------------------------------#
    # @TODO IS DONE 100% 😇
    # Use the after_request decorator to set Access-Control-Allow
    # ----------------------------------------------------------------------------#

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PATCH,POST,DELETE,OPTIONS"
        )
        return response

    # ----------------------------------------------------------------------------#
    # @TODO IS DONE 100% 😇
    # Create an endpoint to handle GET requests for all available categories.
    # ----------------------------------------------------------------------------#
    @app.route("/categories", methods=["GET"])
    def get_categories():
        try:
            all_cat = Category.query.order_by(Category.id).all()

            categories = {}
            for category in all_cat:
                categories[category.id] = category.type

            if len(all_cat) == 0:
                abort(404)

            return jsonify({"success": True, "categories": categories})

        except AttributeError:
            abort(422)

    # ----------------------------------------------------------------------------#
    # @TODO IS DONE 100% 😇
    # Create an endpoint to handle GET requests for questions,
    # including pagination (every 10 questions).
    # This endpoint should return a list of questions,
    # number of total questions, current category, categories.

    # @TEST IS DONE 100% 😇
    # At this point, when you start the application
    # you should see questions and categories generated,
    # ten questions per page and pagination at the bottom of the screen for three pages.
    # Clicking on the page numbers should update the questions.
    # ----------------------------------------------------------------------------#


def paginate_q(request, questions):
    page = request.args.get("page", 1, type=int)

    q_paginated = questions.paginate(
        page=page,
        per_page=QUESTIONS_PER_PAGE,
        error_out=True,
        max_per_page=QUESTIONS_PER_PAGE,
    )

    current_q = [question.format() for question in q_paginated.items]

    return current_q

    @app.route("/questions", methods=["GET"])
    def get_questions():
        try:

            questions = Question.query.order_by(Question.id)
            current_q = paginate_q(request, questions)

            all_cat = Category.query.order_by(Category.id).all()

            categories = {}
            for category in all_cat:
                categories[category.id] = category.type

            if len(current_q) == 0 or len(all_cat) == 0:
                abort(404)

            return jsonify(
                {
                    "success": True,
                    "questions": current_q,
                    "total_questions": len(questions.all()),
                    "categories": categories,
                    "current_category": None,
                }
            )
        except AttributeError:
            abort(422)

    # ----------------------------------------------------------------------------#
    # @TODO IS DONE 100% 😇
    # Create a GET endpoint to get questions based on category.

    # @TEST IS DONE 100% 😇
    # In the "List" tab / main screen, clicking on one of the
    # categories in the left column will cause only questions of that
    # category to be shown.
    # ----------------------------------------------------------------------------#

    @app.route("/categories/<int:category_id>/questions", methods=["GET"])
    def get_questions_id(category_id):
        try:
            questions = Question.query.filter(Question.category == category_id).all()
            current_q = [question.format() for question in questions]

            if len(current_q) == 0:
                abort(404)

            return jsonify(
                {
                    "success": True,
                    "questions": current_q,
                    "total_questions": len(current_q),
                    "current_category": category_id,
                }
            )

        except AttributeError:
            abort(422)

    # ----------------------------------------------------------------------------#
    # @TODO IS DONE 100% 😇
    # Create a POST endpoint to get questions based on a search term.
    # It should return any questions for whom the search term
    # is a substring of the question.

    # @TEST IS DONE 100% 😇
    # Search by any phrase. The questions list will update to include
    # only question that include that string within their question.
    # Try using the word "title" to start.
    # ----------------------------------------------------------------------------#

    @app.route("/questions/search", methods=["POST"])
    def search_questions():
        try:
            body = request.get_json()
            search_string = body.get("searchTerm", None)

            questions = list(
                Question.query.filter(
                    Question.question.ilike("%" + search_string + "%")
                )
            )

            current_q = [question.format() for question in questions]

            if len(current_q) == 0:
                abort(404)

            return jsonify(
                {
                    "success": True,
                    "questions": current_q,
                    "total_questions": len(current_q),
                    "current_category": None,
                }
            )

        except AttributeError:
            abort(422)

    # ----------------------------------------------------------------------------#
    # @TODO IS DONE 100% 😇
    # Create an endpoint to DELETE question using a question ID.

    # @TEST IS DONE 100% 😇
    # When you click the trash icon next to a question, the question will be removed.
    # This removal will persist in the database and when you refresh the page.
    # ----------------------------------------------------------------------------#

    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_questions(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()

            if question is None:
                abort(404)

            question.delete()

            return jsonify({"success": True,})

        except AttributeError:
            abort(422)

    # ----------------------------------------------------------------------------#
    # @TODO IS DONE 100% 😇
    # Create an endpoint to POST a new question,
    # which will require the question and answer text,
    # category, and difficulty score.

    # @TEST IS DONE 100% 😇
    # When you submit a question on the "Add" tab,
    # the form will clear and the question will appear at the end of the last page
    # of the questions list in the "List" tab.
    # ----------------------------------------------------------------------------#

    @app.route("/questions", methods=["POST"])
    def create_questions():
        try:
            body = request.get_json()

            new_q = body.get("question")
            new_answer = body.get("answer")
            new_difficulty = body.get("difficulty")
            new_category = body.get("category")

            question = Question(
                question=new_q,
                answer=new_answer,
                difficulty=new_difficulty,
                category=new_category,
            )
            question.insert()

            return jsonify({"success": True,})

        except AttributeError:
            abort(422)

    # ----------------------------------------------------------------------------#
    # @TODO IS DONE 100% 😇
    # Create a POST endpoint to get questions to play the quiz.
    # This endpoint should take category and previous question parameters
    # and return a random questions within the given category,
    # if provided, and that is not one of the previous questions.

    # @TEST IS DONE 100% 😇
    # In the "Play" tab, after a user selects "All" or a category,
    # one question at a time is displayed, the user is allowed to answer
    # and shown whether they were correct or not.
    # ----------------------------------------------------------------------------#

    @app.route("/quizzes", methods=["POST"])
    def quiz_questions():
        try:
		
            data = request.get_json()
	    prev_q = data.get("previous_questions", [])
            prev_number_questions = len(prev_q)
            quiz_caty = data.get("quiz_caty", None)

            category_id = quiz_caty["id"]
            output = {}

            if category_id == 0:
                questions = Question.query.filter(
                    Question.id.notin_(prev_q)
                ).all()

            else:
                questions = (
                    Question.query.filter(Question.category == category_id)
                    .filter(Question.id.notin_(prev_q))
                    .all()
                )

            if len(questions) > 0:
                new_q = questions[random.randrange(0, len(questions))].format()
                output["question"] = new_q["question"]
                output["answer"] = new_q["answer"]
                output["id"] = new_q["id"]

                return jsonify({"success": True, "question": output})

            if len(questions) == 0:

                return jsonify({"success": True})

        except AttributeError:
            abort(422)

    # ----------------------------------------------------------------------------#
    # @TODO IS DONE 100% 😇
    # Create error handlers for all expected errors.
    # ----------------------------------------------------------------------------#

    @app.errorhandler(HTTPException)
    def http_exception_handler(error):
        return (
            jsonify(
                {"success": False, "error": error.code, "message": error.description}
            ),
            error.code,
        )

    @app.errorhandler(Exception)
    def exception_handler(error):
        return (
            jsonify(
                {
                    "success": False,
                    "error": 500,
                    "message": f"Something went wrong: {error}",
                }
            ),
            500,
        )

    return app
