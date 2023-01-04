import factory
from faker import Faker
from django.contrib.auth.hashers import make_password
from user.models import User
from ledger.models import Ledger

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.LazyFunction(fake.email)
    password = make_password("1q2w3e4r!")
    
class LedgerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ledger
        django_get_or_create = ('user','amount','place','memo', 'ledger_type')
    user = UserFactory()
    amount = factory.LazyFunction(fake.pyint) 
    place = factory.LazyFunction(fake.sentence)
    memo = '비고'
    ledger_type = 'EXP'
    