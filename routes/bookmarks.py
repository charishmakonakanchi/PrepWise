from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.bookmark import Bookmark

bookmarks_bp = Blueprint("bookmarks", __name__)


@bookmarks_bp.route("/bookmarks")
@login_required
def bookmarks():

    bookmarks = Bookmark.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "bookmarks.html",
        bookmarks=bookmarks
    )