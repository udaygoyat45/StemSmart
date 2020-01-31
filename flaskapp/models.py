from flaskapp import db, login_manager, app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class Email(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):

        return f"User('{self.email}')"