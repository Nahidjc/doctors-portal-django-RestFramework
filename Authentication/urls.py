from django.urls import path
from Authentication.views import registration_view
urlpatterns = [
    path('registration/', registration_view, name='register'),
]
