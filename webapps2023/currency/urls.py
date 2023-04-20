from django.urls import path
from .views import CurrencyConverterView

urlpatterns = [
    path('currency/', CurrencyConverterView.as_view(), name='currency'),
]
