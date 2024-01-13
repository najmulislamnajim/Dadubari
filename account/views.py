from django.shortcuts import render,redirect
from . forms import UserRegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def user_registration(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('store')
    return render(request,'registration.html',{'form':UserRegistrationForm})

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user=authenticate(username=username,password=password)
            if user is None:
                messages.error(request,'Invalid Password')
                return redirect('login')
            else:
                login(request,user)
                return redirect('store')
        else:
            messages.error(request,'Invalid Username')
            return redirect('login')
    return render(request,'signin.html')

def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('store')
    else:
        return redirect('login')