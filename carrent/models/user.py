from carrent import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    """Loading the user in login_manager to create a session for him"""
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """This is the user model that interacts with database using SQLAlchemy"""
    id = db.Column(db.Integer ,primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    img_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}') "
