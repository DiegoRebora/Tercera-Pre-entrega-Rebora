from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def about_me(request):
    return render(request, 'PadelApp/about_me.html')
