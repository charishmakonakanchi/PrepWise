from extensions import db


class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255), nullable=False)

    answer = db.Column(db.Text, nullable=False)

    difficulty = db.Column(
        db.Enum("Easy", "Medium", "Hard"),
        nullable=False
    )

    company = db.Column(db.String(100))

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )

    def __repr__(self):
        return f"<Question {self.title}>"