from django.urls import path
from . import views  # views.py dan funksiyalarni import qilish

urlpatterns = [
    path('', views.home, name='home'),  # Asosiy sahifa (localhost:8000/)
    path('login/', views.login, name='login'),  # localhost:8000/login/
    path('about/', views.about, name='about'),  # localhost:8000/about/
    path('team/', views.team, name='team'),  # localhost:8000/team/
    path('contact/', views.contact, name='contact'),  # localhost:8000/contact/
    path('services/', views.services, name='services'),  # localhost:8000/services/
    
   
]
