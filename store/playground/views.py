from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Products
from calendar import *


# Create your views here.
def home(request):
    return render(request, "authentication/index.html")


def signup(request):
    # The code below fetches all the input from the user
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already exists")
            return redirect('home')

        if len(username) > 10:
            messages.error(request, "Username too long, must less than ten characters")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")

        if not username.isalnum():
            messages.error(request, "Username must be alpha_numeric")

        # Now after fetching that input from user, we'll save it in a model called User(from.django.contrib.auth.models import User)
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Account created successfuly")
        return redirect('signin')

    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})

        else:
            messages.error(request, "Wrong credentials, please try again")
            return redirect('home')

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def products(request):
    myproducts = Products.objects.all().values()
    template = loader.get_template('products.html')
    context = {
        'myproducts': myproducts
    }
    return HttpResponse(template.render(context, request))
    # return render(request, "authentication/index.html")


def details(request, id):
    myproducts = Products.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myproducts': myproducts,
    }
    return HttpResponse(template.render(context, request))


def calendaR(request):
    (calendar(2023, 2, 1, 8, 3))
    return render(request, "test.html", {'calendar': calendar})
