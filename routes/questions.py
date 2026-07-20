from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from extensions import db
from models.question import Question
from models.category import Category
from models.bookmark import Bookmark

questions_bp = Blueprint("questions", __name__)


@questions_bp.route("/questions")
def questions():

    questions = Question.query.all()

    return render_template(
        "questions.html",
        questions=questions
    )


@questions_bp.route("/questions/<int:question_id>")
def question_detail(question_id):

    question = Question.query.get_or_404(question_id)

    return render_template(
        "question_detail.html",
        question=question
    )


@questions_bp.route("/bookmark/<int:question_id>")
@login_required
def bookmark_question(question_id):

    existing = Bookmark.query.filter_by(
        user_id=current_user.id,
        question_id=question_id
    ).first()

    if not existing:
        bookmark = Bookmark(
            user_id=current_user.id,
            question_id=question_id
        )

        db.session.add(bookmark)
        db.session.commit()

    return redirect(
        url_for(
            "questions.question_detail",
            question_id=question_id
        )
    )