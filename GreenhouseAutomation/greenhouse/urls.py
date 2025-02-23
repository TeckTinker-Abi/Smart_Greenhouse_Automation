from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('control/', views.control, name='control'),
    path('logs/', views.logs, name='logs'),
    path('about/', views.about, name='about'),
]
