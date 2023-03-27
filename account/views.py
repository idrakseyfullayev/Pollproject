from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from django.contrib.auth.models import User
import re
from django.contrib import messages
from account.models import Account
from django.contrib.auth import authenticate, login, logout
# Create your views here.

import re
def check_password(password_):
    if (len(password_)>5 and re.search("[0-9]", password_) and
        (re.search("[a-z]", password_) or re.search('[A-Z]', password_))):
        return True
    else:
        return False


class RegisterView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            if User.objects.filter(username=username):
                messages.info(request, "Please enter another username")
            elif not check_password(password):
                messages.info(request, "password must contain letters and numbers, minimum length must be 6 characters" )
            else:
                user = User.objects.create_user(username=username, password=password)
                Account.objects.create(user=user)
                messages.success(request, "user created")

                login(request, user)
                return redirect("poll:index")

        if not username:
            messages.info(request, 'Please, enter username')
        if not password:
            messages.info(request, "Please, enter password")        

        return redirect('account:register')


class LoginUserView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("poll:index")
        else:
            messages.info(request, "user was not found")
            return redirect('account:login')


class LogoutUserView(generic.View):
    def get(self, request, *args, **kwargs):
        logout(request)        
        return redirect("poll:index")


