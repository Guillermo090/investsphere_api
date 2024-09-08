from rest_framework import serializers
from .models import CryptocurrencyTransaction

class CryptocurrencyTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptocurrencyTransaction
        fields = '__all__'