from rest_framework import serializers

from .models import Ledger

class LedgerReadOnlySerializer(serializers.ModelSerializer):
     class Meta:
        model = Ledger
        fields = ['earning', 'spending', 'memo']

class LedgerSerializer(serializers.ModelSerializer):
     class Meta:
        model = Ledger
        fields = ['id', 'earning', 'spending', 'place', 'memo']
    