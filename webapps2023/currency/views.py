from django.shortcuts import render
import requests
import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CurrencyConverter
from .serializers import CurrencyConverterSerializer
from .forms import CurrencyConversionForm

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


def currency_conversion(request):
    form = CurrencyConversionForm(request.GET or None)

    if form.is_valid():
        base_currency = form.cleaned_data.get('base_currency', 'USD')
        target_currency = form.cleaned_data.get('target_currency', 'EUR')
        amount = form.cleaned_data.get('amount', 100)

        url = f'http://127.0.0.1:8000/currency/?base_currency={base_currency}&target_currency={target_currency}&amount={amount}'

        response = requests.get(url)
        print(response.content) # new
        data = response.json()

        if 'converted_amount' in data:
            converted_amount = data['converted_amount']
        else:
            converted_amount = None

        context = {'form': form,
                   'converted_amount': converted_amount,
                   }
        return render(request, 'currency2.html', context)

    # print('Converted amount:', converted_amount)
    context = {'form': form}
    return render(request, 'currency2.html', context)