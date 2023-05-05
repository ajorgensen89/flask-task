from taskmanager import db

# Create two different tables. Using class based model. SQLAlchemy - Model.


class Category(db.Model):
    # Unique ID for the Category model. Acting as primary key - autoincrements.
    # DOT notation on db specifies the type of data used in each column.
    id = db.Column(db.Integer, primary_key=True)
    # Set Max Character count - 25. Ensures unique column and not empty.
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # Not visible. Links to Forgein Key CASCADE deletion.
    # One to many relationship.
    # Lazy - finds categories linked to tasks.
    tasks = db.relationship(
        "Task", backref="category", cascade="all, delete", lazy=True)

    # Create a function.

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Task(db.Model):
    # Unique ID for the Task model. Acting as primary key - autoincrements.
    # DOT notation on db specifies the type of data used in each column.
    id = db.Column(db.Integer, primary_key=True)
    # Set Max Character count - 50. Ensures unique column and not empty.
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    # Text - longer string.
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    # Can include db.Time also.
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey(
            "category.id", ondelete="CASCADE"), nullable=False)

    # Create a function.

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        # Return string for Task class.
        # Using python formatting. DOT(.)format used for
        # indentification of 0,1,2 position. (Could use f"{}" string also.)
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
