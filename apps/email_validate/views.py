# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def index(request):
    return render(request, 'email_validate/index.html')

def add_user(request):
    if request.method == "POST":
        response = User.objects.check_user(request.POST)
    if not response[0]:
        for error in response[1]:
            messages.error(request, error[0])
        return redirect('email_validate:index')
    return redirect('email_validate:success')

def success(request):
    context = {
    'users': User.objects.all().order_by('-created_at'),
    }
    return render(request, 'email_validate/success.html', context)
