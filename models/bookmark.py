from extensions import db


class Bookmark(db.Model):
    __tablename__ = "bookmarks"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    question_id = db.Column(
        db.Integer,
        db.ForeignKey("questions.id"),
        nullable=False
    )

    user = db.relationship("User", backref="bookmarks")
    question = db.relationship("Question", backref="bookmarks")