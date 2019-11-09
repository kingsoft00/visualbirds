from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Bird, ModelWithFileField
from django.contrib.auth import logout
from django.urls import reverse
from .forms import UploadFileForm
from django.http import HttpResponse
import json
from django.contrib.messages import get_messages
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

def getConfidenceLevels(classes):
    print(json.dumps(classes, indent=2))
    
    classifiers = classes["images"][0]
    classifiers_JSON = classifiers['classifiers'][0]
    confidence_levels = classifiers_JSON["classes"]
    
    return confidence_levels      

def separateConfidenceLevelsIntoWorkable(confidence_levels):

    list_of_confidence_ratings = []

    for n in confidence_levels:
        for x in n.items():

            if x[0] == "class":
                bird_class = x[1]
            if x[0] == "score":
                confidence_score = x[1]

        confidence_rating = (bird_class, confidence_score)
        list_of_confidence_ratings.append(confidence_rating)

    return list_of_confidence_ratings

def determineHighestConfidenceRating(confidence_rating):

    maxRating = 0
    bird_class = ""

    for x in confidence_rating:
        if (x[1] > maxRating):
            maxRating = x[1]
            bird_class = x[0]
    
    return (bird_class, maxRating) 

# Main page to be templated
def index(request):
    return render(request, 'bird_identifier/information.html')

# Contains results
def results(request, highest_score):

    highest_score_bird = Bird.objects.get(watson_id=highest_score[0])
    context = {"bird" : highest_score_bird}

    return render(request, 'bird_identifier/results.html', context)

def success(request):
    return HttpResponse('Success')

# Contains upload
def upload(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = ModelWithFileField(user_photo=request.FILES['file'])

            classes = getResponseFromWatson(instance.user_photo)
            confidence_levels = getConfidenceLevels(classes)
            confidence_ratings = separateConfidenceLevelsIntoWorkable(confidence_levels)
            highest_score = determineHighestConfidenceRating(confidence_ratings)


            return results(request, highest_score)

    else:
        form = UploadFileForm()
    
    return render(request, 'bird_identifier/upload.html', {'form': form})