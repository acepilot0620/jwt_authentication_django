from rest_framework.test import APITestCase
from rest_framework.views import status

from assignment.factories import UserFactory, LedgerFactory

class LedgerTestCase(APITestCase):
    def setUp(self):
        self.url = '/ledger'
        self.user = UserFactory()
        self.ledger = LedgerFactory.create(
            user=self.user, earning=10000, spending=0)