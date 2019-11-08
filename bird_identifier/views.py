from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Bird, ModelWithFileField
from django.contrib.auth import logout
from django.urls import reverse
from .forms import UploadFileForm
from django.http import HttpResponse

# Main page to be templated
def index(request):
    return render(request, 'bird_identifier/information.html')

# Contains results
def results(request):
    return render(request, 'bird_identifier/results.html')

def success(request):
    return HttpResponse('Success')

# Contains upload
def upload(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(form.errors)
        
        if form.is_valid():
            print("From is valid")
            instance = ModelWithFileField(user_photo=request.FILES['file'])
            instance.save()
            return redirect('success')
        else:
            print(form.errors)

    else:
        form = UploadFileForm()
    
    return render(request, 'bird_identifier/upload.html', {'form': form})