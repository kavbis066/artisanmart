from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm

def home_page(request):
    context = {
        "title": "home",
        "content": "Welcome to home page"
    }
    return render(request, "home_page.html", context)

def checkout(request):
    context = {
        "title": "home",
        "content": "Welcome to home page"
    }
    return render(request, "checkout.html", context)

@login_required
def login_page_view(request):
    context = {
        "user": request.user,
        "title": "home",
        "content": "Welcome to Home Page"
    }

    print(request.user.username)
    return render(request, "index.html", context)

def about_page(request):
    context = {
        "title": "About",
        "content": "Welcome to abour page"
    }
    return render(request, "home_page.html", context)

def validate(email):
    return email.split('@')[1] == "gmail.com"

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
    
        user = authenticate(username = username, password = password)

        if user:
            if(user.is_active):
                login(request, user)
                return (redirect('/login_page_view'))
            else:
                return HttpResponse("ACOUNT NOT CREATED")
        
        else:
            form = RegisterForm()
            #return render(request, "auth/register.html", {'form':form})
            return (redirect('/register'))
    
    else:
        return render(request, "auth/login.html", {})

def register_page(request):
    error = ""
    registered = False
    if request.method == "POST":
        user_form = RegisterForm(data = request.POST)

        if user_form.is_valid():
            if validate(user_form.cleaned_data.get("email")):
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                registered = True

            else:
                error = "GMAIL email is required"
        
        else:
            print(user_form.errors)
    
    else:
        user_form = RegisterForm()
    
    return render(request, "auth/register.html", {
        'user_form': user_form,
        'registered': registered,
        'error': error
    })