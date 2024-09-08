from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewset import CryptocurrencyTransactionViewSet

router = DefaultRouter()
router.register(r'crypto-transactions', CryptocurrencyTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]