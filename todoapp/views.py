

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Todo
from .forms import TodoForm, UserRegisterForm

def register(request):
    """Handle user registration"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    """Display the home page with the user's todos"""
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'home.html', {'todos': todos})

@login_required
def add_todo(request):
    """Add a new todo item"""
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, 'Todo added successfully!')
            return redirect('home')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})

@login_required
def edit_todo(request, id):
    """Edit an existing todo item"""
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo updated successfully!')
            return redirect('home')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'edit_todo.html', {'form': form, 'todo': todo})

@login_required
def delete_todo(request, id):
    """Delete a todo item"""
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'Todo deleted successfully!')
    return redirect('home')

@login_required
def complete_todo(request, id):
    """Mark a todo as complete or incomplete"""
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.complete = not todo.complete
    todo.save()
    return redirect('home')