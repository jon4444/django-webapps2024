from django.shortcuts import render, redirect
from .forms import PaymentForm
from django.contrib import messages
from django.db import transaction, OperationalError
from decimal import Decimal
from .models import Customer, PaymentRequest, Notification
from .forms import PaymentRequestForm
from . import models

# Create your views here.
# def pay(request):
#     form = PaymentForm()
#     if request.method == 'POST':
#         form = PaymentForm(request.POST)
        
#         if form.is_valid():
#             x = form.cleaned_data['sender']
#             y = form.cleaned_data['receiver']
#             z = decimal.Decimal(form.cleaned_data['amount'])
#             print('Sender:', x)
#             print('Receiver:', y)
#             sender = Customer.objects.select_for_update().get(name=x)
#             receiver = Customer.objects.select_for_update().get(name=y)
            
#             with transaction.atomic():
#                 sender.balance -= z
#                 sender.save()
                
#                 receiver.balance += z
#                 receiver.save()
#                 messages.success(request, 'Your amount is transferred :)')
                
#                 return redirect('/')
        
#         else:
#             form = PaymentForm()
#             messages.success(request, 'Something went wrong')
            
#     return render(request, 'pay.html', {'form':form})

def pay(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            src_username = form.cleaned_data["sender"]
            dst_username = form.cleaned_data["receiver"]
            amount_to_transfer = Decimal(form.cleaned_data["amount"])
            
            src_amount = models.Customer.objects.select_related().get(name__exact=src_username)
            dst_amount = models.Customer.objects.select_related().get(name__exact=dst_username)
            
            try:
                with transaction.atomic():
                    src_amount.balance = src_amount.balance - amount_to_transfer
                    src_amount.save()
                    
                    dst_amount.balance = dst_amount.balance + amount_to_transfer
                    dst_amount.save()
            except OperationalError:
                messages.info(request, f"Transfer operation is not possible now.")
                
        return render(request, "pay_transfer.html", {"src_amount": src_amount, "dst_amount": dst_amount})
    else:
        form = PaymentForm()
    
        
    return render(request, "pay.html", {"form": form})


def pay_transfer(request):
    if request.user.is_authenticated:
        try:
            src_amount = models.Customer.objects.select_related().get(name__username=request.user.username)
            dst_amount = models.Customer.objects.select_related().get(name__username=request.user.username)
        except models.Customer.DoesNotExist:
            messages.info(request, "No amount data found for the authenticated user.")
            return redirect("home")

        transactions_sent = models.Payment.objects.filter(sender=src_amount)
        transactions_received = models.Payment.objects.filter(receiver=dst_amount)

        context = {
            "src_amount": src_amount,
            "dst_amount": dst_amount,
            "transactions_sent": transactions_sent,
            "transactions_received": transactions_received,
        }
        
        return render(request, "pay_transfer.html", {"src_amount": src_amount, "dst_amount": dst_amount})
    else:
        messages.info(request, "You need to be logged in to view this page.")
        return redirect("login")
    
    
def request_payment(request):
    if request.method == 'POST':
        form = PaymentRequestForm(request.POST)
        if form.is_valid():
            requester_username = form.cleaned_data["requester"]
            payer_username = form.cleaned_data["payer"]
            amount_to_request = Decimal(form.cleaned_data["amount"])
            
            requester_customer = Customer.objects.select_related().get(name__exact=requester_username)
            payer_customer = Customer.objects.select_related().get