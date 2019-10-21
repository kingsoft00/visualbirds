from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Bird
from django.contrib.auth import logout
from django.urls import reverse

# Main page to be templated
def index(request):
    return render(request, 'bird_identifier/base.html')

# Contains results
def results(request):
    return render(request, 'bird_identifier/results.html')

# Contains upload
def upload(request):
    return render(request, 'bird_identifier/upload.html')