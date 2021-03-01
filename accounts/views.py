from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
import re
from contacts.models import Contact


def register(request):
    # Sprawdzamy czy zostal wcisniety submit
    if request.method == 'POST':
        # Setting status
        everything_ok = 1

        # Get form values
        # First name w nawiasach to input name
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Check if passwords match
        if password != password2:
            everything_ok = 0
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        

        # Test username length
        if len(username) <= 1 or len(username) > 25:
            everything_ok = 0
            messages.error(request, 'Username length must be between 1 and 25 chars.')
            return redirect('register')           


        # Check if username already exists in db
        # Sprawdzamy czy w bazie danych jest uzytkownik z atrybutem username = username z formularza
        if User.objects.filter(username=username).exists():
            everything_ok = 0
            messages.error(request, 'This username is already taken.')
            return redirect('register')
        

        # Check if email already exists in db
        if User.objects.filter(email=email).exists():
            everything_ok = 0
            messages.error(request, 'This email is being used.')
            return redirect('register')
        

        # Test if email is email
        if not re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email): 
            everything_ok = 0
            messages.error(request, 'Enter valid email.')
            return redirect('register')

        # Register user
        if everything_ok == 1:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

            # Login user after register
            # W drugim parametrze musi byc user ktorego stworzylismy

            # auth.login(request, user)
            # messages.success(request, 'Your are now logged in')
            # return redirect('index')

            user.save()
            messages.success(request, 'You were registered, go log in bitch.')
            return redirect('login')


    else:
        return render(request, 'accounts/register.html')

def login(request):
    # Sprawdzamy czy zostal wcisniety submit
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Sprawdzamy czy user o takich kryteriach istnieje
        user = auth.authenticate(username=username, password=password)

        # Jesli user nie jest niczym to znaczy ze taki user istnieje - mozemy logowac
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else: 
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out. ')
        return redirect('index')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    data = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', data)