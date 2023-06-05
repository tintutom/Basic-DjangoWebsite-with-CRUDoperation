from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.decorators.cache import never_cache
# Create your views here.

@never_cache
def HomePage(request):
    if 'username' in request.session:
        return render(request,'home.html')
    
    return redirect(LoginPage)

@never_cache    
def SignupPage(request):
    if 'username' in request.session:
        return redirect(HomePage)
    
    if request.method=="POST":
        uname=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        

        if pass1==pass2:
            my_user=User.objects.create_user(username=uname,email=email,password=pass1)
            my_user.save()
            return redirect(LoginPage)
        else:
            messages.warning(request, 'entered passwords are not same!!')
    return render(request,'signup.html')

@never_cache
def LoginPage(request):
    if 'username' in request.session:
        return redirect(HomePage)
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass']
        user=authenticate(username=username,password=pass1,)
        if user is not None:
            request.session['username']=username
            messages.success(request,'logged in successfully')
            return redirect(HomePage)
            
        else:
            messages.warning(request,'Invalid credentials!!')
    return render(request,'login.html')
def LogoutPage(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(LoginPage)