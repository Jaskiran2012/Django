from django.shortcuts import render

# Defined the view for the home page
def home_view(request):
    return render(request, 'home.html')