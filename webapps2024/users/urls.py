from django.urls import path
from . import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('base/', views.base, name='base'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
]