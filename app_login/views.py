from django.shortcuts import render,HttpResponseRedirect,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from app_login.models import Profile
from app_login.forms import SignUpForm,ProfileForm
from django.contrib import messages
import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket

# Create your views here.
def Signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully!")
            return HttpResponseRedirect(reverse('app_login:login'))
    return render(request,'app_login/Signup.html',context={'form':form})

def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('app_shop:Home'))
    return render(request,'app_login/login.html',context={'form':form})
@login_required
def logout_user(request):
    logout(request)
    messages.warning(request,"You Are Logged Out")
    return HttpResponseRedirect(reverse('app_shop:Home'))
@login_required
def profile_user(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,"Saved Change")
            form = ProfileForm(instance=profile)
    return render(request,'app_login/change_profile.html',context={'form':form})


@login_required
def payment(request):
    saved_address = Billingaddress.objects.get_or_create(user=request.user)
    if not saved_address[0].is_fully_filled():
        messages.info(request,f"Please complete shipping address!")
        return redirect("app_payment:checkout")
    if not request.user.Profile.is_fully_filled():
        messages.info(request,f"please complate profile detailes!")
        return redirect("app_login:profile")
    return render (request,"app_payment/payment.html",context={})
