from werkzeug.security import generate_password_hash

from db import db
from models import User, RoleType


def create_super_user(first_name, last_name, email, password, phone):
    password = generate_password_hash(password)
    user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        role=RoleType.admin,
        phone=phone
    )
    db.session.add()
    db.session.commit()


if __name__ == '__main__':
    # TODO: add values to be fetched from terminal
    create_super_user()
