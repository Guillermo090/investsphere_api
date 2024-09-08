from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CryptocurrencyTransaction
from .serializers import CryptocurrencyTransactionSerializer

class CryptocurrencyTransactionViewSet(viewsets.ModelViewSet):
    queryset = CryptocurrencyTransaction.objects.all()
    serializer_class = CryptocurrencyTransactionSerializer

    def perform_create(self, serializer):
        # Si deseas personalizar alguna lógica en el proceso de creación
        serializer.save(user=self.request.user) 