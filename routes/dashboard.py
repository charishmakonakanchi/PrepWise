from flask import Blueprint, render_template
from flask_login import login_required

from models.question import Question
from models.bookmark import Bookmark
from models.category import Category

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    total_questions = Question.query.count()

    total_bookmarks = Bookmark.query.count()

    total_categories = Category.query.count()

    return render_template(
        "dashboard.html",
        total_questions=total_questions,
        total_bookmarks=total_bookmarks,
        total_categories=total_categories
    )