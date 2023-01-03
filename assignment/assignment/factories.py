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
        django_get_or_create = ('user','earning','spending','place','memo')
    user = UserFactory()
    earning = fake.pyint(min_value=1000, max_value=10000)
    spending = 0
    place = fake.sentence()
    memo = '비고'
    