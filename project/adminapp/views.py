from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.template import loader
from django.contrib import messages
from adminapp.models import AdminSignup
from django.contrib.auth.models import User
from django.db.models import Q
# from django.contrib.auth import login,authenticate


def adminhome(request):
    if request.session.get('username'):
        users = User.objects.all().order_by('id')

        # Search functionality
        query = request.GET.get('q')
        if query:
            users = users.filter(Q(username__istartswith=query) | Q(email__istartswith=query))

        admins = AdminSignup.objects.all().order_by('id')
        return render(request, 'adminhome.html', {'s': users, 'p': admins})
    else:
        return render(request, 'adminlogin.html')

def adminlogin(request):
    if request.method=='POST':
        uname=request.POST.get("username")
        pass1=request.POST.get("pass1")
        check_username=AdminSignup.objects.get(username=uname)
        check_password=AdminSignup.objects.get(pass1=pass1)
        if check_username and check_password:
            request.session['username']=uname
            messages.success(request,"Login success")
            return redirect('/adminhome/')
        else:
            messages.error(request,"Invalid Credentails")
            return redirect('/adminlogin/')
    if request.session.get('username'):    
        return redirect('/adminhome/')
    else:
        return render(request,'adminlogin.html')
def adminsignup(request):
    if request.method=='POST':
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        is_admin=True
        try:
            if AdminSignup.objects.get(username=uname):
                messages.warning(request,"Username is already taken")
                return redirect('/adminsignup/')
        except:
            pass
        try:
            if AdminSignup.objects.get(email=email):
                messages.warning(request,"Email is already taken")
                return redirect('/adminsignup/')
        except:
            pass
        myAdmin=AdminSignup()
        myAdmin.username=uname
        myAdmin.email=email
        myAdmin.pass1=password
        myAdmin.is_admin=is_admin
        myAdmin.save()
        messages.success(request,"Signup successful")
        return redirect('/adminhome/')
    
    return render(request,'adminsignup.html')

def adminlogout(request):
    request.session.flush()
    messages.info(request,"Logout Sucessful")
    return redirect('/adminlogin/')

def user_reg(request):
    if request.method=='POST':
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        try:
            if User.objects.get(username=uname):
                messages.warning(request,"Username is already taken")
                return redirect('/user_reg/')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is already taken")
                return redirect('/user_reg/')
        except:
            pass
        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request,"Successfully Added New User")
        return redirect('/user_reg/')

    return render(request,'user_reg.html')


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('adminhome'))


def updateuser(request,id):
    user=User.objects.get(id=id)
    template=loader.get_template('update.html')
    context={
        'user':user,
    }
    return HttpResponse(template.render(context,request))


def updaterecord(request, id):
    if request.method=='POST':
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        myuser=User.objects.get(id=id)
        myuser.username=uname
        myuser.email=email
        myuser.password=password
        myuser.save()
        messages.success(request,"Successfully Updated User")
        return HttpResponseRedirect(reverse('adminhome'))

