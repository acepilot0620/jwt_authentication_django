import factory
from faker import Faker
from django.contrib.auth.hashers import make_password
from .models import User

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = fake.email()
    password = make_password("1q2w3e4r!")