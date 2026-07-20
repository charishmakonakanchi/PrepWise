from app import app
from extensions import db
from models.category import Category
from models.question import Question

with app.app_context():

    if Category.query.count() == 0:

        dsa = Category(name="DSA")
        dbms = Category(name="DBMS")
        os = Category(name="Operating Systems")
        hr = Category(name="HR Interview")

        db.session.add_all([dsa, dbms, os, hr])
        db.session.commit()

        questions = [

            Question(
                title="What is a Binary Search Tree?",
                answer="A Binary Search Tree is a binary tree where left child < root < right child.",
                difficulty="Easy",
                company="Amazon",
                category_id=dsa.id
            ),

            Question(
                title="Explain Normalization.",
                answer="Normalization removes redundancy and improves data integrity.",
                difficulty="Medium",
                company="Microsoft",
                category_id=dbms.id
            ),

            Question(
                title="What is Deadlock?",
                answer="Deadlock occurs when processes wait indefinitely for each other.",
                difficulty="Medium",
                company="Google",
                category_id=os.id
            ),

            Question(
                title="Tell me about yourself.",
                answer="Give a concise introduction covering education, skills, projects, and career goals.",
                difficulty="Easy",
                company="General",
                category_id=hr.id
            )
        ]

        db.session.add_all(questions)
        db.session.commit()

        print("Database seeded successfully!")

    else:
        print("Database already contains data.")