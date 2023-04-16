from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=13, decimal_places=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name