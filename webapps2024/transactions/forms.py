from django import forms


class PaymentForm(forms.Form):
    sender = forms.CharField(max_length=30)
    receiver = forms.CharField(max_length=30)
    amount = forms.CharField(max_length=30)