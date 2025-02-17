from django.urls import path
from . import views  # views.py dan funksiyalarni import qilish

urlpatterns = [
    path('', views.home, name='home'),  # Asosiy sahifa (localhost:8000/)
    path('login/', views.login, name='login'),  # localhost:8000/login/
    path('about/', views.about, name='about'),  # localhost:8000/about/
]
