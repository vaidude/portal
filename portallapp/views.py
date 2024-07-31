from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *  # Import your User model

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            # Create and save the user to the database
            user = User(username=username, email=email, password=password)
            user.save()
            
            # Redirect to a success page or render a success message
            return redirect('login')
        else:
            error_message = 'Passwords do not match'
            return render(request, 'register.html', {'error_message': error_message})
    
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(email=email, password=password).first()
        
        if user:
            # If the user exists, log them in and redirect to the home page
            request.session['user_id'] = user.id
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')

def home(request):
    return render(request,'home.html')