from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import AuthenticationForm

from users.forms import CustomUserCreationForm

def home(request):
    return render(request,'home.html')

def userlogin(request):
    form = AuthenticationForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('users:home')
    context = {'form':form}
    return render(request,'login.html',context)

def signup(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form':form}
    return render(request,'signup.html',context)

def userlogout(request):
    logout(request)
    return render(request,'signup.html')