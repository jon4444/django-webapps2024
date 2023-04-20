from rest_framework import serializers
from .models import CurrencyConverter

class CurrencyConverterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyConverter
        fields = ('base_currency', 'target_currency', 'rate')
