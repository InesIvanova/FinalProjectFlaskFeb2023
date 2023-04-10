from random import randint

import factory

from db import db
from models import User, RoleType, Complaint, State, TransactionModel
from tests.base import mock_uuid


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.commit()
        return object


class UserFactory(BaseFactory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    phone = str(randint(100000, 200000))
    password = factory.Faker("password")
    role = RoleType.complainer
    iban = factory.Faker("iban")


def get_user_id():
    return UserFactory().id


class ComplaintFactory(BaseFactory):
    class Meta:
        model = Complaint

    id = factory.Sequence(lambda n: n)
    title = "Mocked title"
    description = "Mocked desc"
    photo_url = "example.url"
    amount = 20
    created_at = "2020-01-01"
    status = State.pending.name
    user_id = factory.LazyFunction(get_user_id)


def get_complaint_id():
    return ComplaintFactory().id


class TransactionFactory(BaseFactory):
    class Meta:
        model = TransactionModel

    id = factory.Sequence(lambda n: n)
    quote_id = mock_uuid()
    transfer_id = mock_uuid()
    custom_transfer_id = mock_uuid()
    target_account_id = mock_uuid()
    amount = 20
    create_on = "2020-01-01"
    complaint_id = factory.LazyFunction(get_complaint_id)
