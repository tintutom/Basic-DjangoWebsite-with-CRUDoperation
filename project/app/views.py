from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
def index(request):
    if not request.user.is_authenticated:    
        return render(request,'login.html')
    else:
        return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def handlesignup(request):
    if request.method=='POST':
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")
        if password!=confirmpassword:
            messages.warning(request,"Password is Incorrect")
            return redirect('/signup/')
        try:
            if User.objects.get(username=uname):
                messages.warning(request,"Username is already taken")
                return redirect('/signup/')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is already taken")
                return redirect('/signup/')
        except:
            pass
        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request,"Signup successful")
        messages.info(request,"Please Login")
        return redirect('/login/')

    if not request.user.is_authenticated:    
        return render(request,'signup.html')
    else:
        return render(request,'index.html')

def handlelogin(request):
    if request.method=='POST':
        uname=request.POST.get("username")
        pass1=request.POST.get("pass1")
        myuser=authenticate(username=uname,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login success")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentails")
            return redirect('/login/')
    if not request.user.is_authenticated:    
        return render(request,'login.html')
    else:    
        return render(request,'index.html')

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Sucessful")
    return redirect('/login/')
