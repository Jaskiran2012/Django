from django.urls import path
from . import views
from django.urls import path
from .views import add_employee_view
from .views import signup_view
    
urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('add-employee/', add_employee_view, name='add_employee'),
]



