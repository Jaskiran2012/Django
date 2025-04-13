# userauth/views.py
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import EmployeeCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.is_admin = form.cleaned_data['is_admin']
            user.profile.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to appropriate page which is choose role dashboard.
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})






@login_required
def add_employee_view(request):
    if not request.user.profile.is_admin:
        messages.error(request, "Only admins can add employees.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.is_admin = False  # Ensure employee is not admin
            user.profile.save()
            messages.success(request, f"Employee {user.username} created successfully.")
            return redirect('dashboard')
    else:
        form = EmployeeCreationForm()
    return render(request, 'add_employee.html', {'form': form})
