from django.urls import path

from .views import index, send_mail

urlpatterns = [
    # path to index home page
    path('', index, name='index'),
    # Path to send data for email
    path('send_mail/', send_mail, name='send_mail'),
]
