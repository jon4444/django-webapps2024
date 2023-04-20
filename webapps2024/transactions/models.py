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
    ...