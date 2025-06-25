from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ImageForm
from .models import Image
# Create your views here.
def home(req):
    if req.method == 'POST':
        form = ImageForm(req.POST, req.FILES) # Create an instance of ImageForm with POST data and files.
        # If the form is valid, save the data to the database.
        if form.is_valid():
            form.save()
    form = ImageForm() # Create a new instance of ImageForm for the empty form.
    img = Image.objects.all() # Fetch all Image objects from the database.
    return render(req, 'home/home.html', {'img':img, 'form': form}) 

def login(req):
    if req.method == 'POST':
        log_email = req.POST.get('email')
        log_pass = req.POST.get('password')
        
        user = authenticate(req, email=log_email, password = log_pass) # Authenticate the user with the provided email and password.
        if user is not None: # If the user is authenticated, proceed to log them in.
            login(req, user) # If the user is authenticated, log them in.
            return redirect('home')
        else:
            messages.error(req, 'Invalid credentials! Please try again.') # If authentication fails, show an error message.
            return redirect('login') 
    return render(req, 'home/login.html')

def signup(req):
    if req.method == 'POST':
        E_mail = req.POST.get('email') # Get the email from the POST request. 
        pass1 = req.POST.get('password1') # Get the first password from the POST request.
        pass2 = req.POST.get('password2') # Get the second password from the POST request.
        if pass1 != pass2: # Check if the two passwords match.
            messages.error(req, 'Passwords do not match!') # If the passwords do not match, show an error message.
            return redirect('signup')
        else:    
            my_user = User.objects.create_user(E_mail,pass1,pass2) # Create a new user with the provided email and password.
            my_user.save() # Save the new user to the database.
            messages.success(req, 'Account created successfully!') # Show a success message.
        return redirect('login')
    return render(req, 'home/signup.html')

