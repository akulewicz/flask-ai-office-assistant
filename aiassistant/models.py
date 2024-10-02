from aiassistant import db
from flask_login import UserMixin
from aiassistant import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=False, index=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    password = db.Column(db.String(64), nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
    