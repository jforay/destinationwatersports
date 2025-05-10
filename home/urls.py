from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('saftey/', views.saftey,  name='saftey'),
    path('rates/',views.rates, name='rates'),
]
