from django.db import models
from user.models import User
from assignment.mixin import TimedModelMixin

class Ledger(TimedModelMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    earning = models.IntegerField(default=0)
    spending = models.IntegerField(default=0)
    place = models.CharField(max_length=100)
    memo = models.CharField(max_length=500)
