from flask_testing import TestCase

from config import create_app
from db import db
from managers.auth import AuthManager


def generate_token(user):
    return AuthManager.encode_token(user)


def mock_uuid():
    return "1111-1111"


class TestRESTAPIBase(TestCase):
    def create_app(self):
        return create_app("config.TestingConfig")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
