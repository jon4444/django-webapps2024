from django import forms

class CurrencyConversionForm(forms.Form):
    base_currency = forms.CharField(max_length=3, required=True)
    target_currency = forms.CharField(max_length=3, required=True)
    amount = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
