from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Include routes from another app
    path('quickstart/', include('quickstart.urls')),

    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Role/Mode selection
    path('choose-mode/', views.choose_mode_view, name='choose-mode'),
    path('choose-role/', views.choose_role_view, name='choose-role'),
    path('add-employee/', views.add_employee_view, name='add_employee'),

    # Dashboards
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('employee-dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('personal-dashboard/', views.personal_dashboard, name='personal_dashboard'),

    # Ticket management
    path('create-ticket/', views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/status/<str:new_status>/', views.update_ticket_status, name='update_ticket_status'),
    path('ticket/<int:ticket_id>/reassign/', views.reassign_ticket, name='reassign_ticket'),

    # To-do API
    path('api/todos/', views.get_todos, name='get_todos'),
    path('api/todos/add/', views.add_todo, name='add_todo'),
    path('api/todos/update/<int:todo_id>/', views.update_todo, name='update_todo'),
    path('api/todos/delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),

    # Diary
    path('diary/', views.diary_view, name='diary'),
]
