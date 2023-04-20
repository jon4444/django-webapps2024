from django.db import models

# Create your models here.
class CurrencyConverter(models.Model):
    base_currency = models.CharField(max_length=3)
    target_currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=13, decimal_places=6)
    
    def __str__(self):
        return f"{self.base_currency}/{self.target_currency}: {self.rate}"