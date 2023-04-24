from django.urls import path
from .views import CurrencyConverterView
from .views import currency_conversion

urlpatterns = [
    path('currency/', CurrencyConverterView.as_view(), name='currency'),
    path('currency2/', currency_conversion, name='currency_conversion'),
]
# http://127.0.0.1:8000/currency/?base_currency=USD&target_currency=EUR&amount=100
