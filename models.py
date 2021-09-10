"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG = "https://cdn.imgbin.com/22/9/15/imgbin-user-profile-default-computer-icons-network-video-recorder-avatar-cartoon-maker-6Hsz5aDj13zCrN6KVeVqqTtCp.jpg"


class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMG)

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"


def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)
