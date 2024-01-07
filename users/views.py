from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect

def login_view(request):    
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard')   
    else:
        form = LoginForm(request.POST or None)
        msg = None
        if request.method == "POST":
            if form.is_valid():              
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
            #if user.is_superuser==True:
                if user is not None:
                    if user.is_superuser==True:
                        login(request, user)
                        return HttpResponseRedirect('/dashboard')
                else:
                    msg =True
           #         messages.info(request, "Invalid username or password")
                    return redirect('login')

        return render(request, "users/login.html", {"form": form})
