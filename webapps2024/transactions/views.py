from django.shortcuts import render, redirect
from .forms import PaymentForm
from django.contrib import messages
from django.db import transaction
import decimal
from .models import Customer

# Create your views here.
def pay(request):
    form = PaymentForm()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        
        if form.is_valid():
            x = form.cleaned_data['sender']
            y = form.cleaned_data['receiver']
            z = decimal.Decimal(form.cleaned_data['amount'])
            print('Sender:', x)
            print('Receiver:', y)
            sender = Customer.objects.select_for_update().get(name=x)
            receiver = Customer.objects.select_for_update().get(name=y)
            
            with transaction.atomic():
                sender.balance -= z
                sender.save()
                
                receiver.balance += z
                receiver.save()
                messages.success(request, 'Your amount is transferred :)')
                
                return redirect('/')
        
        else:
            form = PaymentForm()
            messages.success(request, 'Something went wrong')
            
    return render(request, 'pay.html', {'form':form})