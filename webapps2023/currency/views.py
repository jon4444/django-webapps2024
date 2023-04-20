from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CurrencyConverter
from .serializers import CurrencyConverterSerializer

# Create your views here.
class CurrencyConverterView(APIView):
    def get(self, request):
        # Get query parameters
        base_currency = request.query_params.get('base_currency')
        target_currency = request.query_params.get('target_currency')
        amount = request.query_params.get('amount')
        
         # Check if required parameters are provided
        if not base_currency or not target_currency or not amount:
            return Response({'error': 'Missing query parameters.'}, status=400)

        # Query the database for the exchange rate
        try:
            converter = CurrencyConverter.objects.get(base_currency=base_currency.upper(), target_currency=target_currency.upper())
        except CurrencyConverter.DoesNotExist:
            return Response({'error': f"No exchange rate found for {base_currency}/{target_currency}"}, status=400)

        # Convert the amount
        converted_amount = float(amount) * float(converter.rate)

        # Return the result
        return Response({'converted_amount': converted_amount})