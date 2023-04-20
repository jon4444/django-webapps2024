from django.urls import path
from . import views 

urlpatterns = [
    path('pay/', views.pay, name="pay"),
    path('pay_transfer/', views.pay_transfer, name="pay_transfer"),
]
