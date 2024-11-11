from django.shortcuts import render,redirect
from django.http import request, HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout   
from django.contrib.auth.decorators import login_required
from store.models import Product



# Create your views here.
@csrf_exempt
def SignUp(request):
    if request.method != "POST":
        return HttpResponse("Something went wrong!")

    uname = request.POST.get('username')
    email = request.POST.get('email')
    pass1 = request.POST.get('password1')
    pass2 = request.POST.get('password2')

    if pass1 != pass2:
        return HttpResponse("Both Password and Confirm Password must be equal!")

    try:
        new_user = User.objects.create_user(username=uname, email=email, password=pass1)
        new_user.save()
        print("User saved successfully!")
        return redirect('loginPage')
    
    except Exception as e:
        print(f"Error occurred: {e}")
        context = {'data': "An error occurred while creating the user."}
        return render(request, 'Error.html', context)

def LoginPage(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

@csrf_exempt
def Login(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(request,username=uname,password=passw)
        if user is not None:
            login(request,user)
            return redirect('home')
        return render(request,'Error.html',context={'data':"Incorrect Usernmae and Password "})
    
def Index(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())

def LogoutPage(request):
    return HttpResponse("<h2> LogOut Route Working Properly </h2>")

@login_required(login_url='login')
def HomePage(request):
    produts = Product.objects.get()
    context = {
        'products':produts
    }
    return render(request,'home.html',context)
   
    