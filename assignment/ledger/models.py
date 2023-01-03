from django.db import models
from user.models import User
from assignment.mixin import TimedModelMixin

class Ledger(TimedModelMixin, models.Model):
    LEDGER_TYPE =(
        ('EXP','지출'),
        ('INC','수입')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0, verbose_name="금액")
    place = models.CharField(max_length=100, verbose_name="사용처")
    memo = models.CharField(max_length=500, verbose_name="메모")
    ledger_type = models.CharField(max_length=3,choices=LEDGER_TYPE, verbose_name="지출or수입 여부")
