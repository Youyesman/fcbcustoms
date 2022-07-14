from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fcb/privacy.html',views.privacy, name='privacy'),
    # path('send_email/',views.send_email, name='send_email')
]