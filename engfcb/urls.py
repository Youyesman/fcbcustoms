from django.urls import path

from . import views

urlpatterns = [
    path('', views.engindex, name='engindex'),
    path('fcb/privacy.html',views.privacy, name='privacy'),
    
]