import factory
from faker import Faker
from django.contrib.auth.hashers import make_password
from user.models import User
from ledger.models import Ledger

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = fake.email()
    password = make_password("1q2w3e4r!")
    
class LedgerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ledger
        django_get_or_create = ('user','earning','sending','place','memo')
    user = User()
    earning = 0
    spending = 0
    place = fake.name()
    memo = '비고'
    