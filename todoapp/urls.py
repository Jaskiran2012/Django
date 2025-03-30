from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    
    # Todo management URLs
    path('', views.home, name='home'),
    path('add/', views.add_todo, name='add_todo'),
    path('edit/<int:id>/', views.edit_todo, name='edit_todo'),
    path('delete/<int:id>/', views.delete_todo, name='delete_todo'),
    path('complete/<int:id>/', views.complete_todo, name='complete_todo'),
]