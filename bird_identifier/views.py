from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Bird, ModelWithFileField
from django.contrib.auth import logout
from django.urls import reverse
from .forms import UploadFileForm
from django.http import HttpResponse
import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    version='2019-11-05',
    iam_apikey='8VvzgIf3e8WJ_Lh6KlOiPD6KRj1Fm1jCzmjQVIbMNup7'
)

def getResponseFromWatson(file):
    classes = visual_recognition.classify(
            file,
            threshold='0.6',
            classifier_ids='DefaultCustomModel_1403949674').get_result()
    
    return classes

def parseWatsonResponse(classes):
    print(json.dumps(classes, indent=2))

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
        
        if form.is_valid():
            instance = ModelWithFileField(user_photo=request.FILES['file'])
            classes = getResponseFromWatson(instance.user_photo)
            parseWatsonResponse(classes)
            return redirect('results')

    else:
        form = UploadFileForm()
    
    return render(request, 'bird_identifier/upload.html', {'form': form})