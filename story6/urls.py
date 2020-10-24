from django.urls import path
from .views import register, display, register_activites
#url for app
urlpatterns = [
    path('', display, name='display-activities'),
    path('register/', register, name='register-people'),
    path('register-activities/', register_activites, name='register-activities')
]