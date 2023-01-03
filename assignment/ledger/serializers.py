from rest_framework import serializers

from .models import Ledger

class LedgerSerializer(serializers.ModelSerializer):
   class Meta:
      model = Ledger
      fields = ['id', 'amount', 'place', 'memo', 'ledger_type']
    
class LedgerEditSerializer(serializers.ModelSerializer):
   amount = serializers.IntegerField(required=False)
   place = serializers.CharField(required=False)
   memo = serializers.CharField(required=False)
   ledger_type = serializers.CharField(required=False)
   class Meta:
      model = Ledger
      fields = ['amount', 'place', 'memo', 'ledger_type']
        
class LedgerReadOnlySerializer(serializers.ModelSerializer):
   class Meta:
      model = Ledger
      fields = ['amount', 'memo', 'ledger_type']