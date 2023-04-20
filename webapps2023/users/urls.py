from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    # path('base/', views.base, name='base'),
    path('logout/',  auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('balance/', views.account_balance, name='account_balance'),
]