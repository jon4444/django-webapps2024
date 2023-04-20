from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=13, decimal_places=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        details = ''
        details += f'Username : {self.name}\n'
        details += f'Balance  : {self.balance}\n'
        return details
    
class CustomerTransfer(models.Model):
    enter_your_username = models.CharField(max_length=50, null=True)
    enter_destination_username = models.CharField(max_length=50, null=True)
    enter_amount_to_transfer = models.IntegerField(null=True)
    
    def __str__(self):
        details = ''
        details += f'Your username          : {self.enter_your_username}\n'
        details += f'Destination username   : {self.enter_destination_username}\n'
        details += f'Amount to transfer     : {self.enter_amount_to_transfer}\n'
        return details
    

class PaymentRequest(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='recipient')
    amount = models.DecimalField(max_digits=13, decimal_places=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        details = ''
        details += f'Sender    : {self.sender.name}\n'
        details += f'Recipient : {self.recipient.name}\n'
        details += f'Amount    : {self.amount}\n'
        return details
    
class Notification(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message