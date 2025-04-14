from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Ticket


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_admin = forms.BooleanField(label="Sign up as Admin?", required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class EmployeeCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
class TicketCreationForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ticket title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter ticket description'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TicketCreationForm, self).__init__(*args, **kwargs)
        # Only show non-admin users (employees) in the dropdown
        if user:
            self.fields['assigned_to'].queryset = User.objects.filter(profile__is_admin=False)