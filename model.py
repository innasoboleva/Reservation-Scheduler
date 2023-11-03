from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, DateTime

db = SQLAlchemy()

class User(db.Model):
    """ A user model """

    __tablename__ = "users"

    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)

    reservations = db.relationship("Reservation", back_populates="user")

    @classmethod
    def create(cls, email, password):
         """ Create and return a new user instance """
         return cls(email=email, password=password)

    def __repr__(self):
        return f"<User email={self.email}>"


class Reservation(db.Model):
    """ A reservation model, keeps track of day and time """

    __tablename__ = "reservations"

    reservation_id = db.Column(db.Integer, primary_key=True, autoincrement=True, server_default=text("nextval('reservation_id_seq')"))
    user_email = db.Column(db.String, db.ForeignKey("users.email"), nullable=False)
    date = db.Column(DateTime)

    user = db.relationship("User", back_populates="reservations")

    @classmethod
    def create(cls, date, user):
         """ Create and return a new user reservation instance"""
         return cls(date=date, user=user)

    def __repr__(self):
        return f"<Reservations id={self.reservation_id} date={self.date} >"
    


def connect_to_db(flask_app, db_uri="postgresql:///melon-tasting", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)
    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
