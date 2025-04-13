from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('', views.home_view, name='home'),  # Add the home URL
]