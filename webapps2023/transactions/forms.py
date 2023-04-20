from django import forms
from . import models

class PaymentForm(forms.Form):
    sender = forms.CharField(max_length=30)
    receiver = forms.CharField(max_length=30)
    amount = forms.CharField(max_length=30)
    
    class Meta:
        model = models.CustomerTransfer
        # fields = ['enter_your_username', 
        #           'enter_destination_username', 
        #           'enter_amount_to_transfer'
        #           ]
        
class PaymentRequestForm(forms.Form):
    requester = forms.CharField()
    payer = forms.CharField()
    amount = forms.DecimalField()